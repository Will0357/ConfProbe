from evengsdk.client import EvengClient
import time
import threading
import os
import re
import networkx as nx
import subprocess
import datetime
import copy
import json
from dataclasses import dataclass, replace
from typing import List, Callable, Any
from collections import Counter, defaultdict
from functools import partial

from utils.eve_drivers import *
import utils.dag_algorithm as dag

"""
comb: combination pruning
perm: permutation pruning
comp: composition pruning
loop: nontemination pruning
alt: selected branches merge
opt: optional branches merge
"""



@dataclass(slots=True)
class _ProbeState:
    curr: Any
    input_text: str = ''
    cmd: str = ''
    templ: str = ''
    prune_root: Any = None
    merge_root: Any = None
    combi_root: Any = None
    view: str = ''
    view_path: tuple[tuple[str, str], ...] = ()
    level: int = 0


def _find_composition_cover(graph: nx.DiGraph, curr, view_children):
    """Return a same-label view child whose direct successors cover curr."""
    if curr not in graph:
        return None

    curr_label = graph.nodes[curr].get('label')
    curr_successors = graph.nodes[curr].get('succ')
    if not isinstance(curr_successors, set):
        return None

    for view_child in view_children:
        if view_child not in graph:
            continue
        if graph.nodes[view_child].get('label') != curr_label:
            continue
        view_successors = graph.nodes[view_child].get('succ')
        if isinstance(view_successors, set) and curr_successors <= view_successors:
            return view_child

    return None


def _get_view_reentry_path(view_path, current_view):
    """Return the commands needed to re-enter a view after an ancestor fallback."""
    for index in range(len(view_path) - 2, -1, -1):
        if view_path[index][0] == current_view:
            return view_path[index + 1:]
    return None


def _field_signature(field, desc):
    """Identify a help field by its token and its unmodified description."""
    return field, desc


def _matches_permutation_prune(
    sibling_signatures,
    ancestor_signatures,
    current_signature,
    ancestor_signature,
    end_signature,
):
    """Return whether a sibling level is a strict permutation-prune subset."""
    return (
        sibling_signatures != ancestor_signatures
        and current_signature in ancestor_signatures
        and sibling_signatures < ancestor_signatures | {ancestor_signature, end_signature}
    )


def _add_recurrence_edge_if_acyclic(graph: nx.DiGraph, leaf, successor) -> bool:
    """Add a recurrence dependency only when it preserves the DAG invariant."""
    if leaf == successor or nx.has_path(graph, successor, leaf):
        return False

    graph.add_edge(leaf, successor)
    return True


subg_dict = {}

