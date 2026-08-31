import networkx as nx
from collections import deque, defaultdict
import copy
import uuid
import re


def add_attribute(g: nx.DiGraph):
    for node in g.nodes():
        name = label(g, node)
        del g.nodes[node]['label']
        g.nodes[node]['type'] = 'field'
        g.nodes[node]['label'] = name


def add_edges(g: nx.DiGraph, pred_nodes, node=None, attribute: list=None):
    """
    add edges

    Parameter 
    -----
    pred_nodes : predecessor id
    node : successor id
    """
    if not node:
        node = get_uuid()
    if attribute:   
        for pred_node in pred_nodes:
            g.add_edge(pred_node, node, **attribute)
    else:
        g.add_edges_from([(pred, node) for pred in pred_nodes])


def add_node_edge(g: nx.DiGraph, pred_node, attributes: str|list[str], node=None):
    """
    add node and edge from pred to node

    Parameter 
    -----
    pred_node : pred id
    attributes : succ attribute 
    node (optional) : succ id 

    Return
    -----
    node : added node's id
    """
    if not node:
        node = get_uuid()
    if isinstance(attributes, str):
        g.add_node(node, type='field', label=attributes)
    elif isinstance(attributes, list):
        g.add_node(node, type='template', label=attributes[0], remark=attributes[1])
    g.add_edge(pred_node, node)

    return node


def get_avail_ancestors(g: nx.DiGraph, first, node, self=True) -> set:
    if self:
        return (nx.ancestors(g, node) - nx.ancestors(g, first)) | {node}
    else:
        return nx.ancestors(g, node) - nx.ancestors(g, first)


def merge_to_equivalent(g: nx.DiGraph, first, node, succ_flds: set, sbl_flds: set):
    """

    Parameter
    ------
    g : ConfigG
    node : node to be merged
    succ_flds : next level fields
    sbl_flds : current level fields

    Return
    -----
    nearest_id : node being merged to, or None
    """

    except_ids = nx.ancestors(g, node) | {node}     # to avoid cycle
    for node2 in nx.descendants(g, first):
        if node2 in except_ids:
            continue

        if label(g, node) == label(g, node2):
            if succ_flds == labels(g, node2, type='succ'): 
                sbl_flds2 = get_siblings(g, node2, label=True)
                if sbl_flds == sbl_flds2:
                    return node2 

    return None


def delete_subgraph(g: nx.DiGraph, root, delete_root: bool=True):
    if delete_root:
        unnodes = nx.descendants(g, root)|{root}
    else:
        unnodes = nx.descendants(g, root)
    g.remove_nodes_from(unnodes)


def find_ends_dfs_edges(g: nx.DiGraph, start_node):
    """
    using dfs_edges to DFS

    find view or end

    Return
    -----
    (stop_nodes, end_nodes) : stopped nodes, leaf nodes
    """
    stop_nodes = set()
    stop_prt_nodes = set()
    end_nodes = set()
    
    for u, v in nx.dfs_edges(g, start_node):
        if nx.ancestors(g, v) & stop_nodes:
            continue
        if re.search(r'^\[.*?\]$', g.nodes[v]['label']):
            stop_prt_nodes.add(u)
            stop_nodes.add(v)
        elif g.out_degree(v) == 0:
            end_nodes.add(v)
    
    return stop_nodes, end_nodes


def get_node_num(g: nx.DiGraph, first, exception = 'END'):
    """
    get numn starting from first (exept END)
    """
    nodes = {n for n in nx.descendants(g, first) if label(g, n) != exception} | {first}
    return len(nodes)


def get_leaves(g: nx.DiGraph, first=None) -> set:
    """
    get subgraph's leaves rooted at first node
    """
    if first:
        return {n for n in nx.descendants(g, first)|{first} if g.out_degree(n) == 0}
    else:
        return {n for n, d in g.out_degree() if d == 0}



def get_root(g: nx.DiGraph) -> str|int:
    """
    return root id, only when one root
    """
    roots = [n for n, d in g.in_degree() if d == 0]
    if len(roots) == 1:
        return roots[0]
    else:
        x=[label(g, x) for x in roots]
        raise ValueError("multiple roots exist")


