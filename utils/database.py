import networkx as nx
from py2neo import Graph, Node, Relationship

import utils.dag_algorithm as dag
from utils.config import *

url = "bolt://localhost:7687"  # Neo4j数据库的URI
username = "neo4j"              # 数据库用户名
password = "11111111"           # 数据库密码
TYPES = ["<cr>", "<next-view>", "<subgraph>", "ROOT", "END", "NEXT"]

def graph2neo4j(G: nx.DiGraph, subg_dict: dict):

    def import_subgraph(g: nx.DiGraph, parent_node: Node, neo4j_graph: Graph):
        """
        导入子图并连接到父节点
        
        Parameter
        -----
        subgraph : 子图
        parent_node : Neo4j中的父节点
        global_mapping : 全局节点映射
        neo4j_graph : Neo4j图实例
        """

        # 【导入字段节点】
        sub_mapping = {}
        for node, data in g.nodes(data=True):
            node_label = data.get('label', '')
            if node_label in TYPES:
                neo4j_node = Node(node_label, **data)
            else:
                neo4j_node = Node("field", **data)
            
            neo4j_graph.create(neo4j_node)
            sub_mapping[node] = neo4j_node
        
        # 【导入字段依赖】
        for u, v, data in g.edges(data=True):
            if u in sub_mapping and v in sub_mapping:
                rel = Relationship(sub_mapping[u], 'before', sub_mapping[v], **data)
                neo4j_graph.create(rel)
            else:
                print(f"警告: 子图中缺少节点 {u}→{v}，跳过边")

        root = dag.get_root(g)
        rel = Relationship(parent_node, 'CONTAINS', sub_mapping[root])
        neo4j_graph.create(rel)


    # 【开始】
    neo4j_graph = Graph(url, auth=(username, password))
    neo4j_graph.delete_all()

    # 【导入模板节点】
    global_mapping = {}
    for node, data in G.nodes(data=True):
        node_remark = G.nodes[node].get('remark', '')
        node_template = G.nodes[node].get('label', '')
        if node_remark in TYPES:
            neo4j_node = Node(node_remark, **data)
        else:
            neo4j_node = Node("field", **data)
        
        neo4j_graph.create(neo4j_node)
        global_mapping[node] = neo4j_node

        # 如果该节点有映射的子图，导入子图
        if node_template in subg_dict:
            import_subgraph(subg_dict[node_template], neo4j_node, neo4j_graph)

    # 【导入模板依赖】
    for u, v, data in G.edges(data=True):
        rel = Relationship(global_mapping[u], 'ENABLES', global_mapping[v], **data)
        neo4j_graph.create(rel)
    
    print('loaded to neo4j')


def graphml2neo4j(path):
    G = nx.read_graphml(path) 
    graph2neo4j(G)


if __name__ == "__main__":

    cmd = COMMAND.replace(' ', '_')
    # cmd = "router_ospf"
    graph_path = f"CLI echo/sub-command/config/{cmd}.graphml"

    graphml2neo4j(graph_path)
    