class ConfProbe():
    DEVICE_FACTORIES = {
        'arv': ArvModel,
        'arv2': partial(ArvModel, 'AR1000v2'),
        'xrv': XrvModel,
        'xrv2': partial(XrvModel, 'xrv2'),
        'xrv3': partial(XrvModel, 'xrv3'),
        'csr': CsrModel,
        'csr2': partial(CsrModel, 'CSR2'),
        'csr3': partial(CsrModel, 'CSR3'),
        'iol': partial(IosModel, 'R'),
        'iol2': partial(IosModel, 'R2'),
        'iol3': partial(IosModel, 'R3'),
        'xrv9k': Xrv9kModel,
        'cRPD': cRPDModel,
        'cRPD2': partial(cRPDModel, 'cRPD2'),
    }

    def __init__(self, path=None):
        root_cmd = COMMAND
        self.file_name = root_cmd.replace(' ', '_').replace('/', '') if root_cmd else 'ROOT'
        if path:
            self.G: nx.DiGraph = nx.read_graphml(path)
            for node, data in self.G.nodes(data=True):
                if 'recur' in data:
                    parts = data['recur'].split(';')
                    self.G.nodes[node]['recur'] = set(parts)

            if not nx.is_directed_acyclic_graph(self.G):
                raise ValueError(
                    f"cycle detected while loading GraphML: "
                    f"{dag.describe_cycle(self.G)}"
                )


            dir = os.path.dirname(os.path.abspath(path))
            self.fld_svg_path = f"{dir}/{self.file_name}_ConfigG.svg"
            self.tmpl_svg_path = f"{dir}/{self.file_name}_DSL.svg"
            self.tmpl_svg_simple_path = f"{dir}/{self.file_name}_DSLsimple.svg"
            self.tmpl_log_path = f"{dir}/{self.file_name}_DSL.log"
            self.tmpl_json_path = f"{dir}/{self.file_name}_DSL.json"

            node_count = len(self.G.nodes)
            end_count = len({n for n, d in self.G.out_degree() if d == 0})
            viw_count = len({n for n in self.G.nodes if re.search(r'\[.*?\]', dag.label(self.G, n))})
            nfd_count = node_count - end_count - viw_count
            print(f"Normal Field: {nfd_count}, View Count: {viw_count}, End Count: {end_count}")

        else:
            try:
                self.img = self.DEVICE_FACTORIES[PRODUCT]()
            except KeyError:
                raise ValueError(f'Unexpected Device: {PRODUCT}') from None

        self.stop_count = 0
        self.count = Counter()
        self.timer = defaultdict(float)

    

    def label(self, node) -> str:
        return self.G.nodes[node]['label']


    def log_graph_info(self, info: str=None):
        with open(PROBE_FILE, 'a', encoding='utf-8') as log_file:
            if not info:
                current_time = datetime.datetime.now()
                timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S") 
                timestamp = f"\n[{timestamp}]\n"
                log_file.write(timestamp)
                log_file.write(f"PRODUCT:{PRODUCT}, COMMAND:{COMMAND}, MAX_NODES:{MAX_NODES}, MAX_BRANCHES:{MAX_BRANCHES}\n")
                log_file.write(f"ABLATION: {ABLAT}, CROSS:{CROSS}, MODE:{'Load' if GRAPH_PATH else 'Probe'}\n")
                log_file.write(self.get_pathnum_depth_outdgree())
            else:
                log_file.write(f"{info}\n")
                
    def get_pathnum_depth_outdgree(self):
        g = self.G
        root = [node for node in g.nodes() if g.in_degree(node) == 0][0]
        depths = nx.single_source_shortest_path_length(g, root)
        total_depth = sum(depths.values()) - depths[root]  # 减去根节点的深度0
        num_nodes_excluding_root = len(depths) - 1
        average_depth = total_depth / num_nodes_excluding_root if num_nodes_excluding_root > 0 else 0

        non_leaf_nodes = [node for node in g.nodes() if g.out_degree(node) > 0]
        if non_leaf_nodes:
            total_out_degree = sum(g.out_degree(node) for node in non_leaf_nodes)
            average_branching_factor = total_out_degree / len(non_leaf_nodes)
        else:
            average_branching_factor = 0  # 如果图只有根节点一个点

        def count_root_to_leaf_paths(G: nx.DiGraph) -> int:
            cnt = {n: 0 for n in G.nodes}
            cnt[root] = 1
            total = 0
            for u in nx.topological_sort(G):
                if G.out_degree(u) == 0:
                    total += cnt[u]
                else:
                    for v in G.successors(u):
                        cnt[v] += cnt[u]
            return total
        pathnum = count_root_to_leaf_paths(g)
    

        print(f"pathnum:{pathnum} average depth:{average_depth} average out-degree:{average_branching_factor}")
        return f"pathnum:{pathnum} average depth:{average_depth} average out-degree:{average_branching_factor}\n"

    def probe_graph(self):
        """
        Probing ConfigG rooted at given root_cmd
        
        :param self: Description
        :param root_cmd: Startup command prefix of Probing
        :type cmd_segment: str
        """
        self.count = Counter()
        self.timer = defaultdict(float)
        count = self.count
        timer = self.timer
        successor_signatures = {}

        def write_file(content: str, level: int, mode: str='log'):
            # os.makedirs(os.path.dirname(file_path), exist_ok=True) 
            if mode == 'log':
                with open(self.log_path, '+a', encoding='utf-8') as f:
                    f.write(f"{'    '*level}{content}")
            else:
                raise ValueError('Unexpected Type')
    
        def label(node) -> str:
            return self.G.nodes[node]['label']

        def _try_repetition_prune(state: _ProbeState, fields, ancestors) -> bool:
            curr = state.curr
            t0 = time.time()
            timed = False
            try:
                if not REPET_CHECK:
                    return False

                recur_list = []
                loop_count = 1
                for a in reversed(ancestors):
                    if self.G.nodes[a]['succ'] == fields and self.G.nodes[a]['desc'] == self.G.nodes[curr]['desc']:
                        recur_list.append(a)
                        loop_count += 1
                        if loop_count >= MAX_LOOP:
                            recur_ance = recur_list[1]
                            self.G.remove_nodes_from(nx.descendants(self.G, recur_ance))
                            self.G.nodes[recur_ance]['prune'] = 'repetition'

                            timer['repe'] += time.time() - t0
                            timed = True
                            count['repe'] += 1
                            write_file(f"♻️Infinite Repetition: {state.templ}[{label(recur_ance)} - {fields}]...\n", state.level)
                            return True

                return False
            finally:
                if not timed:
                    timer['repe'] += time.time() - t0

        def _try_permutation_prune(
            state: _ProbeState,
            pred,
            curr_fld,
            fields,
            branches,
            branch_signatures,
            ancestors,
        ) -> bool:
            curr = state.curr
            t0 = time.time()
            timed = False
            try:
                if not (PERMU_CHECK and pred in successor_signatures):
                    return False

                # For test:
                # if 'redistribute' not in state.templ and self.img.vendor == 'Cisco':
                #     return False

                traverse = True
                if self.img.vendor == 'Juniper':
                    if re.match(r"> .*", self.G.nodes[curr]['desc']):  # recurrent container
                        pass
                    elif all(not re.match(r"> .*", s_desc) for s_desc in branches.values()):
                        new_ance = [curr]
                        for a in reversed(ancestors[:-1]):
                            if not 'desc' in self.G.nodes[a]:
                                traverse = False
                                break
                            new_ance.append(a)
                            if re.match(r"> .*", self.G.nodes[a]['desc']):
                                ancestors = list(reversed(new_ance))         # traverse leaves with a container
                                break

                if traverse == True:
                    # samelvl_flds = self.G.nodes[pred]['succ']
                    samelvl_signatures = successor_signatures[pred]
                    current_signature = _field_signature(
                        curr_fld,
                        self.G.nodes[curr].get('desc', ''),
                    )
                    remove = False
                    if len(samelvl_signatures) > 1:
                        for ind, a in enumerate(reversed(ancestors[:-1])):
                            ancestor_signatures = successor_signatures.get(a)
                            if ancestor_signatures is None:
                                continue

                            if _matches_permutation_prune(
                                samelvl_signatures,
                                ancestor_signatures,
                                current_signature,
                                _field_signature(label(a), self.G.nodes[a].get('desc', '')),
                                _field_signature('END', self.img.END),
                            ):
                                remove = True
                                # if self.img.vendor != 'Juniper':
                                #     node = ancestors[len(ancestors) - ind - 1]
                                #     if 'recur' in self.G.nodes[node]:
                                #         self.G.nodes[node]['recur'] |= samelvl_flds
                                #         self.G.nodes[node]['recur_end'] |= {pred}
                                #     else:
                                #         self.G.nodes[node]['recur'] = set(samelvl_flds)
                                #         self.G.nodes[node]['recur_end'] = {pred}
                                break

                        if remove:
                            self.G.nodes[pred]['prune'] = 'permutation'
                            self.G.remove_node(curr)
                            timer['perm'] += time.time() - t0
                            timed = True
                            count['perm'] += 1
                            write_file(f"✂️Sucpicious Permutation: {state.templ}...\n", state.level)
                            return True

                return False
            finally:
                if not timed:
                    timer['perm'] += time.time() - t0

        def _try_combination_prune(state: _ProbeState, pred, curr_fld, fields) -> bool:
            curr = state.curr
            combi_root = state.combi_root
            t0 = time.time()
            timed = False
            try:
                if not (COMBI_CHECK and combi_root and 'succ' in self.G.nodes[pred]):
                    return False

                samelvl_flds = self.G.nodes[pred]['succ'] - {curr_fld}
                merged_id1 = dag.merge_to_equivalent(self.G, combi_root, curr, fields, samelvl_flds)
                if merged_id1:
                    self.G.remove_node(curr)
                    self.G.add_edge(pred, merged_id1)
                    self.G.nodes[pred]['prune'] = 'combination'

                    timer['comb'] += time.time() - t0
                    timed = True
                    count['comb'] += 1
                    write_file(f"📚Branch Combination: {state.templ}[{label(merged_id1)}]\n", state.level)
                    return True

                return False
            finally:
                if not timed:
                    timer['comb'] += time.time() - t0

        def _process_terminal(state: _ProbeState, branches):
            succ_end = None
            isolate = False
            composition_children = ()

            write_file(f"{state.templ} - {time.time()-timer['start']}\n", state.level)
            t0 = time.time()
            del branches['END']

            if self.img.if_send(state.templ):
                try:
                    current_view = self.img.get_view()
                except (ReadTimeout, OSError, ValueError) as exc:
                    message = f"{type(exc).__name__}: {exc}".splitlines()[0]
                    self.G.nodes[state.curr]['probe_failed'] = True
                    self.G.nodes[state.curr]['error'] = f"view ({message})"
                    self.img.recover_prompt()
                    write_file(
                        f"(! View recovery failed: {state.cmd} {{{message}}}\n",
                        state.level,
                    )
                    return state, None, True, composition_children

                reentry_path = _get_view_reentry_path(state.view_path, current_view)
                if reentry_path is not None:
                    try:
                        for expected_view, entry_cmd in reentry_path:
                            self.img.process_complete_cmd(entry_cmd)
                            restored_view = self.img.get_view()
                            if restored_view != expected_view:
                                raise ValueError(
                                    f"Unable to restore {expected_view}; reached {restored_view}."
                                )
                        self.img.conn.write_channel(state.cmd)
                    except (ReadTimeout, OSError, ValueError) as exc:
                        message = f"{type(exc).__name__}: {exc}".splitlines()[0]
                        self.G.nodes[state.curr]['probe_failed'] = True
                        self.G.nodes[state.curr]['error'] = f"view ({message})"
                        self.img.recover_prompt()
                        write_file(
                            f"(! View rollback restore failed: {state.cmd} {{{message}}}\n",
                            state.level,
                        )
                        return state, None, True, composition_children

                    write_file(f"({state.view}) <- ({current_view})\n", state.level, 'log')
                    succ_end = dag.add_node_edge(self.G, state.curr, 'END')
                elif state.view != current_view:
                    level = state.level
                    timer['graph_view'] += time.time() - t0
                    t0 = time.time()
                    succ_view = dag.add_node_edge(self.G, state.curr, f"{current_view}")
                    view_state = _ProbeState(
                        curr=succ_view,
                        view=current_view,
                        view_path=state.view_path + ((current_view, state.cmd),),
                        level=level + 1,
                    )
                    timer['graph'] += time.time() - t0
                    write_file(f"({state.view}) ➡️ ({current_view})\n", level, 'log')

                    isolate = probe_recursive(view_state)
                    if succ_view in self.G:
                        view_nodes = {succ_view} | nx.descendants(self.G, succ_view)
                        view_probe_failed = any(
                            self.G.nodes[node].get('probe_failed')
                            for node in view_nodes
                            if node in self.G
                        )
                    else:
                        view_probe_failed = True
                    t0 = time.time()
                    restore_succeeded = True
                    try:
                        self.img.into_last_view(state.cmd, state.view)
                    except (ReadTimeout, OSError, ValueError) as exc:
                        message = f"{type(exc).__name__}: {exc}".splitlines()[0]
                        self.G.nodes[state.curr]['probe_failed'] = True
                        self.G.nodes[state.curr]['error'] = f"view ({message})"
                        self.img.recover_prompt()
                        write_file(
                            f"(! View restore failed: {state.cmd} {{{message}}}\n",
                            state.level,
                        )
                        restore_succeeded = False
                        isolate = True
                    if restore_succeeded and not view_probe_failed:
                        composition_children = tuple(self.G.successors(succ_view))
                    state = replace(
                        state,
                        prune_root=None,
                        merge_root=None,
                        combi_root=None,
                    )
                    timer['graph_view'] += time.time() - t0
                else:
                    self.img.process_complete_cmd(state.cmd)
                    timer['graph_view'] += time.time() - t0
                    succ_end = dag.add_node_edge(self.G, state.curr, 'END')
            else:
                timer['graph'] += time.time() - t0

            return state, succ_end, isolate, composition_children

        def _probe_successors(state: _ProbeState, branches, isolate, composition_children):
            successors = []
            branch_items = list(branches.items())
            for field, desc in branch_items:
                t0 = time.time()
                space = ' '
                instance, new_branch, space = self.img.get_instance(field, desc, space)
                new_templ = state.templ + new_branch + space
                timer['cmd'] += time.time() - t0
                t0 = time.time()

                succ = dag.add_node_edge(self.G, state.curr, new_branch)
                self.G.nodes[succ]['desc'] = desc
                successors.append(succ)

                child_state = replace(
                    state,
                    curr=succ,
                    input_text=instance + space,
                    templ=new_templ,
                    prune_root=state.prune_root if state.prune_root else succ,
                    merge_root=state.merge_root if state.merge_root else succ,
                    combi_root=state.combi_root if state.combi_root else succ,
                )

                timer['graph_add'] += time.time() - t0

                isolate = probe_recursive(child_state)
                t0 = time.time()

                # IOS has one global BGP process.  Remove the process created
                # for this ASN sample before probing the next ASN syntax.
                if self.img.vendor == 'Cisco' and state.cmd.strip() == 'router bgp':
                    process_cmd = f'{state.cmd}{child_state.input_text}'.strip()
                    self.img.remove_bgp_process(process_cmd)

                # Rebuild the exact parent prefix after all branch cleanup.
                # This is important when asynchronous output has polluted the
                # terminal input line.
                self.img.restore_input(state.cmd, child_state.input_text)

                if self.img.vendor == 'Huawei':
                    if state.templ == 'bgp ' and state.view == '[Huawei]':
                        self.img.conn.write_channel('\x08' * 4)
                        self.img.conn.send_command(f'undo bgp', 'Y/N')
                        self.img.conn.send_command('Y', ']')
                        self.img.conn.write_channel('bgp ')

                if state.curr not in self.G:
                    timer['graph'] += time.time() - t0
                    return successors, state, True

                if COMPO_CHECK and composition_children:
                    cover = _find_composition_cover(self.G, succ, composition_children)
                    if cover is not None and succ in self.G:
                        curr_successors = self.G.nodes[succ]['succ']
                        view_successors = self.G.nodes[cover]['succ']
                        self.G.nodes[state.curr]['prune'] = 'composition'
                        self.G.remove_node(succ)
                        successors.remove(succ)
                        write_file(
                            f"(Composition Prune: {new_branch} "
                            f"{sorted(curr_successors)} <= {sorted(view_successors)})\n",
                            state.level,
                        )
                        count['comp'] += 1
                        timer['comp'] += time.time() - t0
                        timer['graph'] += time.time() - t0
                        continue

                if 'prune' in self.G.nodes[state.curr]:
                    prune_type = self.G.nodes[state.curr]['prune']
                    if prune_type == 'repetition' or prune_type == 'permutation':
                        timer['graph'] += time.time() - t0
                        break

                if isolate:
                    state = replace(state, merge_root=None, combi_root=None)
                timer['graph'] += time.time() - t0

            return successors, state, False

        def _connect_recurrence_dependencies(state: _ProbeState, successors):
            t0 = time.time()
            successors = [s for s in successors if s in self.G]
            if state.prune_root and any('recur' in self.G.nodes[s] for s in successors):
                recur_dict = {n: self.G.nodes[n]['recur'] for n in successors if 'recur' in self.G.nodes[n]}

                for p, recur_p in recur_dict.items():
                    for succ in set(successors)-{p}:
                        recur_s = recur_dict[succ] if succ in recur_dict else set()
                        if recur_p >= recur_s|{label(succ)} and p not in recur_s:
                            leaves = {l for l in self.G.nodes[p]['recur_end'] if l in self.G}
                            added = 0
                            for leaf in leaves:
                                if _add_recurrence_edge_if_acyclic(self.G, leaf, succ):
                                    added += 1
                                else:
                                    write_file(
                                        f'(Skip cyclic recurrence dependency: '
                                        f'"{label(leaf)}" -> "{label(succ)}")\n',
                                        state.level,
                                    )

                            if added:
                                write_file(f'(👬Add Dependancies from "{label(p)}\'s leaves" to "{label(succ)}")\n', state.level)
                                count['succ'] += added
                for k in recur_dict.keys():
                    del self.G.nodes[k]['recur']
            timer['succ'] += time.time() - t0

        def _merge_branch_leaves(state: _ProbeState, curr_fld, succ_end):
            t0 = time.time()
            if MGEND and self.img.vendor != 'Juniper':
                if state.curr == state.merge_root:
                    merged_num = dag.merge_end_alter_lca(self.G, state.merge_root, MAX_NODES, succ_end)
                    if merged_num != 0:
                        write_file(f"Form {{}}s after {curr_fld}\n", state.level)
                        count['end'] += merged_num
            timer['end'] += time.time() - t0

        def probe_recursive(state: _ProbeState):
            """
            Recursively probe the next available field from the current state.
            """
            t0 = time.time()

            # 【input ？to get next fields】
            state = replace(state, cmd=state.cmd + state.input_text)
            isolate = False
            curr = state.curr
            pred = list(self.G.pred[curr])[0]
            ancestors = nx.shortest_path(self.G, state.prune_root, curr)[:-1] if state.prune_root else []
            curr_fld = label(curr)
            timer['graph'] += time.time() - t0

            t0 = time.time()
            try:
                echo = self.img.search_command(state.input_text)
            except (ReadTimeout, OSError, ValueError) as exc:
                message = f"{type(exc).__name__}: {exc}".splitlines()[0]
                self.G.nodes[pred]['probe_failed'] = True
                self.G.nodes[pred]['error'] = f"{curr_fld} ({message})"
                if curr in self.G:
                    self.G.remove_node(curr)
                timer['probe'] += time.time() - t0
                print(f'! Probe recovery failed: {state.cmd} ({message})')
                write_file(
                    f"(! Probe recovery failed: {state.cmd} {{{message}}}\n",
                    state.level,
                )
                return False
            count['probe'] += 1
            timer['probe'] += time.time() - t0            

            # 0) Detect Error/Invalid command
            t0 = time.time()
            if self.img.detect_error(echo):
                self.G.nodes[pred]['error'] = curr_fld
                self.G.remove_node(curr)
                timer['probe'] += time.time() - t0
                print(f'! Error: {state.cmd}')
                write_file(f'(❌Invalid Field: {state.cmd}{{{curr_fld}}}\n', state.level)
                return False
            else:
                try:
                    echo, branches = self.img.echo2dict(echo, state.templ)
                except (IndexError, ValueError) as exc:
                    message = f"{type(exc).__name__}: {exc}".splitlines()[0]
                    parent = self.G.nodes.get(pred)
                    if parent is not None:
                        parent['probe_failed'] = True
                        parent['parse_failed'] = True
                        parent['parse_error'] = message
                        parent['parse_branch'] = curr_fld
                        parent['parse_template'] = state.templ
                    count['parse'] += 1
                    recovered = self.img.recover_prompt()
                    if curr in self.G:
                        self.G.remove_node(curr)
                    timer['probe'] += time.time() - t0
                    recovery_note = '' if recovered else '; prompt recovery failed'
                    print(f'! Parse failed: {state.templ} ({message}{recovery_note})')
                    write_file(
                        f'(! Parse failed: {state.templ} {{{message}{recovery_note}}}\n',
                        state.level,
                    )
                    return False
                # For bgp test
                # if state.cmd == 'router bgp ' and '<1-4294967295>' in branches.keys():
                #     if 'Autonomous system number' in branches['<1-4294967295>']:
                #         del branches['<1-4294967295>']
                fields = set(branches.keys())
                branch_signatures = frozenset(
                    _field_signature(field, desc) for field, desc in branches.items()
                )
                timer['probe'] += time.time() - t0
            
            if state.prune_root:
                if _try_repetition_prune(state, fields, ancestors):
                    return False
                if _try_permutation_prune(
                    state,
                    pred,
                    curr_fld,
                    fields,
                    branches,
                    branch_signatures,
                    ancestors,
                ):
                    return False
                if _try_combination_prune(state, pred, curr_fld, fields):
                    return False

            
            # process each successor
            t0 = time.time()
            self.G.nodes[curr]['succ'] = fields 
            successor_signatures[curr] = branch_signatures
            succ_end = None                         # succ that is end
            composition_children = ()
            if len(fields) > MAX_BRANCHES:          # Change prune and merge scope, the branch point support merge leaves but not regular prune
                state = replace(
                    state,
                    merge_root=curr if state.merge_root else None,
                    combi_root=None,
                )
            timer['graph'] += time.time() - t0
            
            if 'END' in branches.keys():    
                state, succ_end, isolate, composition_children = _process_terminal(state, branches)
                if self.G.nodes.get(state.curr, {}).get('probe_failed'):
                    return False

            successors, state, curr_removed = _probe_successors(
                state, branches, isolate, composition_children
            )
            if curr_removed:
                return False
            

            # 5) Add succ dependencies
            t0 = time.time()
            # If no valid successor
            if len(self.G.succ[curr])==0 and 'error' in self.G.nodes[curr]:
                self.G.nodes[pred]['error'] = curr_fld + ' ' + self.G.nodes[curr]['error']
                self.G.remove_node(curr)
                timer['error'] += time.time() - t0
                write_file(f"(❌❌Invalid Field: {state.cmd} {{{self.G.nodes[pred]['error']}}}\n", state.level)
                return False if state.merge_root else True

            # _connect_recurrence_dependencies(state, successors)

            # 6) Merge leaves to form template graph
            _merge_branch_leaves(state, curr_fld, succ_end)


            # Exit of recursion, ensuring scope of composition & combination module. curr kept
            return False if state.merge_root else True

        

        # Start timer
        timer['start'] = time.time()

        # Get the path under the view
        view = self.img.get_view()

        log_dir = f"logs/{PRODUCT}/{view[1:-1]}"
        os.makedirs(log_dir, exist_ok=True)
        self.log_path = f"{log_dir}/{self.file_name}.log"    

        graph_dir = f"graphs/{PRODUCT}/{view[1:-1]}/{self.file_name}"
        os.makedirs(graph_dir, exist_ok=True)
        self.graphml_path = f"{graph_dir}/{self.file_name}_{ABLAT[0]}{ABLAT[2]}{ABLAT[3]}.graphml"
        self.fld_svg_path = f"{graph_dir}/{self.file_name}_ConfigG.svg"
        self.tmpl_svg_path = f"{graph_dir}/{self.file_name}_DSL.svg"
        self.tmpl_svg_simple_path = f"{graph_dir}/{self.file_name}_DSLsimple.svg"
        self.tmpl_log_path = f"{graph_dir}/{self.file_name}_DSL.log"
        self.tmpl_json_path = f"{graph_dir}/{self.file_name}_DSL.json"


        # Clear the current log
        if CLEAR_LOG:
            with open(self.log_path, 'w') as f:                              
                f.write('')

        # Processing prefix
        self.G = nx.DiGraph()
        root = dag.get_uuid()
        self.G.add_node(root, type='field', label=view)
        prefixes = COMMAND.split()
        pred_id = root
        for _, pre in enumerate(prefixes):
            curr_id = dag.get_uuid()
            self.G.add_node(curr_id, type='field', label=pre)
            self.G.add_edge(pred_id, curr_id)
            pred_id = curr_id


        print(f'Prefix: {COMMAND}  Probing View:{CROSS}  Ablation: {ABLAT}')
        branch = COMMAND + ' ' if COMMAND else ''
        initial_state = _ProbeState(
            curr=pred_id,
            input_text=COMMAND + ' ',
            templ=branch,
            prune_root=pred_id,
            view=view,
            view_path=((view, ''),),
        )
        probe_recursive(initial_state)
        for n in dag.get_leaves(self.G):
            if label(n) != 'END':
                # print(f"{label(n)}: END missing")
                dag.add_node_edge(self.G, n, 'END')

        
        dag.graph2graphml(self.G, self.graphml_path)

        node_count = len(self.G.nodes)
        end_count = len({n for n, d in self.G.out_degree() if d == 0})
        viw_count = len({n for n in self.G.nodes if re.search(r'\[.*?\]', label(n))})
        nfd_count = node_count - end_count - viw_count
        graph_info = f"Normal Field: {nfd_count}, \
                        View Count: {viw_count}, \
                        End Count: {end_count},\n \
                        {count},\n \
                        {timer}"
        self.log_graph_info()
        self.log_graph_info(graph_info)
        print(graph_info)


    def get_graph_svg(self, type: str='', path=None):
        if not path:
            if type == 'f':
                g = copy.deepcopy(self.G)
                path = self.fld_svg_path
            elif type == 't':
                g = copy.deepcopy(self.G_templ)
                path = self.tmpl_svg_path
            elif type == 'ts':
                g = copy.deepcopy(self.G_templ_simple)
                path = self.tmpl_svg_simple_path
        else:
            g = copy.deepcopy(self.G)
        
        for node in g.nodes:
            value = g.nodes[node]['label']
            if '.' in value or '<' in value or '>' in value:
                g.nodes[node]['label'] = ' ' + value + ' '
            if 'error' in g.nodes[node]:
                error = g.nodes[node]['error']
                if '.' in error or '<' in error or '>' in error:
                    g.nodes[node]['error'] = ' ' + error + ' '
            if 'prune' in g.nodes[node]:
                mode = g.nodes[node]['prune']
                # g.nodes[node]['style'] = 'filled'
                if mode == 'composition':
                    g.nodes[node]['color'] = "#cb1e1e"
                    g.nodes[node]['fillcolor'] = '#cb1e1e'
                elif mode == 'repetition':
                    g.nodes[node]['color'] = "#6e12d6"
                    g.nodes[node]['fillcolor'] = '#6e12d6'
                elif mode == 'permutation':
                    g.nodes[node]['color'] = "#06991C"
                    g.nodes[node]['fillcolor'] = '#06991C'
                elif mode == 'combination':
                    g.nodes[node]['color'] = "#DF7904"
                    g.nodes[node]['fillcolor'] = '#DF7904'
                elif 'error' in g.nodes[node]:
                    g.nodes[node]['color'] = "#DBDF04"
                    g.nodes[node]['fillcolor'] = '#DBDF04'
            g.nodes[node]['shape'] = 'box'
                # g.nodes[node]['style'] = 'filled'
                # g.nodes[node]['fontcolor'] = "#4F0707"

        dot_file = f'temp_{random.randint(0, 9999)}.dot'

        pydot_graph = nx.nx_pydot.to_pydot(g)
        pydot_graph.set_graph_defaults(rankdir='LR', overlap='false') 

        pydot_graph.write(dot_file)
        subprocess.run([DOT_PATH, "-Tsvg", dot_file, "-o", path])

        os.remove(dot_file)


    def get_valid_path(self):
        root = dag.get_root(self.G)
        topo_order = list(nx.topological_sort(self.G))

        
        # dynamic planning：dp[node] = path_num from root to node
        dp = {node: 0 for node in self.G.nodes()}
        dp[root] = 1  
        
        # topology sequence
        for node in topo_order:
            # pass current node's path_num to succ
            for neighbor in self.G.successors(node):
                dp[neighbor] += dp[node]
        
        # get sum of paths of leaves
        total = 0
        for node in self.G.nodes():
            if self.G.out_degree(node) == 0: 
                total += dp[node]
        
        return total


    def field_to_template(self, store_field_graph=True, simple_template=False): 
        """
        Expand ConfigG for each leaf, and templatize each subgraph

        """

        def unfold_recursive(g: nx.DiGraph, start_n, expanded_g=None):
            if not expanded_g:
                expanded_g = nx.DiGraph()
                expanded_g.add_node(start_n)

            nv_ids, end_ids = dag.find_ends_dfs_edges(g, start_n)
            ends = nv_ids | end_ids
            
            for end in ends:
                # global subg_dict
                sub_g = dag.get_subgraph_reverse(g, start_n, end, copy=True)
                root_subg = dag.get_root(sub_g)
                template, _ = dag.graph2template(sub_g)

                # subg_dict[template] = sub_g
                # with open(self.tmpl_log_path, 'a', encoding='utf-8') as file:
                #     file.write(f'{template}\n')
                
                remark = 'END' if g.out_degree(end) == 0 else 'VIEW'
                dag.add_node_edge(expanded_g, start_n, [template, remark], end)     # add template node: end
                # subg_id = dag.add_node_edge(compacted_g, end, '<subgraph>')       # add subg field node: end->subg_node
                if store_field_graph:
                    expanded_g = nx.compose(expanded_g, sub_g)                          # add subgraph
                    expanded_g.add_edge(end, root_subg)                                 # add edge to subgraph: end->rootsubg

                if remark == 'VIEW':
                    successor_g = unfold_recursive(g, end)                          # get successor template subg
                    expanded_g = nx.compose(expanded_g, successor_g)                # add succ template subg

            return expanded_g


        def unfold_recursive_simple(g: nx.DiGraph, start_n, expanded_g=None):
            if not expanded_g:
                expanded_g = nx.DiGraph()
                expanded_g.add_node(start_n)

            nv_ids, end_ids = dag.find_ends_dfs_edges(g, start_n)
            ends = nv_ids | end_ids
            
            for end in ends:
                # global subg_dict
                sub_g = dag.get_subgraph_reverse(g, start_n, end, copy=True)
                # templates = dag.graph2template_simple(sub_g)
                template, sub_templates = dag.graph2template(sub_g)
                
                remark = 'END' if g.out_degree(end) == 0 else 'VIEW'
                if remark == 'VIEW':
                    dag.add_node_edge(expanded_g, start_n, [template, remark], end)     # add template node: end
                    expanded_g.nodes[end]['view'] = self.label(end)
                    expanded_g.nodes[end]['subt'] = sub_templates
                    successor_g = unfold_recursive_simple(g, end)                          # get successor template subg
                    expanded_g = nx.compose(expanded_g, successor_g)                # add succ template subg
                else:
                    new_node = dag.add_node_edge(expanded_g, start_n, [template, remark])     # add template node: end
                    expanded_g.nodes[new_node]['subt'] = sub_templates

            return expanded_g


        with open(self.tmpl_log_path, 'w') as f:
            f.write('')
        root = dag.get_root(self.G)
        compacted_g = nx.DiGraph()
        compacted_g.add_node(root, type='template', label=dag.label(self.G, root), remark='ROOT')
        if simple_template:
            compacted_g = unfold_recursive_simple(self.G, root, compacted_g)
        else:
            compacted_g = unfold_recursive(self.G, root, compacted_g)
        
        dag.log_graph(compacted_g, self.tmpl_log_path)

        if store_field_graph:
            self.G_templ = compacted_g
        else:
            self.G_templ_simple = compacted_g


    def tree_to_json(self):
        """
        递归将 nx.DiGraph 转化为嵌套的字典 (JSON 结构)
        """
        def recursive(node_id):
            nonlocal num
            num += 1
            node_attrs = graph.nodes[node_id]
            node_data = {}
            node_type = node_attrs.get('remark', 'unknown')
            
            node_data['node_id'] = num
            if node_type == 'ROOT':
                node_data['node_type'] = 'ROOT'
            
            elif node_type == 'VIEW':
                node_data['node_type'] = 'view_node'
                node_data['view_name'] = node_attrs.get('view', 'unknown-view')
                node_data['cmd_aggregatedTemplate'] = node_attrs.get('label', '')
                node_data['cmd_templates'] = node_attrs.get('subt', '')
                
            elif node_type == 'END':
                node_data['node_type'] = 'terminal_node' 
                node_data['cmd_aggregatedTemplate'] = node_attrs.get('label', '')
                node_data['cmd_templates'] = node_attrs.get('subt', '')

            # 递归处理子节点
            # 使用 sorted 保证输出顺序固定 (可选)
            children = sorted(list(graph.successors(node_id)))
            
            # 叶子节点 children 为空列表，符合要求
            node_data['children'] = [recursive(child) for child in children]
            
            return node_data

        graph = self.G_templ_simple
        num = -1
        root = dag.get_root(self.G)
        json_structure = recursive(root)
        with open(self.tmpl_json_path, 'w', encoding='utf-8') as f:
            json.dump(json_structure, f, indent=4, ensure_ascii=False)
        print(f"Json dumped in {self.tmpl_json_path}")

    
    def tree_to_log(self):
        """
        递归生成类似 'tree' 命令的文本视图，并让同一层级下的命令按首字母排序
        """

        graph = self.G_templ_simple
        root = dag.get_root(self.G)

        def get_display_text(node_id):
            """
            获取节点实际输出文本
            """
            node_attrs = graph.nodes[node_id]
            node_type = node_attrs.get('remark')

            if node_type == 'ROOT':
                return "[ROOT]"

            elif node_type == 'VIEW':
                cmd = node_attrs.get('label', '')
                view = node_attrs.get('view', '')
                return f"{cmd}  [Enters: {view}]"

            else:
                return node_attrs.get('label', '')

        def get_sort_key(node_id):
            """
            获取排序 key。
            按命令文本排序，不按 node_id 排序。
            """
            node_attrs = graph.nodes[node_id]
            cmd = node_attrs.get('label', '')

            return (
                cmd.strip().casefold(),
                str(node_id)
            )

        def recursive(node_id, level, is_last, prefix):
            display_text = get_display_text(node_id)

            # 组合前缀和当前文本
            if level == 0:
                current_line = display_text
            else:
                connector = "└── " if is_last else "├── "
                current_line = prefix + connector + display_text

            lines = [current_line]

            # 关键修改：按命令 label 排序，而不是按 node_id 排序
            children = sorted(
                list(graph.successors(node_id)),
                key=get_sort_key
            )

            count = len(children)

            for i, child in enumerate(children):
                is_last_child = (i == count - 1)

                # 更新下一层的前缀
                if level > 0:
                    new_prefix = prefix + ("    " if is_last else "│   ")
                else:
                    new_prefix = ""

                lines.extend(
                    recursive(child, level + 1, is_last_child, new_prefix)
                )

            return lines

        text_lines = recursive(root, 0, False, "")

        with open(self.tmpl_log_path, 'w', encoding='utf-8') as f:
            for line in text_lines:
                f.write(line + '\n')

        print(f"text dumped in {self.tmpl_log_path}")