def get_siblings(g: nx.DiGraph, node, label=False) -> set:
    """
    return v's sibling nodes

    Parameter
    -------
    label : if return label, or just id
    """
    siblings = set()
    for n in g.predecessors(node):
        siblings |= set(g.succ[n])
    siblings -= {node}
    
    if label:
        siblings = {g.nodes[n]['label'] for n in siblings}
    return siblings


def get_subgraph(g: nx.DiGraph, node, copy=True, succ: set=None) -> nx.DiGraph:
    """
    succ : only specified successor's subgraph are included
    Return
    -----
    return view or copy(shallow)
    won't change id
    
    """
    if not succ:
        nodes = {node} | nx.descendants(g, node)
    else:
        nodes = {node} | {nx.descendants(g, n) for n in succ}
        
    if copy:
        return g.subgraph(nodes).copy()
    else:
        return g.subgraph(nodes)


def get_subgraph_reverse(g: nx.DiGraph, start_node=None, node=None, copy=False) -> nx.DiGraph:
    """
    get subgraph from node1 to node2
    
    """
    if not start_node:
        start_node = get_root(g)
    if not node:
        node = get_leaves(g).pop()

    # reversed BGS to get all relative edges
    visited = {node}
    queue = deque([node])
    edges = []

    while queue:
        v = queue.popleft()
        if v == start_node:
            continue

        # traverse all predecessors
        for u in g.predecessors(v):
            edges.append((u, v))

            if u not in visited:
                visited.add(u)
                queue.append(u)

    if copy:
        subgraph = g.edge_subgraph(edges).copy()
        nx.set_node_attributes(subgraph, {n: g.nodes[n] for n in subgraph.nodes})
        nx.set_edge_attributes(subgraph, {(u, v): g[u][v] for u, v in subgraph.edges})
        rename_graph(subgraph)
    else:
        subgraph = g.edge_subgraph(edges)
        nx.set_node_attributes(subgraph, {n: g.nodes[n] for n in subgraph.nodes})
        nx.set_edge_attributes(subgraph, {(u, v): g[u][v] for u, v in subgraph.edges})


    return subgraph


def get_uuid() -> str:
    return str(uuid.uuid1())


def describe_cycle(g: nx.DiGraph) -> str:
    """Return node identifiers and labels for one directed cycle in *g*."""
    cycle = nx.find_cycle(g, source=None)
    nodes = [edge[0] for edge in cycle] + [cycle[-1][1]]
    return ' -> '.join(
        f"{node} ({g.nodes[node].get('label', '<missing label>')})"
        for node in nodes
    )


def graph2graphml(g: nx.DiGraph, new_graph_file: str='new.graphml'):
    if not nx.is_directed_acyclic_graph(g):
        raise ValueError(
            f"cycle detected before GraphML export: {describe_cycle(g)}"
        )

    for node in g.nodes():
        if 'end' in g.nodes[node]:
            del g.nodes[node]['end']
        if 'succ' in g.nodes[node]:
            del g.nodes[node]['succ']
        if 'recur_end' in g.nodes[node]:
            del g.nodes[node]['recur_end']
        if 'desc' in g.nodes[node]:
            del g.nodes[node]['desc']

    newg = copy.deepcopy(g)
    for node, data in newg.nodes(data=True):
        if 'recur' in data:
            set_data = data['recur']
            newg.nodes[node]['recur'] = ';'.join(set_data)

    nx.write_graphml_lxml(newg, new_graph_file)


def graph2dot(g: nx.DiGraph, new_graph_file: str='new.dot'):

    g1 = copy.deepcopy(g)
    for _, data in g1.nodes(data=True):
        data.pop('desc', None)
    g1.graph['rankdir'] = 'LR'
    nx.nx_pydot.write_dot(g1, new_graph_file)


