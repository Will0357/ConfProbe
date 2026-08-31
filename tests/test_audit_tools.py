import json
import io
import sys
import tempfile
import types
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

from audit_agent import (
    AGENT_TOOLS,
    AuditRequest,
    ConfProbeAuditHarness,
    OpenAICompatibleAdapter,
    _agent_system_prompt,
    _needs_vendor_search_skill,
    _vendor_result_version,
    review_findings,
    run_audit,
)
from utils.audit_tools import (
    AuditFinding,
    ManualDocument,
    ManualEvidence,
    ManualSourceHealth,
    ManualCommandBlock,
    CommandRecord,
    ProbeCommandGroup,
    audit_probe_commands,
    audit_manual_overcoverage,
    build_manual_index,
    expand_manual_library,
    group_probe_commands,
    load_manual_library,
    load_probe_model,
    render_report,
    search_manual_library_impl,
    search_vendor_site_impl,
    _micro_conflict_reason,
    _macro_conflicts,
    _cisco_search_url,
    _extract_version_hint,
    _parse_cisco_ai_response,
    _search_cisco_with_browser,
    _search_result_matches,
    _vendor_search_phrase,
)


FIXTURES = Path(__file__).parent / "fixtures"
MANUAL_URL = "https://example.invalid/ospf-commands.html"


class FakeReviewer:
    def __init__(self, conclusion="confirmed", confidence=0.92):
        self.conclusion = conclusion
        self.confidence = confidence
        self.calls = []

    def review_findings(self, candidates, audit_context):
        self.calls.append((candidates, audit_context))
        return {
            "reviews": [
                {
                    "finding_id": item["finding_id"],
                    "conclusion": self.conclusion,
                    "evidence_ids": [item["evidence"][0]["evidence_id"]],
                    "confidence": self.confidence,
                    "rationale": "The cited evidence supports this decision.",
                }
                for item in candidates
            ]
        }


class InvalidEvidenceReviewer:
    def review_findings(self, candidates, audit_context):
        return {
            "reviews": [
                {
                    "finding_id": item["finding_id"],
                    "conclusion": "confirmed",
                    "evidence_ids": ["invented:evidence"],
                    "confidence": 0.99,
                    "rationale": "Unsupported citation.",
                }
                for item in candidates
            ]
        }


class FailingReviewer:
    def review_findings(self, candidates, audit_context):
        raise TimeoutError("relay timed out")


class MalformedReviewer:
    def review_findings(self, candidates, audit_context):
        return {"reviews": "invalid"}


class NativeReviewer:
    def agent_turn(self, messages, tools):
        payload = json.loads(messages[1]["content"])
        if tools and len(messages) == 2:
            return {
                "json_action": {
                    "action": "search_manual_library",
                    "arguments": {"query": "documented", "scope": "target"},
                }
            }
        category = payload["candidate_categories"][0]
        return {
            "content": json.dumps(
                {
                    "category": category,
                    "conclusion": "confirmed",
                    "confidence": 0.91,
                    "rationale": "The supplied evidence supports the candidate.",
                }
            )
        }


class FakeHttpResponse:
    def __init__(self, status_code, payload, text=""):
        self.status_code = status_code
        self._payload = payload
        self.text = text

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self):
        return self._payload


class FakeHttpClient:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.calls = []

    def post(self, endpoint, *, headers, json):
        self.calls.append((endpoint, headers, json))
        return next(self.responses)


def probe_group(
    template,
    *,
    view="router",
    variants=(),
    contexts=(),
    group_id="P00001",
):
    return ProbeCommandGroup(
        group_id=group_id,
        template=template,
        normalized_template=template.lower(),
        semantic_view=view,
        kind="terminal",
        variants=tuple(variants) or (template,),
        contexts=tuple(tuple(context) for context in contexts),
        view_paths=(),
        record_ids=(f"probe:{group_id}",),
    )


def finding(finding_id="F00001"):
    evidence = ManualEvidence(
        evidence_id="M1:B0001:syntax:1",
        block_id="M1:B0001",
        kind="syntax",
        text="cost <cost>",
        url=MANUAL_URL,
    )
    return AuditFinding(
        finding_id=finding_id,
        category="B1",
        name="Constraint Missing",
        reason="Range is absent.",
        probe_group_id="P00001",
        probe_template="cost <1-65535>",
        semantic_view="area",
        manual_block_ids=("M1:B0001",),
        manual_commands=("cost (OSPF)",),
        evidence=(evidence,),
    )


