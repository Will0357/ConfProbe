import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import networkx as nx

import probe
from probe import (
    ConfProbe,
    _add_recurrence_edge_if_acyclic,
    _field_signature,
    _find_composition_cover,
    _get_view_reentry_path,
    _matches_permutation_prune,
)
from utils.dag_algorithm import graph2graphml


class CompositionPruneTest(unittest.TestCase):
    def node(self, graph, node_id, label, successors=None):
        attributes = {"label": label}
        if successors is not None:
            attributes["succ"] = set(successors)
        graph.add_node(node_id, **attributes)

    def test_same_label_and_covered_successors_matches(self):
        graph = nx.DiGraph()
        self.node(graph, "curr", "<WORD>", {"bit-position", "END"})
        self.node(graph, "view", "<WORD>", {"bit-position", "END", "color"})

        self.assertEqual("view", _find_composition_cover(graph, "curr", ("view",)))

    def test_end_difference_prevents_composition_prune(self):
        graph = nx.DiGraph()
        self.node(graph, "curr", "<WORD>", {"bit-position", "END"})
        self.node(graph, "view", "<WORD>", {"bit-position"})

        self.assertIsNone(_find_composition_cover(graph, "curr", ("view",)))

    def test_different_placeholder_labels_do_not_match(self):
        graph = nx.DiGraph()
        self.node(graph, "curr", "<WORD>", {"END"})
        self.node(graph, "view", "<A.B.C.D>", {"END"})

        self.assertIsNone(_find_composition_cover(graph, "curr", ("view",)))

    def test_any_same_label_view_child_can_cover_current_successors(self):
        graph = nx.DiGraph()
        self.node(graph, "curr", "metric", {"value", "END"})
        self.node(graph, "partial", "metric", {"value"})
        self.node(graph, "cover", "metric", {"value", "END", "color"})

        self.assertEqual(
            "cover",
            _find_composition_cover(graph, "curr", ("partial", "cover")),
        )

    def test_missing_or_removed_nodes_are_not_comparable(self):
        graph = nx.DiGraph()
        self.node(graph, "curr", "metric", {"END"})
        self.node(graph, "missing-succ", "metric")

        self.assertIsNone(
            _find_composition_cover(graph, "curr", ("missing-succ", "gone"))
        )
        self.assertIsNone(_find_composition_cover(graph, "gone", ("missing-succ",)))


class PermutationPruneSignatureTest(unittest.TestCase):
    def test_different_descriptions_do_not_match(self):
        into = frozenset({
            _field_signature("level-1", "Inter-area routes into level-1"),
            _field_signature("level-2", "Inter-area routes into level-2"),
        })
        source = frozenset({
            _field_signature("level-1", "Inter-area routes from level-1"),
            _field_signature("level-2", "Inter-area routes from level-2"),
            _field_signature("metric", "Metric"),
        })

        self.assertFalse(
            _matches_permutation_prune(
                into,
                source,
                _field_signature("level-1", "Inter-area routes into level-1"),
                _field_signature("redistribute", "Redistribute routes"),
                _field_signature("END", "<cr>"),
            )
        )

    def test_identical_signatures_can_match(self):
        siblings = frozenset({
            _field_signature("level-1", "Inter-area routes"),
            _field_signature("level-2", "Inter-area routes"),
        })
        ancestor = siblings | {_field_signature("metric", "Metric")}

        self.assertTrue(
            _matches_permutation_prune(
                siblings,
                ancestor,
                _field_signature("level-1", "Inter-area routes"),
                _field_signature("redistribute", "Redistribute routes"),
                _field_signature("END", "<cr>"),
            )
        )


class ViewRollbackTest(unittest.TestCase):
    def test_reentry_path_replays_each_view_below_the_fallback(self):
        view_path = (
            ("[config]", ""),
            ("[config-if-range]", "interface range GigabitEthernet0/0 "),
            ("[config-router]", "router bgp 1 "),
        )

        self.assertEqual(
            view_path[1:],
            _get_view_reentry_path(view_path, "[config]"),
        )

    def test_current_or_unknown_view_is_not_a_rollback(self):
        view_path = (
            ("[config]", ""),
            ("[config-if-range]", "interface range GigabitEthernet0/0 "),
        )

        self.assertIsNone(_get_view_reentry_path(view_path, "[config-if-range]"))
        self.assertIsNone(_get_view_reentry_path(view_path, "[config-router]"))

    def test_ancestor_fallback_keeps_the_field_as_a_terminal(self):
        class FallbackImage:
            END = '<cr>'
            vendor = 'Test'

            def __init__(self):
                self.conn = Mock()
                self.views = iter((
                    '[config]',
                    '[config-if-range]',
                    '[config]',
                    '[config-if-range]',
                ))
                self.completed = []

            def get_view(self):
                return next(self.views)

            def search_command(self, cmd):
                return cmd

            def detect_error(self, echo):
                return False

            def echo2dict(self, echo, templ):
                branches = {
                    'interface range ': {'END': self.END},
                    '': {'bgp-policy': 'BGP policy settings'},
                    'bgp-policy ': {'accounting': 'BGP policy accounting'},
                    'bgp-policy accounting ': {'END': self.END},
                }
                return echo, dict(branches[templ])

            def if_send(self, templ):
                return True

            def process_complete_cmd(self, cmd):
                self.completed.append(cmd)

            def into_last_view(self, cmd, view):
                pass

            def restore_input(self, command, branch_input):
                pass

            def recover_prompt(self):
                return True

            def get_instance(self, branch, desc, space):
                return branch, branch, space

        image = FallbackImage()
        model = object.__new__(ConfProbe)
        model.img = image
        model.file_name = 'rollback'

        with tempfile.TemporaryDirectory() as directory:
            previous_directory = os.getcwd()
            try:
                os.chdir(directory)
                with patch.object(probe, 'COMMAND', 'interface range'), patch.object(
                    probe, 'PRODUCT', 'rollback-test'
                ), patch.object(probe, 'MGEND', False), patch('builtins.print'):
                    model.probe_graph()
            finally:
                os.chdir(previous_directory)

        accounting = next(
            node for node, data in model.G.nodes(data=True)
            if data['label'] == 'accounting'
        )
        self.assertEqual(
            ['END'],
            [model.G.nodes[node]['label'] for node in model.G.successors(accounting)],
        )
        self.assertEqual(['interface range '], image.completed)
        image.conn.write_channel.assert_called_once_with('bgp-policy accounting ')