if __name__ == "__main__":

# probing complete graph
    try:
        startup_time = None
        if not GRAPH_PATH:              # Probe
            t0 = time.time()
            model = ConfProbe()
            startup_time = time.time() - t0
            print(f"Startup Time: {(startup_time):.3f} s")
            t0 = time.time()
            # model.probe_graph()
            model.probe_graph()
            t1 = time.time()
            pre_time = t1 - t0
            print(f"Probing Time: {(pre_time):.3f} s")
        
        else:                           # Convert
            t0 = time.time()
            model = ConfProbe(GRAPH_PATH)
            t1 = time.time()
            pre_time = t1 - t0


        model.get_graph_svg('f')
        t2 = time.time()
        fld_svg_time = t2 - t1
        

        # path_num = model.get_valid_path()
        # model.log_graph_info(f"Valid paths: {path_num}")

        runtime_info = f"startup time: {startup_time if startup_time else 0}\npreparation time: {pre_time}\n"
        model.log_graph_info(runtime_info)
        print(runtime_info)

        # model.partition_tmp()
        # model.field_to_template(store_field_graph=False)
        model.field_to_template(store_field_graph=False, simple_template=True)
        # model.get_graph_svg('ts')
        model.tree_to_json()
        model.tree_to_log()


        # model.field_to_template()
        # model.get_graph_svg('t')

    except TimeoutError:
        print('break')


    # model.partition_tmp()
    # model.field_to_template(store_field_graph=False)
    # model.get_graph_svg('ts')

    # model.field_to_template()
    # model.get_graph_svg('t')


    