class AuditToolsTest(unittest.TestCase):
    def document(self, path=None, title="IOS XR 6.3.1 OSPF Command Reference"):
        return ManualDocument(
            url=MANUAL_URL,
            final_url=MANUAL_URL,
            title=title,
            fetched_at="2026-01-01T00:00:00+00:00",
            html_path=str(path or FIXTURES / "manual.html"),
        )

    def index(self):
        return build_manual_index([self.document()], target_version="6.3.1")

    def test_manual_library_downloads_once_then_uses_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            library = Path(directory) / "manual_db"
            library.mkdir()
            manifest = library / "sources.json"
            manifest.write_text(
                json.dumps(
                    {
                        "vendor": "Cisco",
                        "platform": "IOS XR",
                        "version": "6.3.1",
                        "sources": [MANUAL_URL],
                    }
                ),
                encoding="utf-8",
            )

            def fake_fetch(urls, output_dir, **kwargs):
                manual_dir = Path(output_dir)
                manual_dir.mkdir(parents=True)
                html_path = manual_dir / "manual_001.html"
                html_path.write_text(
                    (FIXTURES / "manual.html").read_text(encoding="utf-8"),
                    encoding="utf-8",
                )
                return [self.document(html_path)]

            with patch("utils.audit_tools.fetch_manuals", side_effect=fake_fetch) as fetch:
                first_documents = load_manual_library(
                    manifest,
                    Path(directory) / "first_run",
                    vendor="Cisco",
                    version="6.3.1",
                )
                second_documents = load_manual_library(
                    manifest,
                    Path(directory) / "second_run",
                    vendor="Cisco",
                    version="6.3.1",
                )

            self.assertEqual(1, fetch.call_count)
            self.assertEqual(MANUAL_URL, first_documents[0].url)
            self.assertTrue(Path(first_documents[0].html_path).is_file())
            self.assertTrue(Path(second_documents[0].html_path).is_file())

    def test_book_landing_page_expands_topics_before_indexing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            landing = root / "book.html"
            landing.write_text(
                '<html><body><a href="/docs/book/ospf-commands.html">OSPF commands</a></body></html>',
                encoding="utf-8",
            )
            document = ManualDocument(
                "https://example.invalid/docs/book.html",
                "https://example.invalid/docs/book.html",
                "Routing Command Reference",
                "",
                str(landing),
                source_url="https://example.invalid/docs/book.html",
                source_role="command_reference",
                source_version="6.3.1",
                is_target_version=True,
                cache_dir=str(root / "cache"),
            )

            def fake_fetch(urls, output_dir, **kwargs):
                target = Path(output_dir) / "manual_001.html"
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text((FIXTURES / "manual.html").read_text(encoding="utf-8"), encoding="utf-8")
                return []

            with patch("utils.audit_tools.fetch_manuals", side_effect=fake_fetch):
                expanded, health = expand_manual_library([document], scope="router ospf")
            blocks, findings = build_manual_index(expanded, target_version="6.3.1")

        self.assertEqual("complete", health[0].status)
        self.assertEqual(1, health[0].indexed_topics)
        self.assertEqual(6, len(blocks))
        self.assertFalse(any(item.category == "C1" for item in findings))

    def test_book_landing_page_expands_all_topics_by_default(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            landing = root / "book.html"
            links = "".join(
                f'<a href="/docs/book/topic-{index}.html">Topic {index}</a>'
                for index in range(129)
            )
            landing.write_text(f"<html><body>{links}</body></html>", encoding="utf-8")
            document = ManualDocument(
                "https://example.invalid/docs/book.html",
                "https://example.invalid/docs/book.html",
                "Routing Command Reference",
                "",
                str(landing),
                source_url="https://example.invalid/docs/book.html",
                source_role="command_reference",
                source_version="6.3.1",
                is_target_version=True,
                cache_dir=str(root / "cache"),
            )

            def fake_fetch(urls, output_dir, **kwargs):
                target = Path(output_dir) / "manual_001.html"
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(
                    (FIXTURES / "manual.html").read_text(encoding="utf-8"),
                    encoding="utf-8",
                )
                return []

            with patch("utils.audit_tools.fetch_manuals", side_effect=fake_fetch):
                _, health = expand_manual_library([document], scope="router ospf")

        self.assertEqual("complete", health[0].status)
        self.assertEqual(129, health[0].discovered_topics)
        self.assertEqual(129, health[0].indexed_topics)

    def test_topic_download_retries_and_unparsed_command_pages_stay_incomplete(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            landing = root / "book.html"
            landing.write_text(
                '<html><body><a href="/docs/book/ospf-commands.html">OSPF commands</a></body></html>',
                encoding="utf-8",
            )
            document = ManualDocument(
                "https://example.invalid/docs/book.html",
                "https://example.invalid/docs/book.html",
                "Routing Command Reference",
                "",
                str(landing),
                source_url="https://example.invalid/docs/book.html",
                source_role="command_reference",
                source_version="6.3.1",
                is_target_version=True,
                cache_dir=str(root / "cache"),
            )
            calls = 0

            def retrying_fetch(urls, output_dir, **kwargs):
                nonlocal calls
                calls += 1
                if calls == 1:
                    raise TimeoutError("temporary timeout")
                target = Path(output_dir) / "manual_001.html"
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text((FIXTURES / "manual.html").read_text(encoding="utf-8"), encoding="utf-8")
                return []

            with (
                patch("utils.audit_tools.fetch_manuals", side_effect=retrying_fetch),
                patch("utils.audit_tools.MANUAL_FETCH_RETRY_DELAY_SECONDS", 0),
            ):
                _, retried_health = expand_manual_library([document], scope="router ospf")

            cache_file = Path(document.cache_dir) / "topics"
            for path in cache_file.rglob("manual_001.html"):
                path.write_text("<html><body>Unsupported chapter layout</body></html>", encoding="utf-8")
            _, incomplete_health = expand_manual_library([document], scope="router ospf")

        self.assertEqual("complete", retried_health[0].status)
        self.assertEqual(1, retried_health[0].retry_count)
        self.assertEqual("incomplete", incomplete_health[0].status)
        self.assertTrue(incomplete_health[0].unparsed_urls)

    def test_single_page_config_guide_without_toc_is_retained(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "guide.html"
            path.write_text(
                "<html><title>OSPF Configuration Guide</title><body>"
                "This page documents the OSPF command and its operational behavior in detail."
                "</body></html>",
                encoding="utf-8",
            )
            document = ManualDocument(
                "https://example.invalid/guide.html",
                "https://example.invalid/guide.html",
                "OSPF Configuration Guide",
                "",
                str(path),
                source_url="https://example.invalid/guide.html",
                source_role="config_guide",
                source_version="7.9",
                is_target_version=False,
            )
            expanded, health = expand_manual_library([document], scope="router ospf")

        self.assertEqual([document], expanded)
        self.assertEqual("complete", health[0].status)

    def test_missing_local_match_is_unresolved_until_searches_complete(self):
        blocks, index_findings = self.index()
        coverage, findings = audit_probe_commands(
            [probe_group("unknown-command")], blocks, index_findings
        )

        self.assertEqual("unresolved", coverage[0].status)
        self.assertEqual(["UNRESOLVED"], [item.category for item in findings])

    def test_harness_emits_command_bound_c1_and_completed_c2(self):
        blocks, index_findings = self.index()
        cost = next(block for block in blocks if block.command_name == "cost")
        other_cost = ManualCommandBlock(
            cost.block_id + ":other",
            cost.command_name,
            cost.title,
            cost.url + "?v=7.9",
            cost.document_title,
            cost.syntax_templates,
            cost.modes,
            cost.evidence,
            source_role="config_guide",
            source_version="7.9",
            is_target_version=False,
        )
        health = [
            ManualSourceHealth("target", "command_reference", "6.3.1", True, "complete"),
            ManualSourceHealth("other", "config_guide", "7.9", False, "complete"),
        ]
        with tempfile.TemporaryDirectory() as directory:
            harness = ConfProbeAuditHarness(
                [block for block in blocks if block.command_name != "cost"] + [other_cost],
                health,
                index_findings,
                object(),
                {"vendor": "Cisco", "version": "6.3.1", "scope": "router ospf"},
                Path(directory) / "discovered",
            )
            _, findings = harness.audit([probe_group("cost <1-65535>")])
            self.assertEqual("C1", findings[0].category)
            self.assertEqual("P00001", findings[0].probe_group_id)

            with (
                patch(
                    "audit_agent.search_vendor_site_impl",
                    return_value={"state": "not_found", "results": []},
                ),
                patch.object(ConfProbeAuditHarness, "_cisco_browser_for_search", return_value=None),
            ):
                c2_harness = ConfProbeAuditHarness(
                    [],
                    health[:1],
                    [],
                    object(),
                    {"vendor": "Cisco", "version": "6.3.1", "scope": "router ospf"},
                    Path(directory) / "discovered2",
                )
                _, c2_findings = c2_harness.audit([probe_group("unknown-command")])
        self.assertEqual("C2", c2_findings[0].category)

    def test_ambiguous_local_candidates_are_selected_by_agent(self):
        class SelectingNativeReviewer:
            def agent_turn(self, messages, tools):
                payload = json.loads(messages[1]["content"])
                category = payload["candidate_categories"][0]
                response = {
                    "category": category,
                    "conclusion": "confirmed",
                    "confidence": 0.9,
                    "rationale": "The OSPF candidate matches the supplied context.",
                }
                if category == "MATCH":
                    response["selected_block_ids"] = ["M1:B0001"]
                return {"content": json.dumps(response)}

        ospf_url = "https://example.invalid/ospf.html"
        isis_url = "https://example.invalid/isis.html"
        blocks = [
            ManualCommandBlock(
                "M1:B0001", "max-metric", "max-metric", ospf_url,
                "OSPF Command Reference", ("max-metric",), ("router",),
                (ManualEvidence("M1:B0001:syntax", "M1:B0001", "syntax", "max-metric", ospf_url),),
            ),
            ManualCommandBlock(
                "M2:B0001", "max-metric", "max-metric", isis_url,
                "IS-IS Command Reference", ("max-metric",), ("router",),
                (ManualEvidence("M2:B0001:syntax", "M2:B0001", "syntax", "max-metric", isis_url),),
            ),
        ]
        harness = ConfProbeAuditHarness(
            blocks,
            [ManualSourceHealth("local", "command_reference", "6.3.1", True, "complete")],
            [],
            SelectingNativeReviewer(),
            {"vendor": "Cisco", "version": "6.3.1", "scope": "router ospf"},
            Path("discovered"),
        )
        coverage, findings = harness.audit(
            [probe_group("max-metric", contexts=(("ospf",), ("isis",)))]
        )

        self.assertEqual("verified", coverage[0].status)
        self.assertFalse(findings)
        self.assertEqual(3, len(harness.trace))

    def test_c3_is_reviewed_by_native_agent(self):
        manual_url = "https://example.invalid/ospf-commands.html"
        block = ManualCommandBlock(
            "M1:B0001",
            "documented",
            "documented",
            manual_url,
            "OSPF Command Reference",
            ("documented enable",),
            ("router",),
            (
                ManualEvidence("M1:B0001:title", "M1:B0001", "title", "documented", manual_url),
                ManualEvidence("M1:B0001:description", "M1:B0001", "description", "OSPF documented command", manual_url),
                ManualEvidence("M1:B0001:syntax", "M1:B0001", "syntax", "documented enable", manual_url),
            ),
        )
        health = [ManualSourceHealth("local", "command_reference", "6.3.1", True, "complete")]
        with tempfile.TemporaryDirectory() as directory, patch(
            "audit_agent.search_vendor_site_impl",
            return_value={"state": "not_found", "results": []},
        ):
            harness = ConfProbeAuditHarness(
                [block],
                health,
                [],
                NativeReviewer(),
                {"vendor": "Cisco", "version": "6.3.1", "scope": "router ospf"},
                Path(directory),
            )
            _, findings = harness.audit([probe_group("unknown-command")])

        c3 = next(item for item in findings if item.category == "C3")
        self.assertEqual("confirmed", c3.status)

    def test_cli_reads_openai_compatible_configuration(self):
        with patch.dict(
            "os.environ",
            {
                "OPENAI_API_KEY": "test-key",
                "OPENAI_BASE_URL": "https://relay.example/v1",
                "OPENAI_MODEL": "test-model",
            },
            clear=False,
        ):
            from audit_agent import _parse_args

            request = _parse_args(
                [
                    "--probe",
                    "graphs/xrv9k/config/router_ospf/router_ospf_DSL.json",
                    "--version",
                    "6.3.1",
                ]
            )

        self.assertEqual("https://relay.example/v1", request.llm_base_url)
        self.assertEqual("test-model", request.llm_model)
        self.assertEqual(180.0, request.llm_timeout)
        self.assertEqual("Cisco", request.vendor)
        self.assertEqual("xrv9k", request.device_model)
        self.assertEqual("router ospf", request.scope)

    def test_cli_uses_configured_manual_library(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            "os.environ",
            {
                "OPENAI_API_KEY": "test-key",
                "OPENAI_BASE_URL": "https://relay.example/v1",
                "OPENAI_MODEL": "test-model",
            },
            clear=False,
        ):
            manifest = Path(directory) / "sources.json"
            manifest.write_text(
                json.dumps(
                    {
                        "vendor": "Cisco",
                        "platform": "IOS XR",
                        "version": "6.3.1",
                        "sources": [MANUAL_URL],
                    }
                ),
                encoding="utf-8",
            )
            from audit_agent import _parse_args

            request = _parse_args(
                [
                    "--probe",
                    "graphs/xrv9k/config/router_ospf/router_ospf_DSL.json",
                    "--manual-library",
                    str(manifest),
                    "--version",
                    "6.3.1",
                ]
            )

        self.assertEqual(str(manifest), request.manual_library)

    def test_openai_adapter_reviews_findings_with_json_schema(self):
        response = FakeHttpResponse(
            200, {"choices": [{"message": {"content": '{"reviews": []}'}}]}
        )
        client = FakeHttpClient([response])
        adapter = OpenAICompatibleAdapter(
            "test-key", "https://relay.example/v1", "test-model", client=client
        )

        result = adapter.review_findings([], {"version": "6.3.1"})

        self.assertEqual({"reviews": []}, result)
        endpoint, headers, request = client.calls[0]
        self.assertEqual("https://relay.example/v1/chat/completions", endpoint)
        self.assertEqual("Bearer test-key", headers["Authorization"])
        self.assertEqual("json_schema", request["response_format"]["type"])
        self.assertNotIn("commands", request["messages"][0]["content"].lower())

    def test_openai_adapter_keeps_json_fallbacks(self):
        client = FakeHttpClient(
            [
                FakeHttpResponse(400, {}, "response_format json_schema is unsupported"),
                FakeHttpResponse(400, {}, "json mode is unsupported"),
                FakeHttpResponse(
                    200,
                    {"choices": [{"message": {"content": '{"reviews": []}'}}]},
                ),
            ]
        )
        adapter = OpenAICompatibleAdapter(
            "test-key", "https://relay.example/v1", "test-model", client=client
        )

        result = adapter.review_findings([], {"version": "6.3.1"})

        self.assertEqual({"reviews": []}, result)
        self.assertEqual(
            [("json_schema", 400), ("json_object", 400), ("plain_json", 200)],
            [(item["mode"], item["status_code"]) for item in adapter.last_attempts],
        )
        self.assertEqual("json_object", client.calls[1][2]["response_format"]["type"])
        self.assertNotIn("response_format", client.calls[2][2])

    def test_openai_adapter_uses_native_tool_calls(self):
        client = FakeHttpClient(
            [
                FakeHttpResponse(
                    200,
                    {
                        "choices": [
                            {
                                "message": {
                                    "role": "assistant",
                                    "tool_calls": [
                                        {
                                            "id": "call_1",
                                            "function": {
                                                "name": "search_manual_library",
                                                "arguments": '{"query":"cost","scope":"target"}',
                                            },
                                        }
                                    ],
                                }
                            }
                        ]
                    },
                )
            ]
        )
        adapter = OpenAICompatibleAdapter(
            "test-key", "https://relay.example/v1", "test-model", client=client
        )

        response = adapter.agent_turn(
            [{"role": "user", "content": "audit cost"}],
            [{"type": "function", "function": {"name": "search_manual_library", "parameters": {}}}],
        )

        self.assertEqual("search_manual_library", response["tool_calls"][0]["function"]["name"])
        self.assertEqual("auto", client.calls[0][2]["tool_choice"])
        self.assertIn("tools", client.calls[0][2])

    def test_openai_adapter_marks_all_generic_400_attempts_unresolved(self):
        client = FakeHttpClient(
            [
                FakeHttpResponse(400, {}, "Request not allowed"),
                FakeHttpResponse(400, {}, "Request not allowed"),
                FakeHttpResponse(400, {}, "Request not allowed"),
            ]
        )
        adapter = OpenAICompatibleAdapter(
            "test-key", "https://relay.example/v1", "test-model", client=client
        )
        item = finding()

        logs = review_findings([item], adapter, {"version": "6.3.1"})

        self.assertEqual("unresolved", item.status)
        self.assertEqual("unresolved", logs[0]["status"])
        self.assertEqual(3, len(logs[0]["attempts"]))
        self.assertEqual(
            ["json_schema", "json_object", "plain_json"],
            [item["mode"] for item in logs[0]["attempts"]],
        )

    def test_load_probe_model_preserves_context_and_view_paths(self):
        records = load_probe_model(FIXTURES / "probe_DSL.json")
        groups = group_probe_commands(records)

        self.assertEqual(4, len(records))
        self.assertEqual("enter_view", records[0].kind)
        self.assertEqual(("[config-ospf]",), records[1].view_path)
        self.assertEqual(
            ("[config-ospf]", "[config-ospf-area]"), records[3].view_path
        )
        self.assertEqual({"global", "router", "area"}, {item.semantic_view for item in groups})

    def test_grouping_merges_equivalent_variant_order_and_contexts(self):
        variants = (
            "adjacency-sid absolute <1-10>",
            "adjacency-sid absolute <1-10> protected",
            "adjacency-sid absolute <1-10> neighbor-address <A.B.C.D>",
        )
        records = [
            CommandRecord(
                "probe:first",
                "adjacency-sid absolute <1-10> [protected|neighbor-address <A.B.C.D>]",
                context=("router ospf <WORD>",),
                view_path=("[config-ospf-if]",),
                variants=variants,
            ),
            CommandRecord(
                "probe:second",
                "adjacency-sid absolute <1-10> [neighbor-address <A.B.C.D>|protected]",
                context=("router ospf <WORD>", "interface <WORD>"),
                view_path=("[config-ospf]", "[config-ospf-if]"),
                variants=tuple(reversed(variants)),
            ),
        ]

        groups = group_probe_commands(records)

        self.assertEqual(1, len(groups))
        self.assertEqual("interface", groups[0].semantic_view)
        self.assertEqual(("interface",), groups[0].semantic_views)
        self.assertEqual(("probe:first", "probe:second"), groups[0].record_ids)
        self.assertEqual(2, len(groups[0].contexts))
        self.assertEqual(2, len(groups[0].view_paths))

    def test_grouping_preserves_each_view_and_b2_checks_them_individually(self):
        records = [
            CommandRecord(
                "probe:router",
                "cost <1-65535>",
                view_path=("[config-ospf]",),
            ),
            CommandRecord(
                "probe:vrf",
                "cost <1-65535>",
                view_path=("[config-ospf-vrf]",),
            ),
        ]
        groups = group_probe_commands(records)
        blocks, index_findings = self.index()
        cost = next(block for block in blocks if block.command_name == "cost")
        cost.modes = ("router",)

        _, findings = audit_probe_commands(groups, [cost], index_findings)
        view_findings = [item for item in findings if item.category == "B2"]

        self.assertEqual(1, len(groups))
        self.assertEqual("mixed", groups[0].semantic_view)
        self.assertEqual(("router", "vrf"), groups[0].semantic_views)
        self.assertEqual(["vrf"], [item.semantic_view for item in view_findings])

    def test_manual_search_uses_probe_context_and_reports_ambiguity(self):
        ospf_url = "https://example.invalid/ospf-commands.html"
        isis_url = "https://example.invalid/isis-commands.html"
        blocks = [
            ManualCommandBlock(
                "M1:B0001",
                "max-metric",
                "max-metric",
                ospf_url,
                "OSPF Command Reference",
                ("max-metric router-lsa",),
                ("router",),
                (ManualEvidence("M1:B0001:title", "M1:B0001", "title", "OSPF max-metric", ospf_url),),
            ),
            ManualCommandBlock(
                "M2:B0001",
                "max-metric",
                "max-metric",
                isis_url,
                "IS-IS Command Reference",
                ("max-metric on-startup",),
                ("router",),
                (ManualEvidence("M2:B0001:title", "M2:B0001", "title", "IS-IS max-metric", isis_url),),
            ),
        ]
        health = [ManualSourceHealth("local", "command_reference", "6.3.1", True, "complete")]

        result = search_manual_library_impl(
            "max-metric router-lsa",
            blocks,
            health,
            contexts=(("router ospf <WORD>",),),
            variants=("max-metric router-lsa",),
        )
        ambiguous = search_manual_library_impl(
            "max-metric",
            blocks,
            health,
            contexts=(("ospf",), ("isis",)),
            variants=("max-metric router-lsa", "max-metric on-startup"),
        )
        missing = search_manual_library_impl(
            "unknown-command",
            blocks,
            health,
            contexts=(("router ospf <WORD>",),),
        )

        self.assertEqual("hit", result["state"])
        self.assertEqual(["M1:B0001"], [item["block_id"] for item in result["results"]])
        self.assertEqual("ambiguous", ambiguous["state"])
        self.assertEqual("miss_complete", missing["state"])

    def test_set_difference_uses_full_branches_and_numeric_containment(self):
        url = "https://example.invalid/cost.html"
        evidence = (ManualEvidence("M1:B1:syntax", "M1:B1", "syntax", "cost <0-65535>", url),)
        covering = ManualCommandBlock(
            "M1:B1", "cost", "cost", url, "OSPF Command Reference",
            ("cost <0-65535>",), ("router",), evidence,
        )
        partial = ManualCommandBlock(
            "M1:B2", "cost", "cost", url, "OSPF Command Reference",
            ("cost <1-5>",), ("router",), evidence,
        )
        group = probe_group("cost <1-10>")

        _, covered_findings = audit_probe_commands([group], [covering])
        _, partial_findings = audit_probe_commands([group], [partial])

        self.assertFalse(any(item.category == "B1" for item in covered_findings))
        self.assertEqual(["B1"], [item.category for item in partial_findings])

    def test_set_difference_combines_all_intersecting_manual_blocks(self):
        url = "https://example.invalid/mode.html"
        first = ManualCommandBlock(
            "M1:B1", "mode", "mode", url, "OSPF Command Reference",
            ("mode one",), ("router",),
            (ManualEvidence("M1:B1:syntax", "M1:B1", "syntax", "mode one", url),),
        )
        second = ManualCommandBlock(
            "M2:B1", "mode", "mode", url + "?page=2", "OSPF Command Reference",
            ("mode two",), ("router",),
            (ManualEvidence("M2:B1:syntax", "M2:B1", "syntax", "mode two", url),),
        )
        group = probe_group("mode {one|two}")

        _, findings = audit_probe_commands([group], [first, second])

        self.assertFalse(any(item.category == "B1" for item in findings))

    def test_manual_only_branches_produce_branch_c3_not_c2(self):
        url = "https://example.invalid/mode.html"
        block = ManualCommandBlock(
            "M1:B1", "mode", "mode", url, "OSPF Command Reference",
            ("mode {one|two}",), ("router",),
            (ManualEvidence("M1:B1:syntax", "M1:B1", "syntax", "mode {one|two}", url),),
        )

        findings = audit_manual_overcoverage(
            [probe_group("mode one")], [block], scope=""
        )

        self.assertEqual(["C3"], [item.category for item in findings])
        self.assertEqual("Branch Overcoverage", findings[0].name)
        self.assertIn("mode two", findings[0].reason)

    def test_ai_recovered_syntax_requires_manual_review(self):
        class RecoveryReviewer:
            def recover_manual_syntax(self, block):
                return {
                    "recovered_syntax_templates": ["broken { enable | disable }"],
                    "evidence_ids": ["M1:B1:syntax"],
                    "confidence": 0.91,
                    "rationale": "The source contains both alternatives and only misses the closing brace.",
                }

            def agent_turn(self, messages, tools):
                category = json.loads(messages[1]["content"])["candidate_categories"][0]
                return {
                    "content": json.dumps(
                        {
                            "category": category,
                            "conclusion": "confirmed",
                            "confidence": 0.95,
                            "rationale": "The recovered branch is supported by the cited source.",
                        }
                    )
                }

        url = "https://example.invalid/broken.html"
        block = ManualCommandBlock(
            "M1:B1", "broken", "broken", url, "OSPF Command Reference",
            ("broken { enable | disable",), ("router",),
            (
                ManualEvidence("M1:B1:title", "M1:B1", "title", "broken", url),
                ManualEvidence("M1:B1:syntax", "M1:B1", "syntax", "broken { enable | disable", url),
            ),
        )
        index_finding = AuditFinding(
            "", "A1", "Syntax Error", "Invalid syntax.",
            manual_block_ids=(block.block_id,), manual_commands=(block.title,),
            evidence=(block.evidence[1],),
        )
        with tempfile.TemporaryDirectory() as directory:
            log_path = Path(directory) / "agent_tool.log"
            harness = ConfProbeAuditHarness(
                [block],
                [ManualSourceHealth("local", "command_reference", "6.3.1", True, "complete")],
                [index_finding],
                RecoveryReviewer(),
                {"vendor": "Cisco", "version": "6.3.1", "scope": "router ospf"},
                Path(directory) / "discovered",
                tool_log_path=log_path,
            )
            recoveries = harness.recover_invalid_syntax()
            _, findings = harness.audit([probe_group("broken enable")])
            log = log_path.read_text(encoding="utf-8")
            c3 = next(item for item in findings if item.category == "C3")
            _, markdown_path = render_report(
                {"version": "6.3.1"}, [], [c3], directory
            )
            markdown = markdown_path.read_text(encoding="utf-8")

        self.assertEqual("recovered", recoveries[0]["state"])
        self.assertEqual("ai_recovered", harness.blocks[0].syntax_provenance)
        self.assertTrue(c3.requires_manual_review)
        self.assertEqual("unresolved", c3.status)
        self.assertIn("recover_invalid_syntax | recovered", log)
        self.assertIn("Syntax provenance: ai_recovered", markdown)
        self.assertIn("Manual review: required", markdown)

    def test_low_confidence_syntax_recovery_is_rejected(self):
        class LowConfidenceRecovery:
            def recover_manual_syntax(self, block):
                return {
                    "recovered_syntax_templates": ["broken { enable | disable }"],
                    "evidence_ids": ["M1:B1:syntax"],
                    "confidence": 0.84,
                    "rationale": "Low confidence recovery.",
                }

        url = "https://example.invalid/broken.html"
        block = ManualCommandBlock(
            "M1:B1", "broken", "broken", url, "OSPF Command Reference",
            ("broken { enable | disable",), ("router",),
            (ManualEvidence("M1:B1:syntax", "M1:B1", "syntax", "broken { enable | disable", url),),
        )
        harness = ConfProbeAuditHarness(
            [block], [], [], LowConfidenceRecovery(),
            {"vendor": "Cisco", "version": "6.3.1", "scope": "router ospf"},
            Path("discovered"),
        )

        recoveries = harness.recover_invalid_syntax()

        self.assertEqual("rejected", recoveries[0]["state"])
        self.assertEqual("manual", harness.blocks[0].syntax_provenance)

    def test_manual_search_reports_incomplete_sources(self):
        result = search_manual_library_impl(
            "missing-command",
            [],
            [ManualSourceHealth("local", "command_reference", "6.3.1", True, "incomplete")],
        )

        self.assertEqual("incomplete", result["state"])

    def test_cisco_vendor_search_retries_timeout_once(self):
        class FailingPlaywright:
            chromium = types.SimpleNamespace(
                launch=lambda **kwargs: (_ for _ in ()).throw(TimeoutError("timed out"))
            )

            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

        package = types.ModuleType("playwright")
        module = types.ModuleType("playwright.sync_api")
        module.sync_playwright = FailingPlaywright
        package.sync_api = module
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            sys.modules,
            {"playwright": package, "playwright.sync_api": module},
        ):
            result = search_vendor_site_impl("Cisco", "router ospf missing", directory)

        self.assertEqual("failed", result["state"])
        self.assertEqual(2, len(result["attempts"]))
        self.assertTrue(all(item["state"] == "failed" for item in result["attempts"]))

    def test_cisco_search_url_supplies_the_query_parameter(self):
        url = _cisco_search_url("router ospf")

        self.assertEqual(1, url.count("?"))
        self.assertIn("query=router+ospf", url)
        self.assertNotIn("?q=", url)

    def test_cisco_ai_response_parser_waits_for_complete_answer(self):
        generating = _parse_cisco_ai_response(
            "All Results AI Response Visit FAQ Important. Results generated by AI. "
            "Before using results, verify accuracy and completeness. Generating... Refine results"
        )
        complete = _parse_cisco_ai_response(
            "All Results AI Response Visit FAQ Important. Results generated by AI. "
            "Before using results, verify accuracy and completeness. Cisco IOS XR Release "
            "7.9 documents ospf affinity-map bit-position. Refine results Sorted by: relevancy"
        )

        self.assertEqual("generating", generating["state"])
        self.assertEqual("complete", complete["state"])
        self.assertIn("affinity-map bit-position", complete["text"])
        self.assertEqual(["7.9"], complete["version_hints"])

    def test_ai_response_timeout_does_not_support_not_found(self):
        class EmptyLocator:
            def all(self):
                return []

        class EmptyPage:
            url = "https://search.cisco.com/search?query=ospf"

            def locator(self, selector):
                return EmptyLocator()

            def close(self):
                pass

        class EmptyBrowser:
            def new_page(self):
                return EmptyPage()

        with (
            patch("utils.audit_tools._open_cisco_search", return_value="search_url"),
            patch(
                "utils.audit_tools._wait_for_cisco_ai_response",
                return_value={"state": "timeout", "text": "", "version_hints": []},
            ),
        ):
            state, _, _, _, _, _ = _search_cisco_with_browser(
                EmptyBrowser(), "router ospf missing", "ospf missing"
            )

        self.assertEqual("incomplete", state)

    def test_vendor_search_uses_representative_command_suffix(self):
        phrase = _vendor_search_phrase(
            "router ospf <WORD> segment-routing mpls sr-prefer tunnel-policy <WORD> "
            "metric-type type-1",
            (("router ospf <WORD>",),),
        )

        self.assertEqual(
            "ospf sr-prefer tunnel-policy metric-type type-1",
            phrase,
        )
        self.assertNotIn("segment-routing", phrase)

    def test_tool3_verifies_other_version_source_after_ai_discovery(self):
        class FakeAnchor:
            def inner_text(self):
                return "OSPF affinity-map bit-position commands, IOS XR Release 7.9"

            def get_attribute(self, name):
                return (
                    "https://www.cisco.com/c/en/us/td/docs/routers/asr9000/"
                    "asr9k-r7-9/ospf-affinity-map.html"
                    if name == "href"
                    else None
                )

        class FakeLocator:
            def __init__(self, *, text="", anchors=()):
                self.text = text
                self.anchors = anchors

            def all(self):
                return list(self.anchors)

            def inner_text(self):
                return self.text

        class FakePage:
            def __init__(self, *, url, text="", anchors=()):
                self.url = url
                self.text = text
                self.anchors = anchors

            def locator(self, selector):
                if selector == "a[href]":
                    return FakeLocator(anchors=self.anchors)
                return FakeLocator(text=self.text)

            def goto(self, url, **kwargs):
                self.url = url

            def close(self):
                pass

        class FakeBrowser:
            def __init__(self):
                self.pages = [
                    FakePage(
                        url="https://search.cisco.com/search?query=ospf",
                        anchors=(FakeAnchor(),),
                    ),
                    FakePage(
                        url="",
                        text=(
                            "Cisco IOS XR Release 7.9 OSPF Command Reference. "
                            "Configure ospf affinity-map bit-position in router mode."
                        ),
                    ),
                ]

            def new_page(self):
                return self.pages.pop(0)

        ai_response = {
            "state": "complete",
            "text": "IOS XR Release 7.9 documents ospf affinity-map bit-position.",
            "version_hints": ["7.9"],
            "message": "Cisco AI Response completed.",
        }
        with tempfile.TemporaryDirectory() as directory:
            harness = ConfProbeAuditHarness(
                [],
                [ManualSourceHealth("target", "command_reference", "7.7.1", True, "complete")],
                [],
                object(),
                {"vendor": "Cisco", "version": "7.7.1", "scope": "router ospf"},
                Path(directory) / "discovered",
            )
            with (
                patch.object(harness, "_cisco_browser_for_search", return_value=FakeBrowser()),
                patch("utils.audit_tools._open_cisco_search", return_value="search_url"),
                patch("utils.audit_tools._wait_for_cisco_ai_response", return_value=ai_response),
            ):
                _, findings = harness.audit(
                    [probe_group("router ospf <WORD> affinity-map <WORD> bit-position <0-255>")]
                )

        self.assertEqual("C1", findings[0].category)
        self.assertIn("version 7.9", findings[0].reason)
        self.assertTrue(any("Version: 7.9" in item.text for item in findings[0].evidence))

    def test_vendor_version_detection_uses_release_context(self):
        self.assertEqual("7.8", _extract_version_hint("/asr9k-r7-8/ospf.html"))
        self.assertEqual("7.9", _extract_version_hint("/b-routing-cg-asr9000-79x.html"))
        self.assertEqual("", _vendor_result_version({"results": [{"version": "7.7"}]}, "7.7.1"))

    def test_vendor_search_cache_collapses_parameter_only_variants(self):
        with tempfile.TemporaryDirectory() as directory:
            harness = ConfProbeAuditHarness(
                [],
                [],
                [],
                object(),
                {"vendor": "Cisco", "version": "6.3.1", "scope": "router ospf"},
                Path(directory) / "discovered",
            )
            result = {
                "state": "not_found",
                "query": "cost <1-10>",
                "results": [],
                "attempts": [],
            }
            with (
                patch.object(harness, "_cisco_browser_for_search", return_value=None),
                patch("audit_agent.search_vendor_site_impl", return_value=result) as search,
            ):
                first = harness._dispatch_tool("search_vendor_site", {"query": "cost <1-10>"})
                second = harness._dispatch_tool("search_vendor_site", {"query": "cost <1-65535>"})

        self.assertEqual("not_found", first["state"])
        self.assertTrue(second["cached"])
        self.assertEqual(1, search.call_count)

    def test_vendor_browser_failure_disables_remaining_run_searches(self):
        with tempfile.TemporaryDirectory() as directory:
            harness = ConfProbeAuditHarness(
                [],
                [],
                [],
                object(),
                {"vendor": "Cisco", "version": "7.7.1", "scope": "router ospf"},
                Path(directory) / "discovered",
            )
            failed = {
                "state": "failed",
                "results": [],
                "attempts": [
                    {
                        "attempt": 1,
                        "state": "failed",
                        "error": "TimeoutError: Locator.fill: Timeout 30000ms exceeded.",
                    }
                ],
            }
            with (
                patch.object(harness, "_cisco_browser_for_search", return_value=object()),
                patch("audit_agent.search_vendor_site_impl", return_value=failed) as search,
            ):
                first = harness._dispatch_tool("search_vendor_site", {"query": "cost <1-10>"})
                second = harness._dispatch_tool("search_vendor_site", {"query": "priority <1-255>"})

        self.assertEqual("failed", first["state"])
        self.assertEqual("failed", second["state"])
        self.assertIn("unavailable for this audit run", second["message"])
        self.assertEqual(1, search.call_count)

    def test_agent_tool_schema_accepts_command_contexts(self):
        search_tool = next(
            item for item in AGENT_TOOLS if item["function"]["name"] == "search_manual_library"
        )
        vendor_tool = next(
            item for item in AGENT_TOOLS if item["function"]["name"] == "search_vendor_site"
        )
        self.assertIn("contexts", search_tool["function"]["parameters"]["properties"])
        self.assertIn("variants", search_tool["function"]["parameters"]["properties"])
        self.assertTrue(
            {"contexts", "platform", "version"}
            <= set(vendor_tool["function"]["parameters"]["properties"])
        )

    def test_vendor_search_phrase_uses_command_context_not_web_search_syntax(self):
        phrase = _vendor_search_phrase(
            'site:cisco.com ASR 9000 "adjacency-sid" <WORD>',
            (("router ospf <WORD>",),),
        )
        self.assertIn("ospf", phrase)
        self.assertIn("adjacency-sid", phrase)
        self.assertNotIn("site:cisco.com", phrase)

    def test_vendor_result_matching_excludes_single_token_navigation_links(self):
        query = "router ospf max-metric router-lsa"
        self.assertFalse(_search_result_matches(query, "Cisco OSPF overview"))
        self.assertTrue(_search_result_matches(query, "OSPF max-metric command"))

    def test_agent_prompt_loads_split_skills(self):
        audit_prompt = _agent_system_prompt(False)
        vendor_prompt = _agent_system_prompt(True)

        self.assertIn("Manual Audit Skill", audit_prompt)
        self.assertIn("For A1", audit_prompt)
        self.assertNotIn("Vendor Search Skill", audit_prompt)
        self.assertIn("Manual Audit Skill", vendor_prompt)
        self.assertIn("Vendor Search Skill", vendor_prompt)

    def test_vendor_search_skill_selection_uses_category_or_search_facts(self):
        a1 = AuditFinding("F00001", "A1", "Syntax Error", "Invalid syntax.")
        c1 = AuditFinding("F00002", "C1", "Version Ambiguity", "Other version match.")

        self.assertFalse(_needs_vendor_search_skill([a1], {}))
        self.assertTrue(_needs_vendor_search_skill([c1], {}))
        self.assertTrue(
            _needs_vendor_search_skill([a1], {"search_phrase": "ospf cost"})
        )

    def test_agent_final_review_receives_tools_for_autonomous_follow_up(self):
        class FinalReviewer:
            def __init__(self):
                self.tools = None

            def agent_turn(self, messages, tools):
                self.tools = list(tools)
                return {
                    "content": json.dumps(
                        {
                            "category": "A1",
                            "conclusion": "confirmed",
                            "confidence": 0.9,
                            "rationale": "The formal syntax is structurally invalid.",
                        }
                    )
                }

        reviewer = FinalReviewer()
        finding = AuditFinding("F00001", "A1", "Syntax Error", "Invalid syntax.")
        harness = ConfProbeAuditHarness(
            [],
            [],
            [],
            reviewer,
            {"vendor": "Cisco", "version": "7.7.1", "scope": "router ospf"},
            Path("discovered"),
        )

        harness._agent_review(probe_group("authentication"), [finding], {"syntax_diffs": []})

        self.assertEqual(AGENT_TOOLS, reviewer.tools)
        self.assertEqual("confirmed", finding.status)

    def test_agent_receives_candidate_evidence_for_a3(self):
        class CapturingNativeReviewer:
            def __init__(self):
                self.payload = None

            def agent_turn(self, messages, tools):
                self.payload = json.loads(messages[1]["content"])
                return {
                    "content": json.dumps(
                        {
                            "category": "A3",
                            "conclusion": "confirmed",
                            "confidence": 0.9,
                            "rationale": "The paired syntax evidence conflicts.",
                        }
                    )
                }

        reviewer = CapturingNativeReviewer()
        evidence = (
            ManualEvidence("M1:B0001:syntax", "M1:B0001", "syntax", "cost <1-10>", MANUAL_URL),
            ManualEvidence("M2:B0001:syntax", "M2:B0001", "syntax", "cost <1-20>", "https://example.invalid/ospf-guide.html"),
        )
        candidate = AuditFinding(
            "F00001",
            "A3",
            "Macro Conflict",
            "Different syntax ranges.",
            evidence=evidence,
        )
        harness = ConfProbeAuditHarness(
            [],
            [],
            [],
            reviewer,
            {"vendor": "Cisco", "version": "6.3.1", "scope": "router ospf"},
            Path("discovered"),
        )
        harness._agent_review(probe_group("cost <1-10>"), [candidate])

        supplied = reviewer.payload["candidate_findings"][0]["evidence"]
        self.assertEqual({item.evidence_id for item in evidence}, {item["evidence_id"] for item in supplied})
        self.assertEqual("confirmed", candidate.status)

    def test_agent_cannot_confirm_deterministic_unresolved_candidate(self):
        class OverconfidentNativeReviewer:
            def agent_turn(self, messages, tools):
                return {
                    "content": json.dumps(
                        {
                            "category": "UNRESOLVED",
                            "conclusion": "confirmed",
                            "confidence": 0.9,
                            "rationale": "This should be rejected.",
                        }
                    )
                }

        candidate = AuditFinding(
            "F00001",
            "UNRESOLVED",
            "Comparison Incomplete",
            "The deterministic comparison exceeded its limit.",
        )
        harness = ConfProbeAuditHarness(
            [],
            [],
            [],
            OverconfidentNativeReviewer(),
            {"vendor": "Cisco", "version": "6.3.1", "scope": "router ospf"},
            Path("discovered"),
        )
        harness._agent_review(probe_group("complex"), [candidate])
        self.assertEqual("unresolved", candidate.status)

    def test_complex_template_comparison_is_unresolved_not_b1(self):
        branches = " ".join("{one|two|three}" for _ in range(6))
        template = f"complex {branches}"
        url = "https://example.invalid/complex.html"
        block = ManualCommandBlock(
            "M1:B0001",
            "complex",
            "complex",
            url,
            "OSPF Command Reference",
            (template,),
            ("router",),
            (ManualEvidence("M1:B0001:syntax", "M1:B0001", "syntax", template, url),),
        )
        _, findings = audit_probe_commands([probe_group(template)], [block])
        self.assertEqual(["UNRESOLVED"], [item.category for item in findings])

    def test_a3_is_scoped_and_b3_requires_body_or_example_evidence(self):
        def block(block_id, url, document_title, syntax, text):
            return ManualCommandBlock(
                block_id,
                "max-metric",
                "max-metric",
                url,
                document_title,
                (syntax,),
                ("router",),
                (
                    ManualEvidence(f"{block_id}:title", block_id, "title", "max-metric", url),
                    ManualEvidence(f"{block_id}:description", block_id, "description", text, url),
                ),
            )

        ospf = block("M1:B0001", "https://example.invalid/ospf.html", "OSPF", "max-metric router-lsa", "OSPF max-metric")
        isis = block("M2:B0001", "https://example.invalid/isis.html", "IS-IS", "max-metric on-startup", "IS-IS max-metric")
        scoped = _macro_conflicts([ospf, isis], scope="router ospf")
        ospf_conflict = block("M3:B0001", "https://example.invalid/ospf-guide.html", "OSPF", "max-metric summary-lsa", "OSPF max-metric")
        self.assertFalse(scoped)
        self.assertEqual(1, len(_macro_conflicts([ospf, ospf_conflict], scope="router ospf")))

        ospf_area = block(
            "M3:B0002",
            "https://example.invalid/ospf-area.html",
            "OSPF Area Command Reference",
            "max-metric router-lsa",
            "OSPF area max-metric",
        )
        isis_area = block(
            "M3:B0003",
            "https://example.invalid/isis-area.html",
            "IS-IS Area Command Reference",
            "max-metric on-startup",
            "IS-IS area max-metric",
        )
        self.assertFalse(
            _macro_conflicts([ospf_area, isis_area], scope="router ospf area")
        )

        title_only = ManualCommandBlock(
            "M4:B0001",
            "legacy",
            "legacy",
            "https://example.invalid/legacy.html",
            "OSPF",
            (),
            ("router",),
            (ManualEvidence("M4:B0001:title", "M4:B0001", "title", "legacy", "https://example.invalid/legacy.html"),),
        )
        body_only = ManualCommandBlock(
            "M5:B0001",
            "legacy",
            "legacy",
            "https://example.invalid/legacy-guide.html",
            "OSPF",
            (),
            ("router",),
            (
                ManualEvidence("M5:B0001:title", "M5:B0001", "title", "legacy", "https://example.invalid/legacy-guide.html"),
                ManualEvidence("M5:B0001:description", "M5:B0001", "description", "Use the legacy command here.", "https://example.invalid/legacy-guide.html"),
            ),
        )
        _, title_findings = audit_probe_commands([probe_group("legacy")], [title_only])
        _, body_findings = audit_probe_commands([probe_group("legacy")], [body_only])
        self.assertNotIn("B3", {item.category for item in title_findings})
        self.assertIn("B3", {item.category for item in body_findings})

    def test_load_probe_model_skips_only_placeholder_terminal_leaves(self):
        records = load_probe_model(FIXTURES / "probe_with_value_leaf_DSL.json")
        groups = group_probe_commands(records)
        templates = {item.template for item in groups}
        blocks, index_findings = self.index()
        coverage, findings = audit_probe_commands(
            groups, blocks, index_findings, missing_search_complete=True
        )

        self.assertNotIn("<WORD>", templates)
        self.assertIn("authentication", templates)
        self.assertIn("passive", templates)
        self.assertFalse(any(item.template == "<WORD>" for item in coverage))
        self.assertFalse(
            any(
                item.category == "C2" and item.probe_template == "<WORD>"
                for item in findings
            )
        )

    def test_cisco_index_extracts_structured_evidence_without_llm(self):
        blocks, findings = self.index()
        cost = next(block for block in blocks if block.command_name == "cost")

        self.assertEqual(6, len(blocks))
        self.assertEqual(("cost <cost>",), cost.syntax_templates)
        self.assertEqual(("area",), cost.modes)
        self.assertTrue(
            {"title", "syntax", "parameter", "modes", "default", "usage", "example", "history"}
            <= {item.kind for item in cost.evidence}
        )
        self.assertIn("A1", {item.category for item in findings})
        self.assertIn("A2", {item.category for item in findings})

    def test_unsupported_manual_layout_fails_clearly(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manual.html"
            path.write_text("<html><h1>Not a command reference</h1></html>", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Unsupported Cisco manual layout"):
                build_manual_index([self.document(path)], target_version="6.3.1")

    def test_probe_rules_cover_verified_b1_b2_b3_and_c2(self):
        blocks, index_findings = self.index()
        groups = [
            probe_group("network point-to-point", group_id="P00001"),
            probe_group(
                "network {point-to-point|broadcast|non-broadcast}",
                group_id="P00002",
            ),
            probe_group("priority <1-255>", group_id="P00003"),
            probe_group("cost <1-65535>", view="interface", group_id="P00004"),
            probe_group("legacy enable", group_id="P00005"),
            probe_group("unknown-command", group_id="P00006"),
        ]

        coverage, findings = audit_probe_commands(
            groups, blocks, index_findings, missing_search_complete=True
        )
        by_group = {item.probe_group_id: item for item in coverage}
        categories = {
            group_id: {item.category for item in findings if item.probe_group_id == group_id}
            for group_id in by_group
        }

        self.assertEqual("verified", by_group["P00001"].status)
        self.assertEqual({"B1"}, categories["P00002"])
        self.assertEqual({"B1"}, categories["P00003"])
        self.assertIn("B2", categories["P00004"])
        self.assertIn("B3", categories["P00005"])
        self.assertEqual("undocumented", by_group["P00006"].status)
        self.assertEqual({"C2"}, categories["P00006"])
        self.assertNotIn("C3", {item.category for item in findings})

    def test_a1_and_a2_require_a_probe_anchor(self):
        blocks, index_findings = self.index()
        groups = [
            probe_group("broken enable", group_id="P00001"),
            probe_group("timer <1-20>", group_id="P00002"),
        ]

        _, findings = audit_probe_commands(groups, blocks, index_findings)

        self.assertEqual(1, sum(item.category == "A1" for item in findings))
        self.assertEqual(1, sum(item.category == "A2" for item in findings))
        anchored = [item for item in findings if item.category in {"A1", "A2"}]
        self.assertTrue(all(item.manual_commands for item in anchored))
        self.assertTrue(all(item.probe_template and item.probe_groups for item in anchored))
        self.assertTrue(
            all(item.probe_group_id == item.probe_groups[0].group_id for item in anchored)
        )
        with tempfile.TemporaryDirectory() as directory:
            report_path, markdown_path = render_report({}, [], findings, directory)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            markdown = markdown_path.read_text(encoding="utf-8")
        report_anchored = [
            item for item in report["findings"] if item["category"] in {"A1", "A2"}
        ]
        self.assertTrue(all(item["probe_groups"] for item in report_anchored))
        self.assertNotIn("Probe template: `N/A`", markdown)

    def test_harness_emits_each_index_finding_once_for_all_matching_groups(self):
        url = "https://example.invalid/ospf.html"
        block = ManualCommandBlock(
            "M1:B0001",
            "cost",
            "cost (OSPF)",
            url,
            "OSPF Command Reference",
            ("cost <1-10>",),
            ("router",),
            (ManualEvidence("M1:B0001:syntax", "M1:B0001", "syntax", "cost <1-10>", url),),
        )
        index_finding = AuditFinding(
            "F00001",
            "A2",
            "Micro Conflict",
            "Example conflict.",
            manual_block_ids=(block.block_id,),
            manual_commands=(block.title,),
            evidence=block.evidence,
        )
        groups = [
            probe_group("cost <1-10>", group_id="P00001", contexts=(("router ospf",),)),
            probe_group("cost <1-10>", group_id="P00002", contexts=(("router ospf",),)),
        ]
        harness = ConfProbeAuditHarness(
            [block],
            [ManualSourceHealth(url, "command_reference", "7.7.1", True, "complete")],
            [index_finding],
            object(),
            {"vendor": "Cisco", "version": "7.7.1", "scope": "router ospf"},
            Path("discovered"),
        )

        coverage, findings = harness.audit(groups)

        self.assertEqual(1, len(findings))
        self.assertEqual("A2", findings[0].category)
        self.assertEqual(["P00001", "P00002"], [item.group_id for item in findings[0].probe_groups])
        self.assertTrue(all(item.finding_ids == ("F00001",) for item in coverage))

    def test_protocol_filter_excludes_ospfv3_from_ospf_search_and_a3(self):
        ospf_url = "https://example.invalid/ospf.html"
        ospfv3_url = "https://example.invalid/ospfv3.html"
        ospf = ManualCommandBlock(
            "M1:B0001", "maximum interfaces", "maximum interfaces (OSPF)", ospf_url,
            "OSPF Command Reference", ("maximum interfaces <number>",), ("router",),
            (ManualEvidence("M1:B0001:syntax", "M1:B0001", "syntax", "maximum interfaces <number>", ospf_url),),
        )
        ospfv3 = ManualCommandBlock(
            "M2:B0001", "maximum interfaces", "maximum interfaces (OSPFv3)", ospfv3_url,
            "OSPFv3 Command Reference", ("maximum interfaces <number> [strict]",), ("router",),
            (ManualEvidence("M2:B0001:syntax", "M2:B0001", "syntax", "maximum interfaces <number> [strict]", ospfv3_url),),
        )
        health = [ManualSourceHealth(ospf_url, "command_reference", "7.7.1", True, "complete")]

        result = search_manual_library_impl(
            "maximum interfaces <1-10>",
            [ospf, ospfv3],
            health,
            scope="target",
            contexts=(("router ospf",),),
        )

        self.assertEqual([ospf.block_id], [item["block_id"] for item in result["results"]])
        self.assertFalse(_macro_conflicts([ospf, ospfv3], scope="router ospf"))

    def test_multiple_ranges_in_one_parameter_description_are_not_a2(self):
        url = "https://example.invalid/ospf.html"
        block = ManualCommandBlock(
            "M1:B0001",
            "redistribute",
            "redistribute (OSPF)",
            url,
            "OSPF Command Reference",
            ("redistribute bgp <process-id>",),
            ("router",),
            (
                ManualEvidence("M1:B0001:syntax", "M1:B0001", "syntax", "redistribute bgp <process-id>", url),
                ManualEvidence(
                    "M1:B0001:parameter",
                    "M1:B0001",
                    "parameter",
                    "process-id | For BGP, ranges are 1 to 65535 and 1 to 4294967295.",
                    url,
                ),
            ),
        )

        self.assertEqual("", _micro_conflict_reason(block))

    def test_unknown_probe_view_is_unresolved_not_b2(self):
        url = "https://example.invalid/ospf.html"
        block = ManualCommandBlock(
            "M1:B0001", "cost", "cost (OSPF)", url, "OSPF Command Reference",
            ("cost <1-10>",), ("router",),
            (ManualEvidence("M1:B0001:syntax", "M1:B0001", "syntax", "cost <1-10>", url),),
        )
        group = probe_group("cost <1-10>", view="unknown")

        _, findings = audit_probe_commands([group], [block])

        self.assertEqual(["UNRESOLVED"], [item.category for item in findings])

    def test_report_displays_category_probe_group_and_unreviewed_confidence(self):
        item = finding()
        item.status = "unresolved"
        item.rationale = "Agent exceeded the bounded tool-call budget."
        with tempfile.TemporaryDirectory() as directory:
            _, markdown_path = render_report({}, [], [item], directory)
            markdown = markdown_path.read_text(encoding="utf-8")

        self.assertIn("- Category: B1", markdown)
        self.assertIn("- Probe groups: P00001:", markdown)
        self.assertIn("- Confidence: N/A (not reviewed)", markdown)

    def test_a3_uses_target_version_blocks_without_page_level_c1(self):
        html = (FIXTURES / "manual.html").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as directory:
            second = Path(directory) / "manual2.html"
            second.write_text(
                html.replace("cost <var>cost</var>", "cost <var>cost</var> [strict]"),
                encoding="utf-8",
            )
            ambiguous = Path(directory) / "ambiguous.html"
            ambiguous.write_text(html.replace("6.3.1", "7.0.0"), encoding="utf-8")
            blocks, index_findings = build_manual_index(
                [
                    self.document(),
                    ManualDocument(MANUAL_URL + "?v=2", MANUAL_URL + "?v=2", "IOS XR 6.3.1", "", str(second)),
                    ManualDocument(MANUAL_URL + "?v=3", MANUAL_URL + "?v=3", "IOS XR 7.0.0", "", str(ambiguous)),
                ],
                target_version="6.3.1",
            )

        _, findings = audit_probe_commands(
            [probe_group("cost <1-65535>")], blocks, index_findings
        )
        categories = [item.category for item in findings]
        self.assertIn("A3", categories)
        self.assertNotIn("C1", categories)

    def test_review_validates_evidence_confidence_and_failures(self):
        confirmed = finding("F00001")
        review_findings([confirmed], FakeReviewer(), {"version": "6.3.1"})
        self.assertEqual("confirmed", confirmed.status)
        self.assertEqual(0.92, confirmed.confidence)

        invalid = finding("F00002")
        review_findings([invalid], InvalidEvidenceReviewer(), {"version": "6.3.1"})
        self.assertEqual("unresolved", invalid.status)
        self.assertIn("not supplied", invalid.rationale)

        low_confidence = finding("F00003")
        review_findings(
            [low_confidence], FakeReviewer(confidence=0.4), {"version": "6.3.1"}
        )
        self.assertEqual("unresolved", low_confidence.status)

        failed = finding("F00004")
        logs = review_findings([failed], FailingReviewer(), {"version": "6.3.1"})
        self.assertEqual("unresolved", failed.status)
        self.assertEqual("unresolved", logs[0]["status"])

        malformed = finding("F00005")
        review_findings(
            [malformed], MalformedReviewer(), {"version": "6.3.1"}
        )
        self.assertEqual("unresolved", malformed.status)

    def test_review_rejects_evidence_excluded_from_request_payload(self):
        item = finding("F00006")
        item.category = "A1"
        item.evidence = item.evidence + (
            ManualEvidence(
                evidence_id="M1:B0001:example:1",
                block_id="M1:B0001",
                kind="example",
                text="cost 65",
                url=MANUAL_URL,
            ),
        )

        class ExcludedEvidenceReviewer:
            def review_findings(self, candidates, audit_context):
                return {
                    "reviews": [
                        {
                            "finding_id": candidates[0]["finding_id"],
                            "conclusion": "confirmed",
                            "evidence_ids": ["M1:B0001:example:1"],
                            "confidence": 0.99,
                            "rationale": "This evidence was not included in the request.",
                        }
                    ]
                }

        review_findings([item], ExcludedEvidenceReviewer(), {"version": "6.3.1"})

        self.assertEqual("unresolved", item.status)
        self.assertIn("not supplied", item.rationale)

    def test_review_batches_truncate_evidence_without_changing_citation_ids(self):
        first = finding("F00001")
        second = finding("F00002")
        for item in (first, second):
            item.evidence = (
                ManualEvidence(
                    evidence_id=f"{item.finding_id}:syntax",
                    block_id="M1:B0001",
                    kind="syntax",
                    text="x" * 2_000,
                    url=MANUAL_URL,
                ),
            )
        reviewer = FakeReviewer()

        logs = review_findings(
            [first, second],
            reviewer,
            {"version": "6.3.1"},
            batch_size=8,
            max_batch_chars=1_800,
        )

        self.assertEqual(2, len(reviewer.calls))
        self.assertEqual(2, len(logs))
        for candidates, _ in reviewer.calls:
            evidence = candidates[0]["evidence"][0]
            self.assertLessEqual(len(evidence["text"]), 1_200)
            self.assertTrue(evidence["truncated"])
            self.assertTrue(evidence["evidence_id"].endswith(":syntax"))

    def test_report_contains_probe_manual_evidence_and_review(self):
        item = finding()
        item.status = "confirmed"
        item.llm_conclusion = "confirmed"
        item.confidence = 0.91
        item.rationale = "Confirmed by cited syntax."
        coverage = []
        with tempfile.TemporaryDirectory() as directory:
            json_path, markdown_path = render_report(
                {"version": "6.3.1"}, coverage, [item], directory
            )
            report = json.loads(json_path.read_text(encoding="utf-8"))
            markdown = markdown_path.read_text(encoding="utf-8")

        self.assertEqual("cost <1-65535>", report["findings"][0]["probe_template"])
        self.assertEqual(MANUAL_URL, report["findings"][0]["evidence"][0]["url"])
        self.assertIn("M1:B0001:syntax:1", markdown)
        self.assertIn("0.91", markdown)

    def test_report_includes_incomplete_manual_source_details(self):
        source_health = ManualSourceHealth(
            "https://example.invalid/book.html",
            "command_reference",
            "6.3.1",
            True,
            "incomplete",
            discovered_topics=5,
            indexed_topics=3,
            message="Two topics could not be parsed",
            retry_count=2,
            failed_urls=("https://example.invalid/book/failure.html",),
            unparsed_urls=("https://example.invalid/book/layout.html",),
        )
        with tempfile.TemporaryDirectory() as directory:
            json_path, markdown_path = render_report(
                {"version": "6.3.1"},
                [],
                [],
                directory,
                source_health=[source_health],
            )
            report = json.loads(json_path.read_text(encoding="utf-8"))
            markdown = markdown_path.read_text(encoding="utf-8")

        self.assertEqual("incomplete", report["manual_source_health"][0]["status"])
        self.assertIn("Incomplete Manual Sources", markdown)
        self.assertIn("failure.html", markdown)

    def test_tool_log_is_appended_when_a_tool_returns(self):
        with tempfile.TemporaryDirectory() as directory:
            log_path = Path(directory) / "agent_tool.log"
            harness = ConfProbeAuditHarness(
                [],
                [ManualSourceHealth("local", "command_reference", "6.3.1", True, "complete")],
                [],
                object(),
                {"vendor": "Cisco", "version": "6.3.1", "scope": "router ospf"},
                Path(directory) / "discovered",
                tool_log_path=log_path,
            )
            harness._dispatch_tool(
                "search_manual_library",
                {"query": "missing-command", "scope": "target"},
            )
            tool_log = log_path.read_text(encoding="utf-8")

        self.assertIn("| search_manual_library | miss_complete |", tool_log)

    def test_agent_review_is_appended_to_the_tool_log(self):
        rationale = (
            "The supplied syntax covers the command and the parameter range matches the "
            "observed Probe variant. No additional manual inconsistency is present."
        )

        class NativeLogReviewer:
            def agent_turn(self, messages, tools):
                return {
                    "content": json.dumps(
                        {
                            "category": "MATCH",
                            "conclusion": "confirmed",
                            "confidence": 0.91,
                            "rationale": rationale,
                        }
                    )
                }

        with tempfile.TemporaryDirectory() as directory:
            log_path = Path(directory) / "agent_tool.log"
            harness = ConfProbeAuditHarness(
                [],
                [],
                [],
                NativeLogReviewer(),
                {"vendor": "Cisco", "version": "6.3.1", "scope": "router ospf"},
                Path(directory) / "discovered",
                tool_log_path=log_path,
            )
            finding = AuditFinding("F00001", "MATCH", "Manual Match", "Syntax matches.")
            harness._agent_review(probe_group("router ospf <WORD>"), [finding], {"syntax": "match"})
            tool_log = log_path.read_text(encoding="utf-8")

        self.assertIn("| agent_review | final |", tool_log)
        self.assertIn("candidates=MATCH", tool_log)
        self.assertIn("conclusion=confirmed", tool_log)
        self.assertIn("Rationale: The supplied syntax covers the command", tool_log)
        self.assertIn(rationale, " ".join(tool_log.split()))

    def test_workflow_persists_recovery_stage_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            output_root = Path(directory) / "runs"

            def fake_fetch(urls, output_dir, **kwargs):
                manual_dir = Path(output_dir)
                manual_dir.mkdir(parents=True)
                html_path = manual_dir / "manual_001.html"
                html_path.write_text(
                    (FIXTURES / "manual.html").read_text(encoding="utf-8"),
                    encoding="utf-8",
                )
                return [self.document(html_path)]

            request = AuditRequest(
                probe_path=str(FIXTURES / "probe_DSL.json"),
                vendor="Cisco",
                device_model="xrv",
                version="6.3.1",
                scope="router ospf",
                manual_library="manual_db/sources.json",
                output_root=str(output_root),
            )
            reviewer = FakeReviewer()
            with (
                patch("audit_agent.load_manual_library", side_effect=fake_fetch),
                patch(
                    "audit_agent.search_vendor_site_impl",
                    return_value={"state": "failed", "results": [], "message": "mocked"},
                ),
            ):
                run_dir = run_audit(request, llm=reviewer, run_id="test-run")

            state = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
            self.assertEqual("completed", state["status"])
            self.assertEqual(7, len(state["stages"]))
            self.assertIsInstance(state["elapsed_seconds"], float)
            self.assertTrue(all(item["elapsed_seconds"] is not None for item in state["stages"]))
            self.assertTrue(reviewer.calls)
            for filename in (
                "request.json",
                "probe_model.json",
                "probe_groups.json",
                "manual_index.json",
                "ai_syntax_recoveries.json",
                "coverage.json",
                "findings.json",
                "agent_trace.json",
                "agent_tool.log",
                "review.json",
                "reviewed_findings.json",
                "report.json",
                "report.md",
            ):
                self.assertTrue((run_dir / filename).exists(), filename)
            tool_log = (run_dir / "agent_tool.log").read_text(encoding="utf-8")
            self.assertIn("| search_manual_library | hit |", tool_log)
            self.assertIn("Input :", tool_log)
            self.assertIn("Output:", tool_log)
            self.assertNotIn('"evidence":', tool_log)

    def test_workflow_marks_agent_review_failure_as_completed_with_unresolved(self):
        with tempfile.TemporaryDirectory() as directory:
            output_root = Path(directory) / "runs"

            def fake_fetch(urls, output_dir, **kwargs):
                manual_dir = Path(output_dir)
                manual_dir.mkdir(parents=True)
                html_path = manual_dir / "manual_001.html"
                html_path.write_text(
                    (FIXTURES / "manual.html").read_text(encoding="utf-8"),
                    encoding="utf-8",
                )
                return [self.document(html_path)]

            request = AuditRequest(
                probe_path=str(FIXTURES / "probe_DSL.json"),
                vendor="Cisco",
                device_model="xrv",
                version="6.3.1",
                scope="router ospf",
                manual_library="manual_db/sources.json",
                output_root=str(output_root),
            )
            with patch("audit_agent.load_manual_library", side_effect=fake_fetch):
                run_dir = run_audit(request, llm=FailingReviewer(), run_id="review-failed")

            state = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))

        self.assertEqual("completed_with_unresolved", state["status"])
        self.assertGreater(state["agent_review_failures"], 0)
        self.assertIn("Agent reviews failed", state["error"])

    def test_workflow_prints_stage_progress_timing_and_model_mismatch(self):
        with tempfile.TemporaryDirectory() as directory:
            output_root = Path(directory) / "runs"
            probe_path = Path(directory) / "graphs" / "xrv9k" / "probe_DSL.json"
            probe_path.parent.mkdir(parents=True)
            probe_path.write_text(
                (FIXTURES / "probe_DSL.json").read_text(encoding="utf-8"),
                encoding="utf-8",
            )

            def fake_fetch(urls, output_dir, **kwargs):
                manual_dir = Path(output_dir)
                manual_dir.mkdir(parents=True)
                html_path = manual_dir / "manual_001.html"
                html_path.write_text(
                    (FIXTURES / "manual.html").read_text(encoding="utf-8"),
                    encoding="utf-8",
                )
                return [self.document(html_path)]

            request = AuditRequest(
                probe_path=str(probe_path),
                vendor="Cisco",
                device_model="xrv",
                version="6.3.1",
                scope="router ospf",
                manual_library="manual_db/sources.json",
                output_root=str(output_root),
            )
            stdout = io.StringIO()
            stderr = io.StringIO()
            with (
                patch("audit_agent.load_manual_library", side_effect=fake_fetch),
                patch(
                    "audit_agent.search_vendor_site_impl",
                    return_value={"state": "failed", "results": [], "message": "mocked"},
                ),
                redirect_stdout(stdout),
                redirect_stderr(stderr),
            ):
                run_audit(request, llm=FakeReviewer(), run_id="observable-run")

        output = stdout.getvalue()
        self.assertIn("[stage] load_probe_model started", output)
        self.assertIn("[stage] render_report completed in", output)
        self.assertIn("[audit] Probe records:", output)
        self.assertIn("[audit] Rule findings:", output)
        self.assertIn("[audit] Stage times:", output)
        self.assertIn("[audit] Total time:", output)
        self.assertIn("does not exactly match", stderr.getvalue())

    def test_workflow_persists_failed_stage(self):
        with tempfile.TemporaryDirectory() as directory:
            output_root = Path(directory) / "runs"
            request = AuditRequest(
                probe_path=str(FIXTURES / "probe_DSL.json"),
                vendor="Cisco",
                device_model="xrv",
                version="6.3.1",
                scope="router ospf",
                manual_library="manual_db/sources.json",
                output_root=str(output_root),
            )
            with patch("audit_agent.load_manual_library", side_effect=RuntimeError("offline")):
                with self.assertRaisesRegex(RuntimeError, "offline"):
                    run_audit(request, llm=FakeReviewer(), run_id="failed-run")

            state = json.loads(
                (output_root / "failed-run" / "run.json").read_text(encoding="utf-8")
            )
            self.assertEqual("failed", state["status"])
            self.assertEqual("fetch_manuals", state["current_stage"])
            self.assertEqual("failed", state["stages"][-1]["status"])


if __name__ == "__main__":
    unittest.main()