def graph2template(g: nx.DiGraph, root=None, leaf=None) -> tuple[str, list]:
    """
    graph to cmd template

    not include &<m,n>

    """

    def get_name(id) -> str:
        # if 'duplicate' in g.nodes[id]:
        #     duplicate = g.nodes[id]['duplicate']
        #     if duplicate == 0 or duplicate == '0':
        #         return label(g, id)
        #     else:
        #         return f"<{label(g, id)}>&<1,{duplicate}>"
        # else:
        return label(g, id)
 
    def pop_same_descendants(queues: list[deque]) -> tuple[list, str]:

        descendants = []
        branch = '{}'
        star = ''
        
        while True:
            if len({q[0] for q in queues if q}) == 1:
                if any(not q for q in queues):
                    return descendants, '[]'
                else:
                    return descendants, '{}'
                
            last = {q[-1] for q in queues if q}
            if len(last) == 1:              
                descendants.append(last.pop())
                for q in queues:
                    if q:
                        q.pop()
                continue
            
            
            if any('dict' in g.nodes[q[0]] for q in queues if q):
                if all('dict' in g.nodes[q[0]] for q in queues if q):   
                    star = '*'
                x = [q[-1] for q in queues if q]
                if len(x) == len(set(x)):
                    branch = '[]' if any(not q for q in queues) else '{}'
                    return descendants, branch+star
                
                remove_list = []
                for q in queues:
                    if q:
                        if 'dict' in g.nodes[q[0]] :
                            for p in queues:
                                if p and p != q:
                                    if 'dict' in g.nodes[p[0]]:
                                        if g.nodes[q[0]]['dict']['recur']|{label(g, q[0])} < g.nodes[p[0]]['dict']['recur']:
                                            if q not in remove_list:
                                                remove_list.append(q)   
                                    elif label(g, p[0]) in g.nodes[q[0]]['dict']['recur']:
                                        if p not in remove_list:
                                            remove_list.append(p)

                if remove_list:
                    for q in remove_list:
                        queues.remove(q)
                    desc = None
                    for q in queues:
                        if q:
                            desc = q.pop()
                    descendants.append(desc)
                else:
                    if any(not q for q in queues):
                        branch = '[]'
                    return descendants, branch+star

            else:
                if any(not q for q in queues):
                    branch = '[]'
                return descendants, branch+star
            
    def get_templ_block(node, leaf) -> tuple:
        field_ids: list[str] = [node]       # one node or tuple
        queues: list[deque] = []
        while True:
            succs = list(g.succ[node])
            if len(succs) == 1:
                field_ids.append(succs[0])
            elif len(succs) > 1:
                # 【add element to queue, first if multiple succ】
                for succ in succs:
                    queues.append(deque([succ]))
                    while True:
                        succ_succs = list(g.succ[succ])   
                        if not succ_succs:
                            break
                        elif len(succ_succs) == 1:
                            succ_succ = succ_succs[0]
                            queues[-1].append(succ_succ)
                            if succ_succ == leaf:               # if end, exit
                                break
                            succ = succ_succ
                        else:
                            templ_block = list(get_templ_block(succ, leaf))
                            if templ_block[0] == queues[-1][-1]:    # deduplicate
                                del templ_block[0]
                            queues[-1].extend(templ_block)      # recursively add to queue
                            break
                
                
                if len(queues) == 1:
                    field_ids.extend([*queues[0]])
                else:
                    descendants, branch = pop_same_descendants(queues)
                    descendants.reverse()
                    if descendants:
                        # field_set: all elemnts are separated with |
                        field_set = []
                        for q in queues:
                            if len(q) > 1:
                                field_set.append((*q,))
                            elif len(q) == 1:
                                field_set.append(q[0])     
                        field_set.append(branch)
                        # field_set.append('[]' if any(len(q)==0 for q in queues) else '{}')
                        field_ids.append(tuple(field_set))
                        field_ids.extend(descendants)      # add all same descendants
                    else:  
                        raise ValueError(f"Fields Empty: {list(queues)}")

            if leaf == field_ids[-1]:
                break
            else:
                node = field_ids[-1]

        return tuple(field_ids)

    def get_templ_string(fields: tuple) -> str:
        """
        tuple to template text
        """

        new_fields = []
        field_type = fields[-1]
        
        if field_type in ['[]', '[]*', '{}', '{}*']:                    # branch
            for field in fields[:-1]:
                if isinstance(field, tuple):
                    new_fields.append(get_templ_string(field))
                elif isinstance(field, (str, int)):
                    new_fields.append(get_name(field))
            if field_type == '[]':                          # optional
                return f"[{'|'.join(new_fields)}]"
            elif field_type == '[]*':                       # finite optional
                return f"[{'|'.join(new_fields)}]*"
            elif field_type == '{}':                        # alternative
                return f"{{{'|'.join(new_fields)}}}"
            else:                                           # finite alternative
                return f"{{{'|'.join(new_fields)}}}*"
        else:                                               # consecutive field
            for field in fields:
                if isinstance(field, tuple):
                    new_fields.append(get_templ_string(field))
                elif isinstance(field, (str, int)):
                    new_fields.append(get_name(field))

            return ' '.join(new_fields)




    if not root:
        root = get_root(g)
        leaf = get_leaves(g).pop()

    fields = list(get_templ_block(root, leaf))

    if re.search(r'\[.*?\]', get_name(fields[0])):      # view
        del fields[0]
    if re.search(r'\[.*?\]', get_name(fields[-1])):     # view
        del fields[-1]
    if fields and get_name(fields[-1]) == 'END':        # END
        del fields[-1]

    new_template = get_templ_string(tuple(fields))
    # print(new_template)


    paths = list(nx.all_simple_paths(g, root, leaf))
    sub_templates = []
    for path in paths:
        fields = [label(g, n) for n in path]
        if re.search(r'\[.*?\]', fields[0]):      # view
            del fields[0]
        if re.search(r'\[.*?\]', fields[-1]):     # view
            del fields[-1]
        if fields and fields[-1] == 'END':                   # END
            del fields[-1]

        template = ' '.join(fields)
        sub_templates.append(template)

    return new_template, sub_templates


