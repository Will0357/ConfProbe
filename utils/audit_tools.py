from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, is_dataclass, replace
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from time import perf_counter, sleep
from typing import Any, Mapping, Sequence
from urllib.parse import urlencode, urldefrag, urljoin, urlparse


MAX_MANUAL_BYTES = 8 * 1024 * 1024
MAX_TEMPLATE_EXPANSIONS = 256
MAX_TOPIC_PAGES_PER_SOURCE: int | None = None
MANUAL_FETCH_ATTEMPTS = 3
MANUAL_FETCH_RETRY_DELAY_SECONDS = 0.5
VENDOR_SEARCH_ATTEMPTS = 2
CISCO_HOME_URL = "https://www.cisco.com/"
CISCO_SEARCH_URL = "https://search.cisco.com/search"
CISCO_AI_RESPONSE_TIMEOUT_MS = 30_000
CISCO_AI_RESPONSE_MAX_CHARS = 4_000
CISCO_SEARCH_PARAMETERS = {
    "locale": "enUS",
    "bizcontext": "",
    "cat": "",
    "mode": "text",
    "clktyp": "enter",
    "autosuggest": "false",
    "istadisplayed": "false",
    "tareqid": "",
    "categoryvalue": "",
}
MANUAL_INDEX_VERSION = 2
FINDING_CATEGORY_ORDER = (
    "A1",
    "A2",
    "A3",
    "B1",
    "B2",
    "B3",
    "C1",
    "C2",
    "C3",
    "UNRESOLVED",
)


@dataclass(slots=True)
class CommandRecord:
    record_id: str
    template: str
    context: tuple[str, ...] = ()
    view_path: tuple[str, ...] = ()
    kind: str = "command"
    variants: tuple[str, ...] = ()
    view_name: str = ""


@dataclass(slots=True)
class ProbeCommandGroup:
    group_id: str
    template: str
    normalized_template: str
    semantic_view: str
    kind: str
    variants: tuple[str, ...]
    contexts: tuple[tuple[str, ...], ...]
    view_paths: tuple[tuple[str, ...], ...]
    record_ids: tuple[str, ...]
    semantic_views: tuple[str, ...] = ()


@dataclass(slots=True)
class ManualEvidence:
    evidence_id: str
    block_id: str
    kind: str
    text: str
    url: str


@dataclass(slots=True)
class ManualCommandBlock:
    block_id: str
    command_name: str
    title: str
    url: str
    document_title: str
    syntax_templates: tuple[str, ...]
    modes: tuple[str, ...]
    evidence: tuple[ManualEvidence, ...]
    source_role: str = "command_reference"
    source_version: str = ""
    is_target_version: bool = True
    syntax_provenance: str = "manual"
    recovery_evidence_ids: tuple[str, ...] = ()
    recovery_confidence: float = 0.0


@dataclass(slots=True)
class ProbeReference:
    group_id: str
    template: str
    semantic_view: str


@dataclass(slots=True)
class AuditFinding:
    finding_id: str
    category: str
    name: str
    reason: str
    probe_group_id: str = ""
    probe_template: str = ""
    semantic_view: str = ""
    manual_block_ids: tuple[str, ...] = ()
    manual_commands: tuple[str, ...] = ()
    probe_groups: tuple[ProbeReference, ...] = ()
    evidence: tuple[ManualEvidence, ...] = ()
    review_required: bool = True
    llm_conclusion: str = "not_reviewed"
    confidence: float = 0.0
    status: str = "candidate"
    rationale: str = ""
    syntax_provenance: str = "manual"
    requires_manual_review: bool = False


@dataclass(slots=True)
class ProbeCoverage:
    coverage_id: str
    probe_group_id: str
    template: str
    semantic_view: str
    status: str
    matched_block_ids: tuple[str, ...] = ()
    finding_ids: tuple[str, ...] = ()


@dataclass(slots=True)
class ManualDocument:
    url: str
    final_url: str
    title: str
    fetched_at: str
    html_path: str
    source_url: str = ""
    source_role: str = "command_reference"
    source_version: str = ""
    is_target_version: bool = True
    cache_dir: str = ""


@dataclass(slots=True)
class ManualSourceHealth:
    source_url: str
    source_role: str
    source_version: str
    is_target_version: bool
    status: str
    discovered_topics: int = 0
    indexed_topics: int = 0
    message: str = ""
    retry_count: int = 0
    failed_urls: tuple[str, ...] = ()
    unparsed_urls: tuple[str, ...] = ()