class ParseFailureRecoveryTest(unittest.TestCase):
    def test_bad_branch_is_removed_and_siblings_continue(self):
        class ParseFailureImage:
            END = '<cr>'
            vendor = 'Test'

            def __init__(self):
                self.conn = Mock()
                self.recoveries = 0

            def get_view(self):
                return '[config]'

            def search_command(self, command):
                return command

            def detect_error(self, echo):
                return False

            def echo2dict(self, echo, templ):
                if templ == 'root ':
                    return echo, {
                        'bad': 'Malformed branch',
                        'good': 'Healthy branch',
                    }
                if templ == 'root bad ':
                    raise IndexError('orphan continuation')
                if templ == 'root good ':
                    return echo, {'END': self.END}
                raise AssertionError(f'unexpected template: {templ}')

            def if_send(self, templ):
                return False

            def get_instance(self, branch, desc, space):
                return branch, branch, space

            def recover_prompt(self):
                self.recoveries += 1
                return True

            def restore_input(self, command, branch_input):
                pass

            def process_complete_cmd(self, command):
                pass

        image = ParseFailureImage()
        model = object.__new__(ConfProbe)
        model.img = image
        model.file_name = 'parse-failure'

        with tempfile.TemporaryDirectory() as directory:
            previous_directory = os.getcwd()
            try:
                os.chdir(directory)
                with patch.object(probe, 'COMMAND', 'root'), patch.object(
                    probe, 'PRODUCT', 'parse-test'
                ), patch.object(probe, 'MGEND', False), patch('builtins.print'):
                    model.probe_graph()
            finally:
                os.chdir(previous_directory)

        labels = [data['label'] for _, data in model.G.nodes(data=True)]
        self.assertNotIn('bad', labels)
        self.assertIn('good', labels)
        self.assertEqual(1, model.count['parse'])
        self.assertEqual(1, image.recoveries)

        root_node = next(
            node for node, data in model.G.nodes(data=True) if data['label'] == 'root'
        )
        self.assertTrue(model.G.nodes[root_node]['probe_failed'])
        self.assertTrue(model.G.nodes[root_node]['parse_failed'])
        self.assertEqual('bad', model.G.nodes[root_node]['parse_branch'])
        self.assertEqual('root bad ', model.G.nodes[root_node]['parse_template'])


class CycleHandlingTest(unittest.TestCase):
    def cycle_graph(self):
        graph = nx.DiGraph()
        graph.add_node("from", label="from")
        graph.add_node("into", label="into")
        graph.add_edge("from", "into")
        graph.add_edge("into", "from")
        return graph

    def test_recurrence_edge_that_closes_cycle_is_rejected(self):
        graph = nx.DiGraph()
        graph.add_edges_from((
            ("from", "from-leaf"),
            ("into", "into-leaf"),
        ))

        self.assertTrue(_add_recurrence_edge_if_acyclic(graph, "from-leaf", "into"))
        self.assertFalse(_add_recurrence_edge_if_acyclic(graph, "into-leaf", "from"))
        self.assertFalse(graph.has_edge("into-leaf", "from"))
        self.assertTrue(nx.is_directed_acyclic_graph(graph))

    def test_graphml_export_reports_cycle_without_mutating_graph(self):
        graph = self.cycle_graph()
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "cycle.graphml"
            with self.assertRaisesRegex(ValueError, "from.*into.*from"):
                graph2graphml(graph, output)

            self.assertFalse(output.exists())
            self.assertTrue(graph.has_edge("from", "into"))
            self.assertTrue(graph.has_edge("into", "from"))

    def test_graphml_load_reports_cycle_without_mutating_input(self):
        graph = self.cycle_graph()
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "cycle.graphml"
            nx.write_graphml_lxml(graph, source)

            with self.assertRaisesRegex(ValueError, "from.*into.*from"):
                ConfProbe(source)


if __name__ == "__main__":
    unittest.main()