def graph2template_simple(g: nx.DiGraph, root=None, leaf=None) -> list:
    if not root:
        root = get_root(g)
        leaf = get_leaves(g).pop()
    paths = list(nx.all_simple_paths(g, root, leaf))
    templates = []
    for path in paths:
        fields = [label(g, n) for n in path]
        if re.search(r'\[.*?\]', fields[0]):      # view
            del fields[0]
        if re.search(r'\[.*?\]', fields[-1]):     # view
            del fields[-1]
        if fields and fields[-1] == 'END':                   # END
            del fields[-1]

        template = ' '.join(fields)
        # subgraph = nx.DiGraph()
        # subgraph.add_nodes_from(path)
        # for u, v in g.subgraph(path).edges():
        #     subgraph.add_edge(u, v)

        templates.append(template)

    return templates



def label(g: nx.DiGraph, n) -> str:
    return g.nodes[n]['label']


def labels(g: nx.DiGraph, n, type: str=None, self=False) -> set:
    """
    return all specified nodes

    Parameter
    ---------
    n : node
    type : {succ | desc}
    self : if include self
    """
    names = set()
    if type == 'succ':
        names = {g.nodes[i]['label'] for i in g.successors(n)}
    elif type == 'pred':
        names = {g.nodes[i]['label'] for i in g.predecessors(n)}
    elif type == 'desc':
        names = {g.nodes[i]['label'] for i in nx.descendants(g, n)}
    elif type == 'ance':
        names = {g.nodes[i]['label'] for i in nx.ancestors(g, n)}
    elif type == 'leaf':
        names = {g.nodes[i]['label'] for i in get_leaves(g, n)}
    else:
        raise ValueError('Undefined Type')
    
    if self:
        names.add(g.nodes[n]['label'])
    return names


def log_graph(g: nx.DiGraph, log_path: str, root: str=None):
    """
    put graph into log
    
    """
    depth = {}
    if not root:
        root = get_root(g)
    depth[root] = -2


    for u, v, direction in nx.dfs_labeled_edges(g, root):
        if direction == 'forward' and g.nodes[v]['type'] == 'template':
            # if forward, depth+1
            depth[v] = depth[u] + 1
    del depth[root]

    with open(log_path, 'a', encoding='utf-8') as file:
        file.write(f"Root view: {label(g, root)}\n")
        for node, d in depth.items():
            file.write(f"{'    '*d}{label(g, node)}\n")
            if 'view' in g.nodes[node]:
                file.write(f"{'    '*d}{g.nodes[node]['view']}\n")