def to_jsonable(value: Any) -> Any:
    if is_dataclass(value) and not isinstance(value, type):
        return {key: to_jsonable(item) for key, item in asdict(value).items()}
    if isinstance(value, Mapping):
        return {str(key): to_jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [to_jsonable(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    return value


def write_json(path: str | Path, value: Any) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(to_jsonable(value), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def load_probe_model(path: str | Path) -> list[CommandRecord]:
    source_path = Path(path)
    with source_path.open("r", encoding="utf-8") as file:
        root = json.load(file)
    if not isinstance(root, dict) or root.get("node_type") != "ROOT":
        raise ValueError(f"Unsupported Probe DSL root in {source_path}")

    records: list[CommandRecord] = []

    def walk(
        node: Mapping[str, Any],
        context: tuple[str, ...],
        view_path: tuple[str, ...],
    ) -> None:
        node_type = node.get("node_type")
        child_context = context
        child_view_path = view_path
        if node_type == "ROOT":
            pass
        elif node_type in {"view_node", "terminal_node"}:
            template = str(node.get("cmd_aggregatedTemplate") or "").strip()
            variants = tuple(
                str(item).strip()
                for item in node.get("cmd_templates", [])
                if str(item).strip()
            )
            if not template:
                if len(variants) != 1:
                    raise ValueError(
                        f"Node {node.get('node_id')} has no aggregate command template"
                    )
                template = variants[0]
            kind = "enter_view" if node_type == "view_node" else "terminal"
            view_name = str(node.get("view_name") or "")
            if kind != "terminal" or _literal_tokens(template):
                records.append(
                    CommandRecord(
                        record_id=f"probe:{node.get('node_id')}",
                        template=template,
                        context=context,
                        view_path=view_path,
                        kind=kind,
                        variants=variants or (template,),
                        view_name=view_name,
                    )
                )
            if node_type == "view_node":
                child_context = context + (template,)
                child_view_path = view_path + (view_name,)
        else:
            raise ValueError(f"Unsupported Probe DSL node type: {node_type!r}")

        children = node.get("children", [])
        if not isinstance(children, list):
            raise ValueError(f"Node {node.get('node_id')} has invalid children")
        for child in children:
            if not isinstance(child, dict):
                raise ValueError(f"Node {node.get('node_id')} has a non-object child")
            walk(child, child_context, child_view_path)

    walk(root, (), ())
    return records


def group_probe_commands(records: Sequence[CommandRecord]) -> list[ProbeCommandGroup]:
    grouped: dict[tuple[str, ...], list[CommandRecord]] = defaultdict(list)
    for record in records:
        grouped[_command_language_signature(record.template, record.variants)].append(record)

    groups: list[ProbeCommandGroup] = []
    for index, (signature, items) in enumerate(sorted(grouped.items()), start=1):
        views = tuple(
            sorted({semantic_view(item.view_path, item.context) for item in items})
        )
        view = views[0] if len(views) == 1 else "mixed"
        kinds = {item.kind for item in items}
        groups.append(
            ProbeCommandGroup(
                group_id=f"P{index:05d}",
                template=min(item.template for item in items),
                normalized_template=" || ".join(signature),
                semantic_view=view,
                kind=next(iter(kinds)) if len(kinds) == 1 else "mixed",
                variants=tuple(sorted({variant for item in items for variant in item.variants})),
                contexts=tuple(sorted({item.context for item in items})),
                view_paths=tuple(sorted({item.view_path for item in items})),
                record_ids=tuple(sorted(item.record_id for item in items)),
                semantic_views=views,
            )
        )
    return groups


def _command_language_signature(
    template: str, variants: Sequence[str] = ()
) -> tuple[str, ...]:
    values = tuple(variants) or _expand_template(template)
    return tuple(sorted({normalize_template(value) for value in values}))


def semantic_view(view_path: Sequence[str], context: Sequence[str] = ()) -> str:
    value = (view_path[-1] if view_path else "").lower()
    if "-mif" in value:
        return "multi-area"
    if "-sl" in value:
        return "sham-link"
    if "-vl" in value:
        return "virtual-link"
    if value.endswith("-if]"):
        return "interface"
    if value.endswith("-ar]"):
        return "area"
    if value.endswith("-vrf]"):
        return "vrf"
    if value.endswith("-ospf]"):
        return "router"
    if not view_path:
        return "global"

    parent = context[-1].lower() if context else ""
    for prefix, mode in (
        ("multi-area-interface ", "multi-area"),
        ("interface ", "interface"),
        ("sham-link ", "sham-link"),
        ("virtual-link ", "virtual-link"),
        ("area ", "area"),
        ("vrf ", "vrf"),
        ("router ospf ", "router"),
    ):
        if parent.startswith(prefix):
            return mode
    return "unknown"


def fetch_manuals(
    urls: Sequence[str],
    output_dir: str | Path,
    *,
    max_bytes: int = MAX_MANUAL_BYTES,
    timeout: float = 30.0,
) -> list[ManualDocument]:
    try:
        import httpx
    except ImportError as exc:
        raise RuntimeError(
            "Manual fetching requires httpx; install the project requirements"
        ) from exc

    if not urls:
        raise ValueError("At least one manual URL is required")
    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    documents: list[ManualDocument] = []
    headers = {"User-Agent": "ConfProbe-Audit/0.2"}

    with httpx.Client(follow_redirects=True, timeout=timeout, headers=headers) as client:
        for index, url in enumerate(urls, start=1):
            _validate_http_url(url)
            with client.stream("GET", url) as response:
                response.raise_for_status()
                _validate_http_url(str(response.url))
                content_type = response.headers.get("content-type", "").lower()
                if content_type and "html" not in content_type:
                    raise ValueError(f"Manual URL did not return HTML: {url}")
                content_length = response.headers.get("content-length")
                if content_length and int(content_length) > max_bytes:
                    raise ValueError(f"Manual exceeds {max_bytes} bytes: {url}")
                chunks: list[bytes] = []
                total = 0
                for chunk in response.iter_bytes():
                    total += len(chunk)
                    if total > max_bytes:
                        raise ValueError(f"Manual exceeds {max_bytes} bytes: {url}")
                    chunks.append(chunk)
                encoding = response.encoding or "utf-8"
                html = b"".join(chunks).decode(encoding, errors="replace")

            stem = f"manual_{index:03d}"
            html_path = target_dir / f"{stem}.html"
            html_path.write_text(html, encoding="utf-8")
            document = ManualDocument(
                url=url,
                final_url=str(response.url),
                title=_extract_html_title(html) or str(response.url),
                fetched_at=_utc_now(),
                html_path=str(html_path),
            )
            write_json(target_dir / f"{stem}.json", document)
            documents.append(document)
    return documents


class _ManualFetchFailure(RuntimeError):
    def __init__(self, url: str, errors: Sequence[str]) -> None:
        self.url = url
        self.errors = tuple(errors)
        super().__init__(f"{url} failed after {len(errors)} attempts: {self.errors[-1]}")


def _fetch_manual_with_retries(
    url: str,
    output_dir: str | Path,
    *,
    max_bytes: int,
) -> int:
    errors: list[str] = []
    for attempt in range(1, MANUAL_FETCH_ATTEMPTS + 1):
        try:
            fetch_manuals((url,), output_dir, max_bytes=max_bytes)
            return attempt
        except Exception as exc:
            errors.append(f"{type(exc).__name__}: {exc}")
            if attempt < MANUAL_FETCH_ATTEMPTS:
                sleep(MANUAL_FETCH_RETRY_DELAY_SECONDS * attempt)
    raise _ManualFetchFailure(url, errors)


def load_manual_library(
    library_path: str | Path,
    output_dir: str | Path,
    *,
    vendor: str,
    version: str,
    max_bytes: int = MAX_MANUAL_BYTES,
) -> list[ManualDocument]:
    manifest_path = Path(library_path).resolve()
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Manual library manifest not found: {manifest_path}")

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid manual library manifest: {manifest_path}") from exc

    entries = manifest.get("manuals") if isinstance(manifest, Mapping) else None
    if entries is None and isinstance(manifest, Mapping) and "sources" in manifest:
        entries = [manifest]
    if not isinstance(entries, list):
        raise ValueError(
            "Manual library manifest must be a source entry or contain a 'manuals' array"
        )

    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    library_root = manifest_path.parent
    source_urls: list[tuple[Mapping[str, Any], str]] = []
    for entry in entries:
        if not isinstance(entry, Mapping):
            continue
        if str(entry.get("vendor", "")).strip().casefold() != vendor.strip().casefold():
            continue
        if str(entry.get("version", "")).strip().casefold() != version.strip().casefold():
            continue
        sources = entry.get("sources")
        if not isinstance(sources, list) or not sources:
            raise ValueError("Each matching manual entry requires a non-empty 'sources' array")
        for source_url in sources:
            if not isinstance(source_url, str) or not source_url.strip():
                raise ValueError("Each manual source must be a non-empty URL string")
            source_urls.append((entry, source_url.strip()))

    if not source_urls:
        raise ValueError(
            "No manual library entry matches "
            f"vendor={vendor!r}, version={version!r} in {manifest_path}"
        )

    documents: list[ManualDocument] = []
    for index, (entry, source_url) in enumerate(source_urls, start=1):
        _validate_http_url(source_url)
        cache_dir = _manual_cache_dir(library_root, entry, source_url)
        cache_html_path = cache_dir / "manual_001.html"
        if not cache_html_path.is_file():
            _fetch_manual_with_retries(source_url, cache_dir, max_bytes=max_bytes)

        html = cache_html_path.read_text(encoding="utf-8")
        title = (
            str(entry.get("title", "")).strip()
            or _extract_html_title(html)
            or source_url
        )
        source_role = _manual_source_role(source_url, title)
        detected_version = _source_version_hint(source_url, title)
        declared_version = str(entry.get("version", "")).strip()
        source_version = detected_version or declared_version
        is_target_version = not (
            source_role == "config_guide"
            and detected_version
            and detected_version.casefold() != version.casefold()
        )
        stem = f"manual_{index:03d}"
        html_path = target_dir / f"{stem}.html"
        html_path.write_text(html, encoding="utf-8")
        document = ManualDocument(
            url=source_url,
            final_url=source_url,
            title=title,
            fetched_at=_utc_now(),
            html_path=str(html_path),
            source_url=source_url,
            source_role=source_role,
            source_version=source_version,
            is_target_version=is_target_version,
            cache_dir=str(cache_dir),
        )
        write_json(target_dir / f"{stem}.json", document)
        documents.append(document)
    return documents


def _manual_cache_dir(
    library_root: Path,
    entry: Mapping[str, Any],
    source_url: str,
) -> Path:
    def path_part(value: Any) -> str:
        result = re.sub(r"[^a-z0-9]+", "-", str(value).casefold()).strip("-")
        return result or "unknown"

    source_hash = hashlib.sha256(source_url.encode("utf-8")).hexdigest()[:16]
    return (
        library_root
        / "cache"
        / path_part(entry.get("vendor", ""))
        / path_part(entry.get("platform", ""))
        / path_part(entry.get("version", ""))
        / source_hash
    )


def expand_manual_library(
    documents: Sequence[ManualDocument],
    *,
    scope: str,
    max_bytes: int = MAX_MANUAL_BYTES,
    max_topic_pages: int | None = MAX_TOPIC_PAGES_PER_SOURCE,
) -> tuple[list[ManualDocument], list[ManualSourceHealth]]:
    """Expand Cisco book landing pages into cache-backed topic documents.

    A landing page is only an index. It is deliberately excluded from the command
    index so that a failed expansion can never be mistaken for a missing command.
    """
    if max_topic_pages is not None and max_topic_pages <= 0:
        raise ValueError("max_topic_pages must be positive")

    expanded: list[ManualDocument] = []
    health: list[ManualSourceHealth] = []
    for document in documents:
        html = Path(document.html_path).read_text(encoding="utf-8")
        if _contains_command_topics(html):
            expanded.append(document)
            health.append(
                ManualSourceHealth(
                    source_url=document.source_url or document.url,
                    source_role=document.source_role,
                    source_version=document.source_version,
                    is_target_version=document.is_target_version,
                    status="complete",
                    discovered_topics=1,
                    indexed_topics=1,
                )
            )
            continue

        links = _read_cached_topic_links(document, html) or _discover_topic_links(
            html, document.final_url or document.url
        )
        if (
            document.source_role == "config_guide"
            and not links
            and _has_readable_body(html)
        ):
            expanded.append(document)
            health.append(
                ManualSourceHealth(
                    source_url=document.source_url or document.url,
                    source_role=document.source_role,
                    source_version=document.source_version,
                    is_target_version=document.is_target_version,
                    status="complete",
                    discovered_topics=1,
                    indexed_topics=1,
                )
            )
            continue

        selected = (
            links
            if max_topic_pages is None
            else links[:max_topic_pages]
        )
        source_documents: list[ManualDocument] = []
        failure_messages: list[str] = []
        failed_urls: list[str] = []
        unparsed_urls: list[str] = []
        retry_count = 0
        for topic_url in selected:
            try:
                topic_path = _cached_topic_path(document, topic_url)
                if not topic_path.is_file():
                    attempts = _fetch_manual_with_retries(
                        topic_url,
                        topic_path.parent,
                        max_bytes=max_bytes,
                    )
                    retry_count += attempts - 1
                topic_html = topic_path.read_text(encoding="utf-8")
                if not _contains_command_topics(topic_html) and document.source_role == "command_reference":
                    unparsed_urls.append(topic_url)
                    continue
                source_documents.append(
                    ManualDocument(
                        url=topic_url,
                        final_url=topic_url,
                        title=_extract_html_title(topic_html) or topic_url,
                        fetched_at=_utc_now(),
                        html_path=str(topic_path),
                        source_url=document.source_url or document.url,
                        source_role=document.source_role,
                        source_version=document.source_version,
                        is_target_version=document.is_target_version,
                        cache_dir=document.cache_dir,
                    )
                )
            except _ManualFetchFailure as exc:
                retry_count += max(0, len(exc.errors) - 1)
                failed_urls.append(topic_url)
                failure_messages.append(str(exc))
            except Exception as exc:
                failed_urls.append(topic_url)
                failure_messages.append(f"{topic_url}: {type(exc).__name__}: {exc}")

        if failure_messages:
            status = "failed" if not source_documents else "incomplete"
        elif unparsed_urls:
            status = "incomplete"
        elif max_topic_pages is not None and len(links) > max_topic_pages:
            status = "incomplete"
        elif not links:
            status = "incomplete"
        else:
            status = "complete"
        source_health = ManualSourceHealth(
            source_url=document.source_url or document.url,
            source_role=document.source_role,
            source_version=document.source_version,
            is_target_version=document.is_target_version,
            status=status,
            discovered_topics=len(links),
            indexed_topics=len(source_documents),
            message="; ".join(
                [
                    *failure_messages,
                    *(
                        [
                            f"{len(unparsed_urls)} command-reference topics could not be parsed"
                        ]
                        if unparsed_urls
                        else []
                    ),
                ]
            ),
            retry_count=retry_count,
            failed_urls=tuple(failed_urls),
            unparsed_urls=tuple(unparsed_urls),
        )
        _write_source_index(document, links, source_health)
        expanded.extend(source_documents)
        health.append(source_health)
    return expanded, health


def _contains_command_topics(html: str) -> bool:
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise RuntimeError(
            "Manual parsing requires beautifulsoup4; install the project requirements"
        ) from exc
    soup = BeautifulSoup(html, "html.parser")
    return bool(soup.select("article.topic.reference h2.title.topictitle2"))


def _has_readable_body(html: str) -> bool:
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise RuntimeError(
            "Manual parsing requires beautifulsoup4; install the project requirements"
        ) from exc
    soup = BeautifulSoup(html, "html.parser")
    if soup.body is None:
        return False
    return len(_clean_text(soup.body.get_text(" ", strip=True))) >= 40


def _discover_topic_links(html: str, source_url: str) -> list[str]:
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise RuntimeError(
            "Manual parsing requires beautifulsoup4; install the project requirements"
        ) from exc
    parsed_source = urlparse(source_url)
    source_path = parsed_source.path
    source_stem = Path(source_path).stem
    allowed_prefix = source_path.rsplit("/", 1)[0].rstrip("/") + f"/{source_stem}/"
    soup = BeautifulSoup(html, "html.parser")
    links: set[str] = set()
    for anchor in soup.select("a[href]"):
        href = str(anchor.get("href", "")).strip()
        if not href:
            continue
        absolute, _ = urldefrag(urljoin(source_url, href))
        parsed = urlparse(absolute)
        if parsed.scheme not in {"http", "https"} or parsed.netloc != parsed_source.netloc:
            continue
        path = parsed.path
        if not path.startswith(allowed_prefix) or not path.endswith(".html"):
            continue
        name = Path(path).name.casefold()
        if name in {"preface.html"} or "_clt_" in name:
            continue
        links.add(absolute)
    return sorted(links)


def _cached_topic_path(document: ManualDocument, topic_url: str) -> Path:
    source_cache = Path(document.cache_dir) if document.cache_dir else Path(document.html_path).parent
    topic_hash = hashlib.sha256(topic_url.encode("utf-8")).hexdigest()[:16]
    return source_cache / "topics" / topic_hash / "manual_001.html"


def _write_source_index(
    document: ManualDocument,
    topic_links: Sequence[str],
    health: ManualSourceHealth,
) -> None:
    if not document.cache_dir:
        return
    path = Path(document.cache_dir) / "manual_index.v2.json"
    source_html = Path(document.html_path).read_bytes()
    write_json(
        path,
        {
            "index_version": MANUAL_INDEX_VERSION,
            "source_url": document.source_url or document.url,
            "html_sha256": hashlib.sha256(source_html).hexdigest(),
            "topic_links": list(topic_links),
            "health": health,
        },
    )


def _read_cached_topic_links(document: ManualDocument, html: str) -> list[str]:
    if not document.cache_dir:
        return []
    path = Path(document.cache_dir) / "manual_index.v2.json"
    if not path.is_file():
        return []
    try:
        cached = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    if (
        cached.get("index_version") != MANUAL_INDEX_VERSION
        or cached.get("html_sha256") != hashlib.sha256(html.encode("utf-8")).hexdigest()
        or cached.get("source_url") != (document.source_url or document.url)
    ):
        return []
    links = cached.get("topic_links")
    return [str(link) for link in links] if isinstance(links, list) else []


def _manual_source_role(source_url: str, title: str) -> str:
    value = f"{source_url} {title}".casefold()
    return "config_guide" if "configuration/guide" in value or "configuration guide" in value else "command_reference"


def _source_version_hint(source_url: str, title: str) -> str:
    value = f"{source_url} {title}".casefold()
    match = re.search(r"(?:release\s*)?(\d+\.\d+(?:\.\d+)?)(?:\s*x)?", value)
    return match.group(1) if match else ""


def build_manual_index(
    documents: Sequence[ManualDocument],
    *,
    target_version: str,
    scope: str = "",
) -> tuple[list[ManualCommandBlock], list[AuditFinding]]:
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise RuntimeError(
            "Manual parsing requires beautifulsoup4; install the project requirements"
        ) from exc

    del target_version  # The manifest establishes target applicability, not page metadata.
    blocks: list[ManualCommandBlock] = []
    findings: list[AuditFinding] = []
    for document_index, document in enumerate(documents, start=1):
        html = Path(document.html_path).read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "html.parser")
        topics = [
            topic
            for topic in soup.select("article.topic.reference")
            if topic.select_one("h2.title.topictitle2")
        ]
        if not topics:
            topics = [
                topic
                for topic in soup.select("article.topic")
                if topic.select_one("h1, h2, h3")
            ]
        if not topics and document.source_role == "config_guide" and soup.body:
            topics = [soup.body]
        if not topics:
            raise ValueError(
                f"Unsupported Cisco manual layout at {document.final_url}: no content"
            )

        document_blocks: list[ManualCommandBlock] = []
        for topic_index, topic in enumerate(topics, start=1):
            block_id = f"M{document_index}:B{topic_index:04d}"
            title_element = topic.select_one("h2.title.topictitle2, h1, h2, h3")
            if title_element is None:
                title_element = soup.title
            title = _clean_text(
                title_element.get_text(" ", strip=True)
                if title_element is not None
                else document.title
            )
            command_name = _canonical_command_name(title)
            evidence = [
                ManualEvidence(
                    evidence_id=f"{block_id}:title",
                    block_id=block_id,
                    kind="title",
                    text=title,
                    url=document.final_url,
                )
            ]
            syntax_templates: list[str] = []

            intro = topic.select_one("section.body.refbody > section.section:not(.refsyn)")
            if intro:
                _append_evidence(evidence, block_id, "description", intro, document.final_url)
            else:
                _append_evidence(evidence, block_id, "description", topic, document.final_url)

            syntax = topic.select_one("section.refsyn")
            if syntax:
                for syntax_index, syntax_node in enumerate(syntax.select(".synblk"), start=1):
                    rendered = _render_syntax(syntax_node)
                    if rendered:
                        syntax_templates.append(rendered)
                        evidence.append(
                            ManualEvidence(
                                evidence_id=f"{block_id}:syntax:{syntax_index}",
                                block_id=block_id,
                                kind="syntax",
                                text=rendered,
                                url=document.final_url,
                            )
                        )

            syntax_table = topic.select_one("table.syntax")
            if syntax_table:
                for row_index, row in enumerate(syntax_table.select("tr"), start=1):
                    cells = [
                        _clean_text(cell.get_text(" ", strip=True))
                        for cell in row.find_all(["th", "td"], recursive=False)
                    ]
                    if cells:
                        evidence.append(
                            ManualEvidence(
                                evidence_id=f"{block_id}:parameter:{row_index}",
                                block_id=block_id,
                                kind="parameter",
                                text=" | ".join(cells),
                                url=document.final_url,
                            )
                        )

            for kind, selector in (
                ("modes", "section.command_modes"),
                ("default", "section.command_default"),
                ("usage", "section.usage_guidelines"),
                ("example", "section.command_examples, section.example"),
                ("history", "table.command_history"),
            ):
                node = topic.select_one(selector)
                if node:
                    _append_evidence(evidence, block_id, kind, node, document.final_url)

            modes_evidence = next((item.text for item in evidence if item.kind == "modes"), "")
            block = ManualCommandBlock(
                block_id=block_id,
                command_name=command_name,
                title=title,
                url=document.final_url,
                document_title=document.title,
                syntax_templates=tuple(syntax_templates),
                modes=tuple(sorted(_manual_semantic_modes(modes_evidence))),
                evidence=tuple(evidence),
                source_role=document.source_role,
                source_version=document.source_version,
                is_target_version=document.is_target_version,
            )
            blocks.append(block)
            document_blocks.append(block)

            invalid_syntax = any(
                not _valid_template_syntax(template) for template in block.syntax_templates
            )
            if invalid_syntax:
                findings.append(
                    AuditFinding(
                        finding_id="",
                        category="A1",
                        name="Syntax Error",
                        reason=(
                            "The formal syntax block contains unbalanced or "
                            "structurally invalid brackets."
                        ),
                        manual_block_ids=(block.block_id,),
                        manual_commands=(block.title,),
                        evidence=_unique_evidence((block,), {"syntax"}),
                    )
                )
            elif block.syntax_templates:
                conflict_reason = _micro_conflict_reason(block)
                if conflict_reason:
                    findings.append(
                        AuditFinding(
                            finding_id="",
                            category="A2",
                            name="Micro Conflict",
                            reason=conflict_reason,
                            manual_block_ids=(block.block_id,),
                            manual_commands=(block.title,),
                            evidence=_unique_evidence(
                                (block,),
                                {
                                    "syntax",
                                    "parameter",
                                    "default",
                                    "usage",
                                    "example",
                                    "description",
                                },
                            ),
                        )
                    )

    findings.extend(
        _macro_conflicts(
            [block for block in blocks if block.is_target_version],
            scope=scope,
        )
    )
    return blocks, _assign_finding_ids(findings)


def finalize_manual_source_health(
    documents: Sequence[ManualDocument],
    source_health: Sequence[ManualSourceHealth],
    blocks: Sequence[ManualCommandBlock],
) -> list[ManualSourceHealth]:
    """Mark a source incomplete when a downloaded document did not yield a block."""
    parsed_urls = {block.url for block in blocks}
    result: list[ManualSourceHealth] = []
    for health in source_health:
        source_documents = [
            document
            for document in documents
            if (document.source_url or document.url) == health.source_url
        ]
        missing_urls = [
            document.final_url
            for document in source_documents
            if document.final_url not in parsed_urls
        ]
        unparsed_urls = tuple(dict.fromkeys((*health.unparsed_urls, *missing_urls)))
        if not missing_urls:
            result.append(health)
            continue
        message = "; ".join(
            value
            for value in (
                health.message,
                f"{len(missing_urls)} downloaded topics produced no manual block",
            )
            if value
        )
        status = "failed" if health.status == "failed" else "incomplete"
        result.append(
            replace(
                health,
                status=status,
                indexed_topics=max(0, health.indexed_topics - len(missing_urls)),
                message=message,
                unparsed_urls=unparsed_urls,
            )
        )
    return result


def audit_probe_commands(
    groups: Sequence[ProbeCommandGroup],
    blocks: Sequence[ManualCommandBlock],
    index_findings: Sequence[AuditFinding] = (),
    *,
    missing_search_complete: bool = False,
) -> tuple[list[ProbeCoverage], list[AuditFinding]]:
    matches_by_group = {group.group_id: _find_manual_blocks(group, blocks) for group in groups}
    matched_block_ids = {
        block.block_id for matches in matches_by_group.values() for block in matches
    }
    active_index_findings = [
        finding
        for finding in index_findings
        if not finding.manual_block_ids
        or matched_block_ids.intersection(finding.manual_block_ids)
    ]
    for finding in active_index_findings:
        if not finding.manual_block_ids:
            continue
        references = tuple(
            ProbeReference(
                group_id=group.group_id,
                template=group.template,
                semantic_view=group.semantic_view,
            )
            for group in groups
            if any(
                block.block_id in finding.manual_block_ids
                for block in matches_by_group[group.group_id]
            )
        )
        finding.probe_groups = references
        if references:
            primary = references[0]
            finding.probe_group_id = primary.group_id
            finding.probe_template = primary.template
            finding.semantic_view = primary.semantic_view
    findings = list(active_index_findings)
    coverage_rows: list[
        tuple[ProbeCommandGroup, str, tuple[str, ...], list[AuditFinding]]
    ] = []

    for group in groups:
        matches = matches_by_group[group.group_id]
        group_findings: list[AuditFinding] = []
        if not matches:
            if missing_search_complete:
                group_findings.append(
                    _finding(
                        "C2",
                        "Command Undercoverage",
                        "No command topic matched after all configured searches completed.",
                        group,
                    )
                )
                coverage_rows.append((group, "undocumented", (), group_findings))
            else:
                group_findings.append(
                    _finding(
                        "UNRESOLVED",
                        "Search Incomplete",
                        "No local match was found; cross-version and vendor-site searches are required before C2.",
                        group,
                    )
                )
                coverage_rows.append((group, "unresolved", (), group_findings))
            findings.extend(group_findings)
            continue

        matched_ids = {block.block_id for block in matches}
        related_findings = [
            finding
            for finding in active_index_findings
            if matched_ids.intersection(finding.manual_block_ids)
        ]
        for block in matches:
            if not block.syntax_templates and _has_command_evidence(block):
                group_findings.append(
                    _finding(
                        "B3",
                        "Template Missing",
                        "The manual command topic exists, but it has no formal syntax block.",
                        group,
                        (block,),
                        tuple(
                            item
                            for item in block.evidence
                            if item.kind in {"title", "description", "example"}
                        ),
                    )
                )

        usable_blocks = [
            block
            for block in matches
            if block.syntax_templates
            and all(_valid_template_syntax(value) for value in block.syntax_templates)
        ]
        if usable_blocks:
            missing_variants, comparison_complete = _combined_probe_only(
                group, usable_blocks
            )
            if not comparison_complete:
                group_findings.append(
                    _finding(
                        "UNRESOLVED",
                        "Comparison Incomplete",
                        "The template is too complex for bounded deterministic comparison.",
                        group,
                        usable_blocks,
                        _unique_evidence(usable_blocks, {"syntax"}),
                    )
                )
            elif missing_variants:
                preview = ", ".join(missing_variants[:3])
                group_findings.append(
                    _finding(
                        "B1",
                        "Constraint Missing",
                        f"Probe branches are absent from the combined manual language: {preview}",
                        group,
                        usable_blocks,
                        _unique_evidence(
                            usable_blocks, {"syntax", "parameter", "usage"}
                        ),
                    )
                )

        mode_evidence = _unique_evidence(matches, {"title", "modes"})
        views = group.semantic_views or (group.semantic_view,)
        for view in views:
            if view == "unknown":
                group_findings.append(
                    _finding(
                        "UNRESOLVED",
                        "Probe View Unmapped",
                        "Probe view cannot be mapped to a known Cisco command mode.",
                        group,
                        matches,
                        mode_evidence,
                        semantic_view=view,
                    )
                )
            elif not any(view in block.modes for block in matches):
                group_findings.append(
                    _finding(
                        "B2",
                        "View Missing",
                        f"Probe exposes the command in {view} view, which is absent from Command Modes.",
                        group,
                        matches,
                        mode_evidence,
                        semantic_view=view,
                    )
                )

        all_related = related_findings + group_findings
        status = "issue" if all_related else "verified"
        coverage_rows.append(
            (group, status, tuple(block.block_id for block in matches), all_related)
        )
        findings.extend(group_findings)

    findings = _assign_finding_ids(findings)
    coverage = [
        ProbeCoverage(
            coverage_id=f"C{index:05d}",
            probe_group_id=group.group_id,
            template=group.template,
            semantic_view=group.semantic_view,
            status=status,
            matched_block_ids=block_ids,
            finding_ids=tuple(finding.finding_id for finding in related),
        )
        for index, (group, status, block_ids, related) in enumerate(coverage_rows, start=1)
    ]
    return coverage, findings


def update_coverage_statuses(
    coverage: Sequence[ProbeCoverage], findings: Sequence[AuditFinding]
) -> None:
    by_id = {finding.finding_id: finding for finding in findings}
    for item in coverage:
        active = [
            by_id[finding_id]
            for finding_id in item.finding_ids
            if finding_id in by_id and by_id[finding_id].status != "dismissed"
        ]
        if not active:
            item.status = "verified"
        elif any(finding.category == "C2" for finding in active):
            item.status = "undocumented"
        elif any(finding.category == "UNRESOLVED" for finding in active):
            item.status = "unresolved"
        elif all(finding.status == "unresolved" for finding in active):
            item.status = "unresolved"
        else:
            item.status = "issue"


def audit_manual_overcoverage(
    groups: Sequence[ProbeCommandGroup],
    blocks: Sequence[ManualCommandBlock],
    *,
    scope: str,
) -> list[AuditFinding]:
    """Find target command-reference languages that exceed all associated Probe languages."""
    findings: list[AuditFinding] = []
    for block in blocks:
        if not block.is_target_version or block.source_role != "command_reference":
            continue
        if not _scope_relevant(block, scope):
            continue
        if not block.syntax_templates or any(
            not _valid_template_syntax(template) for template in block.syntax_templates
        ):
            continue
        references, manual_only, comparison_complete = _manual_only_against_groups(
            block, groups
        )
        if not comparison_complete or not manual_only:
            continue
        if not references:
            name = "Command Overcoverage"
            reason = "An in-scope target-version manual command topic has no matching Probe language."
        else:
            name = "Branch Overcoverage"
            preview = ", ".join(manual_only[:3])
            reason = f"Manual branches are absent from all associated Probe languages: {preview}"
        findings.append(
            AuditFinding(
                finding_id="",
                category="C3",
                name=name,
                reason=reason,
                probe_group_id=references[0].group_id if references else "",
                probe_template=references[0].template if references else "",
                semantic_view=references[0].semantic_view if references else "",
                manual_block_ids=(block.block_id,),
                manual_commands=(block.title,),
                probe_groups=references,
                evidence=_unique_evidence((block,), {"title", "syntax", "modes"}),
                review_required=True,
                syntax_provenance=block.syntax_provenance,
                requires_manual_review=block.syntax_provenance == "ai_recovered",
            )
        )
    return _assign_finding_ids(findings)


def normalize_template(template: str) -> str:
    normalized = _clean_text(template).lower()
    normalized = re.sub(r"<\s*(-?\d+)\s*-\s*(-?\d+)\s*>", r"<range:\1:\2>", normalized)
    normalized = re.sub(r"<[^<>]+>", "<arg>", normalized)
    normalized = re.sub(r"\s*\|\s*", "|", normalized)
    normalized = re.sub(r"([{}\[\]])\s+", r"\1", normalized)
    normalized = re.sub(r"\s+([{}\[\]])", r"\1", normalized)
    return _clean_text(normalized)


def render_report(
    request: Any,
    coverage: Sequence[ProbeCoverage],
    findings: Sequence[AuditFinding],
    output_dir: str | Path,
    *,
    source_health: Sequence[ManualSourceHealth] = (),
) -> tuple[Path, Path]:
    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    category_counts = Counter(item.category for item in findings)
    status_counts = Counter(item.status for item in findings)
    coverage_counts = Counter(item.status for item in coverage)
    source_status_counts = Counter(item.status for item in source_health)
    category_rank = {category: index for index, category in enumerate(FINDING_CATEGORY_ORDER)}
    ordered_findings = sorted(
        findings, key=lambda item: (category_rank.get(item.category, len(category_rank)), item.finding_id)
    )
    report = {
        "generated_at": _utc_now(),
        "scope": "evidence-backed candidate findings; no device revalidation was performed",
        "request": to_jsonable(request),
        "summary": {
            "probe_groups": len(coverage),
            "findings": len(findings),
            "coverage": dict(sorted(coverage_counts.items())),
            "by_category": dict(sorted(category_counts.items())),
            "by_status": dict(sorted(status_counts.items())),
        },
        "coverage": [to_jsonable(item) for item in coverage],
        "findings": [to_jsonable(item) for item in ordered_findings],
        "manual_source_health": [to_jsonable(item) for item in source_health],
    }
    json_path = target_dir / "report.json"
    markdown_path = target_dir / "report.md"
    write_json(json_path, report)

    lines = [
        "# Probe-Driven Cisco Manual Audit",
        "",
        "> Findings are evidence-backed candidates; the device was not revalidated.",
        "",
        "## Summary",
        "",
        f"- Probe groups: {len(coverage)}",
        f"- Findings: {len(findings)}",
    ]
    lines.extend(f"- Coverage {key}: {value}" for key, value in sorted(coverage_counts.items()))
    lines.extend(f"- {key}: {value}" for key, value in sorted(category_counts.items()))
    lines.extend(
        f"- Manual sources {key}: {value}"
        for key, value in sorted(source_status_counts.items())
    )
    incomplete_sources = [item for item in source_health if item.status != "complete"]
    if incomplete_sources:
        lines.extend(["", "## Incomplete Manual Sources", ""])
        for item in incomplete_sources:
            lines.extend(
                [
                    f"- Source: {item.source_url}",
                    f"- Status: {item.status}",
                    f"- Topics: discovered={item.discovered_topics}, indexed={item.indexed_topics}",
                    f"- Retry count: {item.retry_count}",
                    f"- Failed URLs: {_markdown_inline(', '.join(item.failed_urls) or 'N/A')}",
                    f"- Unparsed URLs: {_markdown_inline(', '.join(item.unparsed_urls) or 'N/A')}",
                    f"- Detail: {_markdown_inline(item.message or 'N/A')}",
                    "",
                ]
            )
    lines.extend(["", "## Findings", ""])
    if not findings:
        lines.append("No candidate manual issues were found.")
    current_category = ""
    for item in ordered_findings:
        if item.category != current_category:
            current_category = item.category
            lines.extend([f"### {item.category} {item.name}", ""])
        urls = sorted({evidence.url for evidence in item.evidence if evidence.url})
        references = item.probe_groups
        if not references and item.probe_group_id:
            references = (
                ProbeReference(
                    group_id=item.probe_group_id,
                    template=item.probe_template,
                    semantic_view=item.semantic_view,
                ),
            )
        probe_groups = ", ".join(
            f"{reference.group_id}: `{_markdown_inline(reference.template)}` ({reference.semantic_view})"
            for reference in references
        )
        if not probe_groups and item.category == "C3":
            probe_groups = "No matching Probe group (manual-only check)"
        confidence = (
            "N/A (not reviewed)"
            if item.llm_conclusion == "not_reviewed"
            or item.rationale.startswith(
                ("Agent exceeded", "Agent review failed", "No bounded Agent review")
            )
            else f"{item.confidence:.2f}"
        )
        lines.extend(
            [
                f"#### {item.finding_id}",
                "",
                f"- Category: {item.category}",
                f"- Status: {item.status}",
                f"- Probe template: `{_markdown_inline(item.probe_template or 'N/A')}`",
                f"- Probe view: {item.semantic_view or 'N/A'}",
                f"- Probe groups: {probe_groups or 'N/A'}",
                f"- Manual commands: {_markdown_inline(', '.join(item.manual_commands) or 'N/A')}",
                f"- Manual blocks: {_markdown_inline(', '.join(item.manual_block_ids) or 'N/A')}",
                f"- URLs: {_markdown_inline(', '.join(urls) or 'N/A')}",
                f"- Reason: {_markdown_inline(item.reason)}",
                f"- Syntax provenance: {item.syntax_provenance}",
                f"- Manual review: {'required' if item.requires_manual_review else 'not required'}",
                f"- LLM conclusion: {item.llm_conclusion}",
                f"- Confidence: {confidence}",
                f"- Review rationale: {_markdown_inline(item.rationale or 'N/A')}",
            ]
        )
        for evidence in item.evidence:
            source = f" [{evidence.url}]" if evidence.url else ""
            lines.append(
                f"- Evidence `{evidence.evidence_id}` ({evidence.kind}): "
                f"{_markdown_inline(evidence.text)}{source}"
            )
        lines.append("")
    markdown_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, markdown_path


class _ExpansionLimit(ValueError):
    pass


def _find_manual_blocks(
    group: ProbeCommandGroup, blocks: Sequence[ManualCommandBlock]
) -> list[ManualCommandBlock]:
    return [
        block
        for block in blocks
        if _protocol_compatible(block, _group_protocol_scope(group))
        and _block_language_relation(group.variants or (group.template,), block)["matches"]
    ]


def _context_tokens(contexts: Sequence[Sequence[str]]) -> tuple[str, ...]:
    ignored = {
        "address-family",
        "configuration",
        "config",
        "global",
        "interface",
        "router",
        "unicast",
        "view",
    }
    values = {
        token
        for context in contexts
        for value in context
        for token in _literal_tokens(value)
        if token not in ignored
    }
    return tuple(sorted(values))


def _protocol_from_text(text: str) -> str:
    value = text.casefold()
    protocols: set[str] = set()
    if re.search(r"\bospf(?:[\s_-]*v(?:ersion)?[\s_-]*3|v3)\b", value):
        protocols.add("ospfv3")
    elif re.search(r"\bospf\b", value):
        protocols.add("ospf")
    if re.search(r"\bis[-\s]?is\b", value):
        protocols.add("isis")
    if re.search(r"\bbgp\b", value):
        protocols.add("bgp")
    if re.search(r"\beigrp\b", value):
        protocols.add("eigrp")
    if re.search(r"\brip\b", value):
        protocols.add("rip")
    return next(iter(protocols)) if len(protocols) == 1 else ""


def _block_protocol(block: ManualCommandBlock) -> str:
    return _protocol_from_text(
        " ".join((block.title, block.document_title, block.url))
    )


def _protocol_compatible(block: ManualCommandBlock, scope: str) -> bool:
    scope_protocol = _protocol_from_text(scope)
    block_protocol = _block_protocol(block)
    return not scope_protocol or not block_protocol or scope_protocol == block_protocol


def _context_protocols(contexts: Sequence[Sequence[str]]) -> set[str]:
    return {
        protocol
        for context in contexts
        if (protocol := _protocol_from_text(" ".join(context)))
    }


def _group_protocol_scope(group: ProbeCommandGroup) -> str:
    protocols = _context_protocols(group.contexts)
    return next(iter(protocols)) if len(protocols) == 1 else ""


def _block_search_text(block: ManualCommandBlock) -> str:
    return " ".join(
        [
            block.title,
            block.command_name,
            block.document_title,
            block.url,
            *(item.text for item in block.evidence),
        ]
    ).casefold()


@dataclass(frozen=True, slots=True)
class _SymbolicToken:
    kind: str
    value: str = ""
    low: int | None = None
    high: int | None = None


@dataclass(frozen=True, slots=True)
class _SymbolicBranch:
    text: str
    tokens: tuple[_SymbolicToken, ...]


@lru_cache(maxsize=8192)
def _symbolic_branches(template: str) -> tuple[_SymbolicBranch, ...]:
    return tuple(
        _SymbolicBranch(
            text=branch,
            tokens=tuple(_symbolic_token(token) for token in _raw_template_tokens(branch)),
        )
        for branch in _expand_template(template)
    )


def _symbolic_token(token: str) -> _SymbolicToken:
    if not token.startswith("<"):
        return _SymbolicToken("literal", token.casefold())
    value = token[1:-1].strip().casefold()
    match = re.fullmatch(r"(-?\d+)\s*-\s*(-?\d+)", value)
    if match:
        low, high = (int(item) for item in match.groups())
        return _SymbolicToken("range", value, low, high)
    return _SymbolicToken("argument", value)


def _language_from_templates(templates: Sequence[str]) -> tuple[_SymbolicBranch, ...]:
    branches: dict[tuple[_SymbolicToken, ...], _SymbolicBranch] = {}
    for template in templates:
        for branch in _symbolic_branches(template):
            branches.setdefault(branch.tokens, branch)
    return tuple(branches.values())


def _branches_intersect(left: _SymbolicBranch, right: _SymbolicBranch) -> bool:
    if len(left.tokens) != len(right.tokens):
        return False
    for first, second in zip(left.tokens, right.tokens):
        if first.kind == second.kind == "literal":
            if first.value != second.value:
                return False
            continue
        if first.kind == "literal" or second.kind == "literal":
            return False
        if first.kind == second.kind == "range":
            if first.high is None or second.high is None or max(first.low or 0, second.low or 0) > min(first.high, second.high):
                return False
    return True


def _ranges_cover(
    ranges: Sequence[tuple[str, str]], low: int, high: int
) -> bool:
    return any(int(start) <= low and int(end) >= high for start, end in ranges)


def _manual_branch_covers_probe(
    manual: _SymbolicBranch,
    probe: _SymbolicBranch,
    parameter_ranges: Mapping[str, set[tuple[str, str]]],
) -> bool:
    if not _branches_intersect(manual, probe):
        return False
    for manual_token, probe_token in zip(manual.tokens, probe.tokens):
        if probe_token.kind != "range":
            continue
        if manual_token.kind == "range":
            if (manual_token.low or 0) > (probe_token.low or 0) or (manual_token.high or 0) < (probe_token.high or 0):
                return False
        elif manual_token.kind == "argument":
            if not _ranges_cover(
                tuple(parameter_ranges.get(manual_token.value, set())),
                probe_token.low or 0,
                probe_token.high or 0,
            ):
                return False
    return True


def _probe_branch_covers_manual(
    probe: _SymbolicBranch,
    manual: _SymbolicBranch,
    parameter_ranges: Mapping[str, set[tuple[str, str]]],
) -> bool:
    if not _branches_intersect(probe, manual):
        return False
    for probe_token, manual_token in zip(probe.tokens, manual.tokens):
        if manual_token.kind != "range":
            continue
        if probe_token.kind == "range":
            if (probe_token.low or 0) > (manual_token.low or 0) or (probe_token.high or 0) < (manual_token.high or 0):
                return False
        elif probe_token.kind == "argument":
            continue
    return True


def _title_matches_probe_variants(
    command_name: str, variants: Sequence[str]
) -> bool:
    title_tokens = _literal_tokens(command_name)
    if not title_tokens:
        return False
    try:
        branches = _language_from_templates(variants)
    except (_ExpansionLimit, ValueError):
        return False
    for branch in branches:
        literals = [
            token.value if token.kind == "literal" else "<arg>"
            for token in branch.tokens
        ]
        for index in range(len(literals) - len(title_tokens) + 1):
            if literals[index : index + len(title_tokens)] == title_tokens:
                return True
    return False


def _block_language_relation(
    probe_variants: Sequence[str], block: ManualCommandBlock
) -> dict[str, Any]:
    variants = tuple(probe_variants)
    title_match = _title_matches_probe_variants(block.command_name, variants)
    if not block.syntax_templates:
        return {
            "state": "syntaxless",
            "matches": title_match and _has_command_evidence(block),
            "intersection": (),
            "probe_only": (),
            "manual_only": (),
            "comparison_complete": True,
            "syntax_provenance": block.syntax_provenance,
        }
    if any(not _valid_template_syntax(template) for template in block.syntax_templates):
        return {
            "state": "invalid_syntax",
            "matches": title_match,
            "intersection": (),
            "probe_only": (),
            "manual_only": (),
            "comparison_complete": True,
            "syntax_provenance": block.syntax_provenance,
        }
    try:
        probe_branches = _language_from_templates(variants)
        manual_branches = _language_from_templates(block.syntax_templates)
    except (_ExpansionLimit, ValueError) as exc:
        return {
            "state": "incomplete",
            "matches": False,
            "intersection": (),
            "probe_only": (),
            "manual_only": (),
            "comparison_complete": False,
            "message": str(exc),
            "syntax_provenance": block.syntax_provenance,
        }
    parameter_ranges = _parameter_ranges(block)
    intersection_examples: list[tuple[str, str]] = []
    intersection_count = 0
    for probe in probe_branches:
        for manual in manual_branches:
            if not _branches_intersect(probe, manual):
                continue
            intersection_count += 1
            if len(intersection_examples) < 12:
                intersection_examples.append((probe.text, manual.text))
    probe_only = tuple(
        probe.text
        for probe in probe_branches
        if not any(
            _manual_branch_covers_probe(manual, probe, parameter_ranges)
            for manual in manual_branches
        )
    )
    manual_only = tuple(
        manual.text
        for manual in manual_branches
        if not any(
            _probe_branch_covers_manual(probe, manual, parameter_ranges)
            for probe in probe_branches
        )
    )
    return {
        "state": "hit" if intersection_count else "miss",
        "matches": bool(intersection_count),
        "intersection": tuple(intersection_examples),
        "intersection_count": intersection_count,
        "probe_only": probe_only,
        "manual_only": manual_only,
        "comparison_complete": True,
        "syntax_provenance": block.syntax_provenance,
    }


def _combined_probe_only(
    group: ProbeCommandGroup, blocks: Sequence[ManualCommandBlock]
) -> tuple[tuple[str, ...], bool]:
    try:
        probe_branches = _language_from_templates(group.variants or (group.template,))
    except (_ExpansionLimit, ValueError):
        return (), False
    manual_entries: list[tuple[_SymbolicBranch, Mapping[str, set[tuple[str, str]]]]] = []
    try:
        for block in blocks:
            if not block.syntax_templates or any(
                not _valid_template_syntax(template) for template in block.syntax_templates
            ):
                continue
            ranges = _parameter_ranges(block)
            manual_entries.extend(
                (branch, ranges) for branch in _language_from_templates(block.syntax_templates)
            )
    except (_ExpansionLimit, ValueError):
        return (), False
    if not manual_entries:
        return (), True
    return (
        tuple(
            probe.text
            for probe in probe_branches
            if not any(
                _manual_branch_covers_probe(manual, probe, ranges)
                for manual, ranges in manual_entries
            )
        ),
        True,
    )


def _manual_only_against_groups(
    block: ManualCommandBlock, groups: Sequence[ProbeCommandGroup]
) -> tuple[tuple[ProbeReference, ...], tuple[str, ...], bool]:
    try:
        manual_branches = _language_from_templates(block.syntax_templates)
    except (_ExpansionLimit, ValueError):
        return (), (), False
    parameter_ranges = _parameter_ranges(block)
    related: list[ProbeCommandGroup] = []
    probe_branches: list[_SymbolicBranch] = []
    for group in groups:
        if not _protocol_compatible(block, _group_protocol_scope(group)):
            continue
        relation = _block_language_relation(group.variants or (group.template,), block)
        if relation["state"] == "incomplete":
            return (), (), False
        if not relation["matches"]:
            continue
        try:
            probe_branches.extend(
                _language_from_templates(group.variants or (group.template,))
            )
        except (_ExpansionLimit, ValueError):
            return (), (), False
        related.append(group)
    manual_only = tuple(
        manual.text
        for manual in manual_branches
        if not any(
            _probe_branch_covers_manual(probe, manual, parameter_ranges)
            for probe in probe_branches
        )
    )
    references = tuple(
        ProbeReference(
            group_id=group.group_id,
            template=group.template,
            semantic_view=group.semantic_view,
        )
        for group in related
    )
    return references, manual_only, True


def _language_relation_summary(relation: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "state": relation.get("state", "unknown"),
        "matches": bool(relation.get("matches")),
        "comparison_complete": bool(relation.get("comparison_complete")),
        "syntax_provenance": relation.get("syntax_provenance", "manual"),
        "intersection_count": int(relation.get("intersection_count", 0)),
        "intersection": [
            {"probe": probe, "manual": manual}
            for probe, manual in relation.get("intersection", ())
        ],
        "probe_only": list(relation.get("probe_only", ())),
        "manual_only": list(relation.get("manual_only", ())),
        "message": relation.get("message", ""),
    }


@lru_cache(maxsize=4096)
def _expand_template(template: str, limit: int = MAX_TEMPLATE_EXPANSIONS) -> tuple[str, ...]:
    template = _clean_text(template)
    opening = next((index for index, char in enumerate(template) if char in "{["), -1)
    if opening < 0:
        return (template,)
    closing = _matching_bracket(template, opening)
    if closing < 0:
        raise ValueError("unbalanced template")
    inner = template[opening + 1 : closing]
    branches = _split_top_level(inner)
    if template[opening] == "[":
        branches = [""] + branches
    results: list[str] = []
    for branch in branches:
        combined = f"{template[:opening]} {branch} {template[closing + 1:]}"
        results.extend(_expand_template(combined, limit))
        if len(results) > limit:
            raise _ExpansionLimit(f"template expands beyond {limit} variants")
    return tuple(dict.fromkeys(_clean_text(item) for item in results))


def _matching_bracket(text: str, opening: int) -> int:
    pairs = {"{": "}", "[": "]"}
    expected = pairs[text[opening]]
    stack = [text[opening]]
    for index in range(opening + 1, len(text)):
        char = text[index]
        if char in pairs:
            stack.append(char)
        elif char in "}]":
            if not stack or pairs[stack[-1]] != char:
                return -1
            stack.pop()
            if not stack:
                return index if char == expected else -1
    return -1


def _split_top_level(text: str) -> list[str]:
    parts: list[str] = []
    stack: list[str] = []
    start = 0
    pairs = {"{": "}", "[": "]"}
    for index, char in enumerate(text):
        if char in pairs:
            stack.append(char)
        elif char in "}]" and stack:
            stack.pop()
        elif char == "|" and not stack:
            parts.append(text[start:index])
            start = index + 1
    parts.append(text[start:])
    return parts


def _template_tokens(template: str) -> list[str]:
    normalized = re.sub(r"<[^<>]+>", " <arg> ", _clean_text(template).lower())
    return re.findall(r"<arg>|[a-z0-9_.:/-]+", normalized)


def _raw_template_tokens(template: str) -> list[str]:
    return re.findall(r"<[^<>]+>|[a-z0-9_.:/-]+", _clean_text(template).lower())


def _raw_templates_match(left: Sequence[str], right: Sequence[str]) -> bool:
    if len(left) != len(right):
        return False
    return all(
        first == second or first.startswith("<") or second.startswith("<")
        for first, second in zip(left, right)
    )


def _literal_tokens(template: str) -> list[str]:
    return [token for token in _template_tokens(template) if token != "<arg>"]


def _starts_with_tokens(template: str, prefix: Sequence[str]) -> bool:
    tokens = _template_tokens(template)
    index = 0
    for token in tokens:
        if token == "<arg>":
            continue
        if index >= len(prefix) or token != prefix[index]:
            return False
        index += 1
        if index == len(prefix):
            return True
    return False


def _valid_template_syntax(template: str) -> bool:
    stack: list[str] = []
    pairs = {"{": "}", "[": "]"}
    for char in template:
        if char in pairs:
            stack.append(char)
        elif char in "}]":
            if not stack or pairs[stack.pop()] != char:
                return False
    if stack:
        return False
    if re.search(r"\|\s*\||\{\s*\||\[\s*\||\|\s*}|\|\s*\]", template):
        return False
    try:
        _expand_template(template)
    except _ExpansionLimit:
        return True
    except ValueError:
        return False
    return True


def _micro_conflict_reason(block: ManualCommandBlock) -> str:
    parameter_ranges = _parameter_ranges(block)
    syntax_ranges = {
        match
        for template in block.syntax_templates
        for match in re.findall(
            r"<\s*(-?\d+)\s*-\s*(-?\d+)\s*>", template.lower()
        )
    }
    documented_ranges = {value for values in parameter_ranges.values() for value in values}
    if len(syntax_ranges) == len(documented_ranges) == 1 and syntax_ranges != documented_ranges:
        return "Formal syntax and parameter descriptions specify different numeric ranges."

    syntax_text = " ".join(block.syntax_templates).lower()
    for item in block.evidence:
        if item.kind != "parameter":
            continue
        parameter = _parameter_name(item.text)
        if parameter and parameter not in {
            "syntax",
            "parameter",
            "command",
            "description",
            "note",
        }:
            pattern = rf"(?<![a-z0-9_-]){re.escape(parameter)}(?![a-z0-9_-])"
            if not re.search(pattern, syntax_text):
                return f"Parameter table entry {parameter} is absent from formal syntax."

    examples = [item.text for item in block.evidence if item.kind == "example"]
    manual_variants: list[str] = []
    try:
        manual_variants = [
            variant
            for syntax in block.syntax_templates
            if not syntax.lower().startswith("no ")
            for variant in _expand_template(syntax)
        ]
    except (ValueError, _ExpansionLimit):
        return "Formal syntax cannot be compared with its examples."
    for example in examples:
        for command in _example_commands(example, block.command_name):
            if not any(
                _example_matches(command, syntax, parameter_ranges)
                for syntax in manual_variants
            ):
                return f"Example command is not covered by formal syntax: {command}"
    return ""


def _parameter_name(text: str) -> str:
    name = text.split("|", 1)[0].strip().lower()
    name = re.sub(r"^<|>$", "", name)
    return name if re.fullmatch(r"[a-z][a-z0-9_-]*", name) else ""


def _parameter_ranges(
    block: ManualCommandBlock,
) -> dict[str, set[tuple[str, str]]]:
    ranges: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for item in block.evidence:
        if item.kind != "parameter":
            continue
        parameter = _parameter_name(item.text)
        if parameter in {
            "syntax",
            "parameter",
            "command",
            "description",
            "note",
        } or not parameter:
            continue
        ranges[parameter].update(
            re.findall(r"(-?\d+)\s*(?:-|to|through)\s*(-?\d+)", item.text.lower())
        )

    return ranges


def _example_matches(
    command: str,
    syntax: str,
    parameter_ranges: Mapping[str, set[tuple[str, str]]],
) -> bool:
    command_tokens = _raw_template_tokens(command)
    syntax_tokens = _raw_template_tokens(syntax)
    if not _raw_templates_match(command_tokens, syntax_tokens):
        return False
    for value, parameter in zip(command_tokens, syntax_tokens):
        if not parameter.startswith("<") or not re.fullmatch(r"-?\d+", value):
            continue
        name = parameter.strip("<>").lower()
        ranges = parameter_ranges.get(name, set())
        direct = re.fullmatch(r"(-?\d+)\s*-\s*(-?\d+)", name)
        if direct:
            ranges = ranges | {direct.groups()}
        if ranges and not any(int(low) <= int(value) <= int(high) for low, high in ranges):
            return False
    return True


def _example_commands(text: str, command_name: str) -> list[str]:
    title_tokens = _literal_tokens(command_name)
    commands: list[str] = []
    for line in text.splitlines():
        candidate = line.split("#", 1)[-1].strip() if "#" in line else line.strip()
        if title_tokens and _starts_with_tokens(candidate, title_tokens):
            commands.append(candidate)
    return commands


def _has_command_evidence(block: ManualCommandBlock) -> bool:
    command_tokens = _literal_tokens(block.command_name)
    if not command_tokens:
        return False
    for item in block.evidence:
        if item.kind not in {"description", "example", "usage"}:
            continue
        text_tokens = _literal_tokens(item.text)
        if all(token in text_tokens for token in command_tokens):
            return True
    return False


def _scope_relevant(block: ManualCommandBlock, scope: str) -> bool:
    if not _protocol_compatible(block, scope):
        return False
    scope_tokens = _context_tokens((tuple(scope.split()),))
    if not scope_tokens:
        return True
    block_tokens = set(_literal_tokens(_block_search_text(block)))
    return all(token in block_tokens for token in scope_tokens)


def _macro_conflicts(
    blocks: Sequence[ManualCommandBlock], *, scope: str = ""
) -> list[AuditFinding]:
    by_name: dict[str, list[ManualCommandBlock]] = defaultdict(list)
    for block in blocks:
        if not _scope_relevant(block, scope):
            continue
        by_name[block.command_name].append(block)
    findings: list[AuditFinding] = []
    for name, items in by_name.items():
        if len({item.url for item in items}) < 2:
            continue
        signatures = {
            (
                tuple(sorted(normalize_template(value) for value in item.syntax_templates)),
                tuple(sorted(item.modes)),
                tuple(
                    sorted(
                        normalize_template(evidence.text)
                        for evidence in item.evidence
                        if evidence.kind == "parameter"
                    )
                ),
            )
            for item in items
        }
        if len(signatures) > 1:
            findings.append(
                AuditFinding(
                    finding_id="",
                    category="A3",
                    name="Macro Conflict",
                    reason="Different supplied manual pages describe the same command differently.",
                    manual_block_ids=tuple(item.block_id for item in items),
                    manual_commands=tuple(item.title for item in items),
                    evidence=_unique_evidence(items, {"syntax", "modes", "parameter"}),
                )
            )
    return findings


def _finding(
    category: str,
    name: str,
    reason: str,
    group: ProbeCommandGroup,
    blocks: Sequence[ManualCommandBlock] = (),
    evidence: Sequence[ManualEvidence] = (),
    semantic_view: str | None = None,
) -> AuditFinding:
    if not evidence:
        evidence = (
            ManualEvidence(
                evidence_id=f"{group.group_id}:probe",
                block_id="",
                kind="probe_template",
                text=group.template,
                url="",
            ),
        )
    recovered = any(block.syntax_provenance == "ai_recovered" for block in blocks)
    return AuditFinding(
        finding_id="",
        category=category,
        name=name,
        reason=reason,
        probe_group_id=group.group_id,
        probe_template=group.template,
        semantic_view=group.semantic_view if semantic_view is None else semantic_view,
        manual_block_ids=tuple(block.block_id for block in blocks),
        manual_commands=tuple(block.title for block in blocks),
        probe_groups=(
            ProbeReference(
                group_id=group.group_id,
                template=group.template,
                semantic_view=group.semantic_view,
            ),
        ),
        evidence=tuple(evidence),
        syntax_provenance="ai_recovered" if recovered else "manual",
        requires_manual_review=recovered and category in {"B1", "C3"},
    )


def _assign_finding_ids(findings: Sequence[AuditFinding]) -> list[AuditFinding]:
    for index, finding in enumerate(findings, start=1):
        finding.finding_id = f"F{index:05d}"
    return list(findings)


def _unique_evidence(
    blocks: Sequence[ManualCommandBlock], kinds: set[str] | None = None
) -> tuple[ManualEvidence, ...]:
    result: list[ManualEvidence] = []
    seen: set[str] = set()
    for block in blocks:
        for item in block.evidence:
            if kinds is not None and item.kind not in kinds:
                continue
            if item.evidence_id not in seen:
                seen.add(item.evidence_id)
                result.append(item)
    return tuple(result)


def _append_evidence(
    evidence: list[ManualEvidence],
    block_id: str,
    kind: str,
    node: Any,
    url: str,
) -> None:
    if kind == "example":
        commands = [
            _clean_text(command.get_text(" ", strip=True))
            for command in node.select("kbd.userinput")
        ]
        text = "\n".join(dict.fromkeys(command for command in commands if command))
        if not text:
            text = _clean_text(node.get_text(" ", strip=True))
    else:
        text = _clean_text(node.get_text(" ", strip=True))
    if text:
        evidence.append(
            ManualEvidence(
                evidence_id=f"{block_id}:{kind}",
                block_id=block_id,
                kind=kind,
                text=text,
                url=url,
            )
        )


def _render_syntax(node: Any) -> str:
    try:
        from bs4 import NavigableString
    except ImportError:
        return _clean_text(node.get_text(" ", strip=True))

    def render(item: Any) -> str:
        if isinstance(item, NavigableString):
            return str(item)
        if getattr(item, "name", None) == "var":
            return f"<{_clean_text(item.get_text(' ', strip=True))}>"
        if getattr(item, "name", None) == "br":
            return " "
        return "".join(render(child) for child in getattr(item, "children", ()))

    return _clean_text(render(node))


def _manual_semantic_modes(text: str) -> set[str]:
    value = text.lower()
    modes: set[str] = set()
    patterns = (
        (r"global(?: [a-z0-9]+)* configuration", "global"),
        (r"multi-area(?: interface)? configuration", "multi-area"),
        (r"sham-link configuration", "sham-link"),
        (r"virtual-link configuration", "virtual-link"),
        (r"(?:ospfv?2? )?interface configuration", "interface"),
        (r"(?:ospfv?2? )?area configuration", "area"),
        (r"(?:ospfv?2? )?vrf configuration", "vrf"),
        (r"router(?: ospfv?2?)? configuration|ospfv?2? router configuration|ospf configuration", "router"),
    )
    for pattern, mode in patterns:
        if re.search(pattern, value):
            modes.add(mode)
    return modes


def _canonical_command_name(title: str) -> str:
    value = re.sub(r"\s*\((?:ospf[^)]*|ospfv[^)]*)\)\s*$", "", title, flags=re.I)
    return _clean_text(value).lower()


def _clean_text(value: str, *, preserve_lines: bool = False) -> str:
    value = value.replace("\xa0", " ")
    if preserve_lines:
        lines = [re.sub(r"[ \t]+", " ", line).strip() for line in value.splitlines()]
        return "\n".join(line for line in lines if line)
    return re.sub(r"\s+", " ", value).strip()


def _validate_http_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"Only absolute HTTP/HTTPS manual URLs are supported: {url}")


def _extract_html_title(html: str) -> str:
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise RuntimeError(
            "Manual parsing requires beautifulsoup4; install the project requirements"
        ) from exc
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.get_text(" ", strip=True) if soup.title else ""


def _markdown_inline(value: str) -> str:
    return re.sub(r"\s+", " ", value).replace("`", "'").strip()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()



def search_manual_library_impl(
    query: str,
    blocks: Sequence[ManualCommandBlock],
    source_health: Sequence[ManualSourceHealth],
    *,
    scope: str = "target",
    contexts: Sequence[Sequence[str]] = (),
    variants: Sequence[str] = (),
) -> dict[str, Any]:
    """Compare the complete Probe language with each eligible local manual block."""
    if scope not in {"target", "other_local_versions"}:
        raise ValueError("scope must be 'target' or 'other_local_versions'")
    target = scope == "target"
    context_protocols = _context_protocols(contexts)
    protocol_scope = next(iter(context_protocols)) if len(context_protocols) == 1 else ""
    eligible_blocks = [
        block
        for block in blocks
        if block.is_target_version is target
        and _protocol_compatible(block, protocol_scope)
    ]
    eligible_health = [
        item
        for item in source_health
        if item.is_target_version is target
    ]
    probe_variants = tuple(variants) or (query,)
    relations = [
        (block, _block_language_relation(probe_variants, block))
        for block in eligible_blocks
    ]
    matches = [(block, relation) for block, relation in relations if relation["matches"]]
    comparison_incomplete = any(
        relation["state"] == "incomplete" for _, relation in relations
    )
    ambiguous = False
    if len(context_protocols) > 1:
        matched_protocols = {
            protocol
            for block, _ in matches
            if (protocol := _block_protocol(block)) in context_protocols
        }
        ambiguous = len(matched_protocols) > 1
    complete = bool(eligible_health) and all(item.status == "complete" for item in eligible_health)
    if ambiguous:
        state = "ambiguous"
    elif matches:
        state = "hit"
    elif comparison_incomplete:
        state = "incomplete"
    elif complete or (scope == "other_local_versions" and not eligible_health):
        state = "miss_complete"
    else:
        state = "incomplete"
    return {
        "query": query,
        "scope": scope,
        "state": state,
        "complete": complete,
        "ambiguous": ambiguous,
        "source_status": [to_jsonable(item) for item in eligible_health],
        "results": [
            {
                **_manual_block_summary(block),
                "language_relation": _language_relation_summary(relation),
            }
            for block, relation in matches
        ],
    }


def inspect_manual_match_impl(
    probed_template: str,
    block_ids: Sequence[str],
    blocks: Sequence[ManualCommandBlock],
    *,
    probed_variants: Sequence[str] = (),
) -> dict[str, Any]:
    selected = [block for block in blocks if block.block_id in set(block_ids)]
    if not selected:
        return {
            "state": "not_found",
            "found": False,
            "message": "Manual blocks were not found",
        }
    syntax_diffs = [
        ast_syntax_diff_impl(probed_template, syntax)
        for block in selected
        for syntax in block.syntax_templates
    ]
    variants = tuple(probed_variants) or (probed_template,)
    relations = [
        {
            "block_id": block.block_id,
            **_language_relation_summary(_block_language_relation(variants, block)),
        }
        for block in selected
    ]
    return {
        "state": "hit",
        "found": True,
        "blocks": [_manual_block_summary(block, include_evidence=True) for block in selected],
        "syntax_diffs": syntax_diffs,
        "language_comparisons": relations,
    }


def search_vendor_site_impl(
    vendor: str,
    query: str,
    discovered_dir: str | Path,
    *,
    contexts: Sequence[Sequence[str]] = (),
    platform: str = "",
    version: str = "",
    browser: Any | None = None,
) -> dict[str, Any]:
    """Run an official-site search without mutating the configured manual library."""
    target_dir = Path(discovered_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    search_phrase = _vendor_search_phrase(query, contexts)
    cache_key = json.dumps(
        {
            "vendor": vendor,
            "query": query,
            "contexts": contexts,
            "platform": platform,
            "version": version,
        },
        ensure_ascii=False,
        sort_keys=True,
    )
    cache_path = target_dir / f"vendor_search_{hashlib.sha256(cache_key.encode('utf-8')).hexdigest()[:16]}.json"
    if cache_path.is_file():
        return json.loads(cache_path.read_text(encoding="utf-8"))
    if vendor.casefold() != "cisco":
        result = {
            "state": "unsupported",
            "vendor": vendor,
            "query": query,
            "search_phrase": search_phrase,
            "results": [],
            "message": f"Official-site search is not implemented for {vendor}.",
        }
        return result
    sync_playwright = None
    if browser is None:
        import_started = perf_counter()
        try:
            from playwright.sync_api import sync_playwright
        except ImportError as exc:
            return {
                "state": "failed",
                "vendor": vendor,
                "query": query,
                "search_phrase": search_phrase,
                "results": [],
                "attempts": [
                    {
                        "attempt": 0,
                        "state": "failed",
                        "elapsed_seconds": perf_counter() - import_started,
                        "error": f"{type(exc).__name__}: {exc}",
                    }
                ],
                "message": "Playwright is not installed; cannot complete Cisco official-site search.",
            }
    attempts: list[dict[str, Any]] = []
    for attempt in range(1, VENDOR_SEARCH_ATTEMPTS + 1):
        started = perf_counter()
        try:
            if browser is None:
                assert sync_playwright is not None
                with sync_playwright() as playwright:
                    temporary_browser = playwright.chromium.launch(headless=True)
                    try:
                        (
                            state,
                            results,
                            message,
                            navigation,
                            verification_errors,
                            ai_response,
                        ) = _search_cisco_with_browser(temporary_browser, query, search_phrase)
                    finally:
                        temporary_browser.close()
            else:
                (
                    state,
                    results,
                    message,
                    navigation,
                    verification_errors,
                    ai_response,
                ) = _search_cisco_with_browser(browser, query, search_phrase)
            attempt_result = {
                "attempt": attempt,
                "state": state,
                "elapsed_seconds": perf_counter() - started,
                "search_phrase": search_phrase,
                "navigation": navigation,
                "verification_errors": verification_errors,
                "ai_response_state": ai_response.get("state", "unavailable"),
            }
            attempts.append(attempt_result)
            if state in {"found", "not_found"}:
                result = {
                    "state": state,
                    "vendor": vendor,
                    "query": query,
                    "search_phrase": search_phrase,
                    "results": results,
                    "ai_response": ai_response,
                    "attempts": attempts,
                    "message": message,
                }
                write_json(cache_path, result)
                return result
            if state == "ambiguous" or attempt == VENDOR_SEARCH_ATTEMPTS:
                return {
                    "state": state,
                    "vendor": vendor,
                    "query": query,
                    "search_phrase": search_phrase,
                    "results": results,
                    "ai_response": ai_response,
                    "attempts": attempts,
                    "message": message,
                }
        except Exception as exc:
            attempts.append(
                {
                    "attempt": attempt,
                    "state": "failed",
                    "elapsed_seconds": perf_counter() - started,
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )
            if attempt == VENDOR_SEARCH_ATTEMPTS:
                return {
                    "state": "failed",
                    "vendor": vendor,
                    "query": query,
                    "search_phrase": search_phrase,
                    "results": [],
                    "attempts": attempts,
                    "message": "Cisco official-site search failed after retries.",
                }
    raise AssertionError("unreachable")


def _search_cisco_with_browser(
    browser: Any,
    query: str,
    search_phrase: str,
) -> tuple[str, list[dict[str, Any]], str, str, list[str], dict[str, Any]]:
    page = browser.new_page()
    try:
        navigation = _open_cisco_search(page, search_phrase)
        ai_response = _wait_for_cisco_ai_response(page)
        ranked_results: dict[str, dict[str, Any]] = {}
        for anchor in page.locator("a[href]").all():
            href = str(anchor.get_attribute("href") or "")
            text = _clean_text(anchor.inner_text())
            absolute = urljoin(page.url, href)
            host = urlparse(absolute).hostname or ""
            match_score = _search_result_match_score(query, f"{text} {absolute}")
            if host.endswith("cisco.com") and text and match_score > 0:
                existing = ranked_results.get(absolute)
                if existing is None or match_score > existing["match_score"]:
                    ranked_results[absolute] = {
                        "title": text[:240],
                        "url": absolute,
                        "match_score": match_score,
                    }
            if len(ranked_results) >= 50:
                break
        results = sorted(
            ranked_results.values(),
            key=lambda item: (-item["match_score"], item["url"]),
        )

        verification_errors: list[str] = []
        verified_results: list[dict[str, Any]] = []
        for item in results[:5]:
            detail_page = browser.new_page()
            try:
                detail_page.goto(item["url"], wait_until="domcontentloaded", timeout=30_000)
                body = _clean_text(detail_page.locator("body").inner_text())
                if _contains_query_tokens(search_phrase, body):
                    verified = dict(item)
                    verified.pop("match_score", None)
                    verified["version"] = _extract_version_hint(
                        f"{item['title']} {item['url']} {body}"
                    )
                    verified["matched_fragment"] = search_phrase
                    verified["evidence"] = _evidence_excerpt(body, search_phrase)
                    verified_results.append(verified)
            except Exception as exc:
                verification_errors.append(f"{item['url']}: {type(exc).__name__}: {exc}")
            finally:
                detail_page.close()

        ai_mentions_command = _contains_query_tokens(
            search_phrase, str(ai_response.get("text", ""))
        )
        if not results and ai_response.get("state") in {"failed", "generating", "timeout"}:
            return (
                "incomplete",
                [],
                "Cisco ordinary results were empty and the AI Response did not complete.",
                navigation,
                verification_errors,
                ai_response,
            )
        if not results and ai_mentions_command:
            return (
                "ambiguous",
                [],
                "Cisco AI Response mentioned the command but no cited source page was verified.",
                navigation,
                verification_errors,
                ai_response,
            )
        if not results:
            return (
                "not_found",
                results,
                "Cisco official-site search completed without results.",
                navigation,
                verification_errors,
                ai_response,
            )
        if verified_results:
            return (
                "found",
                verified_results,
                "Cisco official-site search found verified command evidence.",
                navigation,
                verification_errors,
                ai_response,
            )
        if verification_errors:
            return (
                "failed",
                [],
                "Cisco result-page verification failed.",
                navigation,
                verification_errors,
                ai_response,
            )
        return (
            "ambiguous",
            [],
            "Cisco search returned pages without verified command evidence.",
            navigation,
            verification_errors,
            ai_response,
        )
    finally:
        page.close()


def _open_cisco_search(page: Any, search_phrase: str) -> str:
    """Open Cisco search without assuming the first responsive search box is visible."""
    page.goto(CISCO_HOME_URL, wait_until="domcontentloaded", timeout=30_000)
    selector = (
        "input[type='search'], input[aria-label*='Search' i], "
        "input[placeholder*='Search' i]"
    )
    search_input = _first_visible_locator(page.locator(selector))
    if search_input is None:
        trigger = _first_visible_locator(
            page.locator(
                "button[aria-label*='Search' i], [role='button'][aria-label*='Search' i]"
            )
        )
        if trigger is not None:
            trigger.click()
            search_input = _first_visible_locator(page.locator(selector))
    if search_input is not None:
        try:
            search_input.fill(search_phrase)
            search_input.press("Enter")
            page.wait_for_load_state("domcontentloaded", timeout=30_000)
            _wait_for_cisco_search_results(page, search_phrase)
            return "home_ui"
        except Exception:
            # Cisco renders hidden desktop/mobile duplicates on some layouts.
            pass
    page.goto(_cisco_search_url(search_phrase), wait_until="domcontentloaded", timeout=30_000)
    _wait_for_cisco_search_results(page, search_phrase)
    return "search_url"


def _cisco_search_url(search_phrase: str) -> str:
    parameters = dict(CISCO_SEARCH_PARAMETERS)
    parameters["query"] = search_phrase
    return f"{CISCO_SEARCH_URL}?{urlencode(parameters)}"


def _wait_for_cisco_search_results(page: Any, search_phrase: str) -> None:
    tokens = _vendor_query_tokens(search_phrase)
    if not tokens:
        return
    try:
        page.wait_for_function(
            """tokens => tokens.every(token =>
                (document.body?.innerText || '').toLowerCase().includes(token)
            )""",
            arg=tokens,
            timeout=5_000,
        )
    except Exception:
        pass


def _first_visible_locator(locator: Any) -> Any | None:
    for candidate in locator.all():
        try:
            if candidate.is_visible() and candidate.is_enabled():
                return candidate
        except Exception:
            continue
    return None


def _vendor_search_phrase(
    query: str,
    contexts: Sequence[Sequence[str]] = (),
) -> str:
    command_tokens = _vendor_query_tokens(query)
    representative_tokens = command_tokens[-4:]
    context_tokens = [
        token for token in _context_tokens(contexts) if token not in representative_tokens
    ][:2]
    tokens = list(dict.fromkeys((*context_tokens, *representative_tokens)))
    return " ".join(tokens) or _clean_text(query)


def _wait_for_cisco_ai_response(page: Any) -> dict[str, Any]:
    try:
        initial_text = _clean_text(page.locator("body").inner_text())
    except Exception as exc:
        return {
            "state": "failed",
            "text": "",
            "version_hints": [],
            "message": f"Unable to read Cisco AI Response: {type(exc).__name__}: {exc}",
        }
    if "ai response" not in initial_text.casefold():
        return {
            "state": "unavailable",
            "text": "",
            "version_hints": [],
            "message": "Cisco AI Response was not present on the search page.",
        }
    try:
        page.wait_for_function(
            r"""() => {
                const text = document.body?.innerText || '';
                const lower = text.toLowerCase();
                const start = lower.indexOf('ai response');
                if (start < 0) return false;
                const end = lower.indexOf('refine results', start);
                const section = text.slice(start, end < 0 ? undefined : end);
                return !/generating(?:\.\.\.)?/i.test(section) && section.length >= 160;
            }""",
            timeout=CISCO_AI_RESPONSE_TIMEOUT_MS,
        )
    except Exception:
        pass
    parsed = _parse_cisco_ai_response(page.locator("body").inner_text())
    if parsed["state"] == "generating":
        parsed["state"] = "timeout"
        parsed["message"] = "Cisco AI Response did not finish before the timeout."
    return parsed


def _parse_cisco_ai_response(body_text: str) -> dict[str, Any]:
    text = _clean_text(body_text)
    lower = text.casefold()
    start = lower.find("ai response")
    if start < 0:
        return {
            "state": "unavailable",
            "text": "",
            "version_hints": [],
            "message": "Cisco AI Response was not present on the search page.",
        }
    end_positions = [
        position
        for marker in ("refine results", "sorted by:")
        if (position := lower.find(marker, start)) >= 0
    ]
    end = min(end_positions) if end_positions else len(text)
    section = text[start + len("ai response") : end].strip()
    section = re.sub(r"^visit faq\s*", "", section, flags=re.I)
    section = re.sub(
        r"^important\.\s*results generated by ai\.\s*"
        r"before using results, verify accuracy and completeness\.\s*",
        "",
        section,
        flags=re.I,
    )
    if re.search(r"\bgenerating(?:\.\.\.)?\b", section, flags=re.I):
        return {
            "state": "generating",
            "text": "",
            "version_hints": [],
            "message": "Cisco AI Response is still generating.",
        }
    answer = section[:CISCO_AI_RESPONSE_MAX_CHARS].strip()
    return {
        "state": "complete" if answer else "unavailable",
        "text": answer,
        "version_hints": list(_extract_version_hints(answer)),
        "message": (
            "Cisco AI Response completed."
            if answer
            else "Cisco AI Response did not contain answer text."
        ),
    }


def _contains_query_tokens(query: str, text: str) -> bool:
    query_tokens = _vendor_query_tokens(query)
    value = text.casefold()
    return bool(query_tokens) and all(token in value for token in query_tokens)


def _search_result_matches(query: str, text: str) -> bool:
    return _search_result_match_score(query, text) > 0


def _search_result_match_score(query: str, text: str) -> int:
    query_tokens = _vendor_query_tokens(query)
    value = text.casefold()
    matched = sum(token in value for token in query_tokens)
    required = 1 if len(query_tokens) == 1 else 2
    return matched if matched >= required else 0


def _vendor_query_tokens(query: str) -> list[str]:
    ignored = {
        "address-family",
        "asr",
        "asr9k",
        "cisco",
        "cisco.com",
        "config",
        "configuration",
        "global",
        "interface",
        "ios",
        "ios-xr",
        "router",
        "site",
        "unicast",
        "view",
        "xr",
        "xrv",
        "xrv9k",
    }
    return [
        token
        for token in _literal_tokens(query)
        if (
            token
            and token not in ignored
            and not token.startswith("site:")
            and not re.fullmatch(r"\d{4}", token)
        )
    ]


def _evidence_excerpt(text: str, search_phrase: str, limit: int = 1_200) -> str:
    value = _clean_text(text)
    lowered = value.casefold()
    position = next(
        (
            lowered.find(token)
            for token in reversed(_vendor_query_tokens(search_phrase))
            if lowered.find(token) >= 0
        ),
        0,
    )
    start = max(0, position - limit // 3)
    return value[start : start + limit]


def _extract_version_hint(text: str) -> str:
    versions = _extract_version_hints(text)
    return versions[0] if versions else ""


def _extract_version_hints(text: str) -> tuple[str, ...]:
    versions: list[str] = []
    explicit_patterns = (
        r"\b(?:cisco\s+)?ios(?:\s+|-)xr(?:\s+(?:software\s+)?(?:release|version))?\s+"
        r"(\d+\.\d+(?:\.\d+)?)",
        r"\b(?:release|version)\s+[rv]?\s*(\d+\.\d+(?:\.\d+)?)",
    )
    for pattern in explicit_patterns:
        versions.extend(match.group(1) for match in re.finditer(pattern, text, flags=re.I))
    for match in re.finditer(r"(?:^|[/_-])r(\d+)-(\d+)(?:-(\d+))?(?=$|[/_.-])", text, flags=re.I):
        versions.append(".".join(part for part in match.groups() if part is not None))
    for match in re.finditer(r"(?:^|[/_-])(\d)(\d)x(?=$|[/_.-])", text, flags=re.I):
        versions.append(f"{match.group(1)}.{match.group(2)}")
    return tuple(dict.fromkeys(versions))


def _manual_block_summary(
    block: ManualCommandBlock,
    *,
    include_evidence: bool = False,
) -> dict[str, Any]:
    result = {
        "block_id": block.block_id,
        "title": block.title,
        "command_name": block.command_name,
        "url": block.url,
        "source_role": block.source_role,
        "source_version": block.source_version,
        "is_target_version": block.is_target_version,
        "syntax_templates": list(block.syntax_templates),
        "modes": list(block.modes),
    }
    if include_evidence:
        result["evidence"] = [to_jsonable(item) for item in block.evidence]
    return result


def ast_syntax_diff_impl(
    probed_template: str,
    manual_syntax: str,
) -> dict[str, Any]:
    manual_valid = _valid_template_syntax(manual_syntax)
    if not manual_valid:
        return {
            "valid_syntax": False,
            "syntax_error": True,
            "message": "Manual syntax failed structural/bracket validation (A1 Candidate)",
        }

    probe_valid = _valid_template_syntax(probed_template)
    match_found = False
    if manual_valid and probe_valid:
        try:
            probe_variants = _expand_template(probed_template)
            manual_variants = _expand_template(manual_syntax)
            common = set(probe_variants).intersection(set(manual_variants))
            match_found = len(common) > 0
        except Exception:
            match_found = False

    return {
        "valid_syntax": True,
        "syntax_error": False,
        "probe_valid": probe_valid,
        "syntax_match": match_found,
        "manual_syntax": manual_syntax,
        "probed_template": probed_template,
    }