def merge_leaf(g: nx.DiGraph, leaves: set, node_id):
    """
    merge leaves: first remove then add

    Parameter 
    ------
    leaves : leaf set(-node_id)
    node_id : leaf being merged to
    """
    for leaf in leaves:
        preds = set(g.pred[leaf])
        g.remove_node(leaf)
        add_edges(g, preds, node_id)


def merge_end_alter_lca(g: nx.DiGraph, first, max_num: int, freeze_end=None) -> int:
    """
    merge end that haven't been merged before

    Return
    ------
    merged_num : merged leaf number
    """        

    lca_dict = defaultdict(set)
    merged_num = 0

    
    for leaf in get_leaves(g, first)-{freeze_end}:

        if len(g.pred[leaf]) == 1:           
            ance = get_avail_ancestors(g, first, leaf) 
            if len(ance) < max_num:    
                node = leaf             
                end_loop = False 
                while not end_loop:
                    preds = set(g.pred[node])
                    if first in preds: 
                        node = first
                        break
                    
                    for pred in preds:
                        node = pred
                        if not set(g.succ[pred]) <= ance:   
                            end_loop = True
                            break

                lca_dict[node].add(leaf)
        
        elif label(g, leaf) != 'END':
            add_node_edge(g, leaf, 'END')

        
    for leaves in lca_dict.values():
        ends = {leaf for leaf in leaves if label(g, leaf) == 'END'}

        ance_set = set()
        for leaf in leaves:
            ance_set |= nx.ancestors(g, leaf)
        ance_set |= (leaves - ends)
        ance_set -= nx.ancestors(g, first)

        if len(ance_set) > max_num:
            for n in leaves-ends:
                add_node_edge(g, n, 'END')

        else:
            if ends:
                non_ends = leaves - ends
                end = ends.pop()
                g.add_edges_from([(non_end, end) for non_end in non_ends])
                merge_leaf(g, ends, end)
            else:
                leaf = leaves.pop()
                end = add_node_edge(g, leaf, 'END')
                add_edges(g, leaves, end)

            merged_num += (len(leaves)-1) if leaves else 0

    return merged_num
            

def merge_end_option(g: nx.DiGraph, first, end, max_num: int) -> int:
    """
    merge []

    Return
    ------
    nodes_num : merged leaf number
    """

    other_leaves = get_leaves(g, first)-{end}
    other_ends = {leaf for leaf in other_leaves if label(g, leaf) == 'END'}

    if get_node_num(g, first) > max_num:
        for leaf in other_leaves-other_ends:
            add_node_edge(g, leaf, 'END')
        return 0
        
    else:
        if other_ends:
            for other_end in other_ends:
                other_leaves |= set(g.predecessors(other_end))
            other_leaves -= other_ends
            g.remove_nodes_from(other_ends)

        add_edges(g, other_leaves, end)
        return len(other_leaves)
    

def rename_graph(origin_g: nx.DiGraph, exception: set=None):

    exception = exception or set()
    mapping = {}
    for old_id in set(origin_g.nodes()) - exception:
        mapping[old_id] = get_uuid()

    nx.relabel_nodes(origin_g, mapping, copy=False)





if __name__ == "__main__":

    g = nx.DiGraph()
    edges = [
        (0,1),(1,2),(2,3),(3,4),(4,5),
        (2,5),(0,7),(7,6),(6,5),(5,8)
    ]
    g.add_nodes_from(range(9))
    g.nodes[0]['label'] = 'A'
    g.nodes[1]['label'] = 'B'
    g.nodes[2]['label'] = 'C'
    g.nodes[3]['label'] = 'D'
    g.nodes[4]['label'] = 'E'
    g.nodes[5]['label'] = 'F'
    g.nodes[6]['label'] = 'G'
    g.nodes[7]['label'] = 'H'
    g.nodes[8]['label'] = 'I'
    g.add_edges_from(edges)
    # graph2template(g)

    depths = log_graph(g, 'test.log')
    for node, d in depths.items():
        print(f"node: {node}, depth: {d}")
