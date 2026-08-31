import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from math import ceil
import scipy.sparse as sp
from pyvis.network import Network
import subprocess
import os

from py2neo import Graph, Node, Relationship
import utils.dag_algorithm as dag
# from config import *
from utils.config import *

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

edge_color_map = {
    'view': 'darkgrey',  
    'direct': 'royalblue',  
    'indirect': 'firebrick', 
    'dual': 'forestgreen'  
}

def hierarchical_layout(G):
    """每层节点水平居中对称排列"""
    # 计算节点层级（基于最长路径）
    layers = {}
    for node in nx.topological_sort(G):
        if G.in_degree(node) == 0:
            layers[node] = 0
        else:
            layers[node] = max(layers[pred] for pred in G.predecessors(node)) + 1

    # 按层分组节点
    layer_groups = defaultdict(list)
    for node, layer in layers.items():
        layer_groups[layer].append(node)

    # 布局参数
    max_layers = max(layers.values(), default=0)
    vertical_spacing = 1.2    # 垂直层间距
    base_y = max_layers * vertical_spacing  # 顶层初始Y坐标
    
    pos = {}
    for layer in sorted(layer_groups.keys()):
        nodes_in_layer = layer_groups[layer]
        num_nodes = len(nodes_in_layer)
        
        # 水平对称布局
        horizontal_range = num_nodes * 1.0  # 水平总跨度
        start_x = -horizontal_range / 2     # 起始X坐标
        
        # 计算每个节点的坐标
        for i, node in enumerate(sorted(nodes_in_layer)):
            x = start_x + (i + 0.5) * (horizontal_range / num_nodes)
            y = base_y - layer * vertical_spacing  # Y坐标从顶部开始递减
            pos[node] = (x, y)
    
    return pos


def visualize_graph(G):
    # 绘图初始化
    pos = hierarchical_layout(G)
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.axis("off")

    # 边颜色映射
    edge_colors = [edge_color_map[G[u][v]["dependency"]] for u, v in G.edges()]

    # 绘制基础图形
    nodes = nx.draw_networkx_nodes(
        G, pos, 
        node_color="lightblue", 
        edgecolors="black",
        linewidths=0.8,
        ax=ax
    )

    # 始终显示节点ID
    nx.draw_networkx_labels(
        G, pos,
        labels={n: str(n) for n in G.nodes()},  # 显示节点ID
        font_size=9,
        font_color="black",
        font_weight="light",
        ax=ax
    )

    

    # 绘制边（带箭头）
    edges = nx.draw_networkx_edges(G, pos, edge_color=edge_colors, arrows=True, arrowstyle="->", ax=ax)

    # 交互式标注功能
    annot_node = ax.annotate("", xy=(0,0), 
                            xytext=(15,15),  # 调整偏移量避免遮挡ID
                            textcoords="offset points", 
                            bbox=dict(boxstyle="round", fc="w", alpha=0.9),
                            fontsize=10,
                            visible=False)
    annot_edge = ax.annotate("", xy=(0,0),
                            xytext=(15,15),
                            textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w", alpha=0.9),
                            fontsize=10,
                            visible=False)
    
    def update_annot(event):
    # 新增：检查鼠标是否在坐标系内
        if event.inaxes != ax or event.xdata is None or event.ydata is None:
            annot_node.set_visible(False)
            annot_edge.set_visible(False)
            fig.canvas.draw_idle()
            return
        
        # 清除旧标注
        annot_node.set_visible(False)
        annot_edge.set_visible(False)
        
        # 检查节点悬停
        if nodes.contains(event)[0]:
            ind = nodes.contains(event)[1]["ind"][0]
            node = list(G.nodes)[ind]
            x, y = pos[node]
            annot_node.xy = (x, y)
            
            # 安全获取节点属性（修复KeyError）
            template = G.nodes[node].get('template', 'No template')
            params = G.nodes[node].get('params', [])  # 使用get方法提供默认值
            
            text = f"""
            Node ID: {node}
            Template: {template}
            Parameters: {', '.join(params) if params else 'None'}
            """
            annot_node.set_text(text)
            annot_node.set_visible(True)
        
        # 检查边悬停（修复后的计算逻辑）
        else:
            min_dist = float('inf')
            target_edge = None
            
            # 遍历所有边
            for (u, v) in G.edges():
                x1, y1 = pos[u]
                x2, y2 = pos[v]
                
                # 计算线段参数
                dx = x2 - x1
                dy = y2 - y1
                segment_length_sq = dx**2 + dy**2
                
                # 处理零长度边（避免除零错误）
                if segment_length_sq == 0:
                    continue
                    
                # 计算投影参数 t
                t = ((event.xdata - x1) * dx + (event.ydata - y1) * dy) / segment_length_sq
                t = max(0, min(1, t))  # 限制在[0,1]范围内
                
                # 计算最近点坐标
                proj_x = x1 + t * dx
                proj_y = y1 + t * dy
                
                # 计算距离
                dist = np.hypot(event.xdata - proj_x, event.ydata - proj_y)
                
                if dist < min_dist:
                    min_dist = dist
                    target_edge = (u, v)
            
            # 判断是否触发边悬停
            if min_dist < 0.05 and target_edge is not None:
                u, v = target_edge
                mid_x = (pos[u][0] + pos[v][0]) / 2
                mid_y = (pos[u][1] + pos[v][1]) / 2
                annot_edge.xy = (mid_x, mid_y)
                text = f"Edge ({u}→{v})\nDependency: {G[u][v]['dependency']}"
                annot_edge.set_text(text)
                annot_edge.set_visible(True)
        
        fig.canvas.draw_idle()

    # 绑定事件
    fig.canvas.mpl_connect("motion_notify_event", update_annot)

    # 添加图例
    legend_handles = [plt.Line2D([0], [0], color=color, lw=4, label=f"{dep_type}") 
                    for dep_type, color in edge_color_map.items()]
    plt.legend(handles=legend_handles, title="Dependency Types", 
            loc="upper right", bbox_to_anchor=(0.95, 1))
    # 显示图形
    plt.tight_layout()
    plt.show()


def visualize_graphs(subgraph_dict, max_cols=3, figsize=(20, 15)):
    """
    可视化叶子节点子图字典
    
    参数:
    subgraph_dict (dict): {叶子节点: nx.DiGraph} 的字典
    max_cols (int): 每行最大显示列数
    figsize (tuple): 画布尺寸
    """
    # 1. 准备布局参数
    n = len(subgraph_dict)
    if n == 0:
        print("警告：输入字典为空")
        return
    
    cols = min(max_cols, n)
    rows = ceil(n / cols)
    
    # 2. 创建画布
    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    if n == 1:
        axes = [[axes]]  # 统一处理单子图情况
    else:
        axes = axes.reshape(rows, cols)  # 确保二维索引
    
    # 3. 定义可视化参数  
    node_style = {
        'node_size': 100,
        'node_color': 'lightblue',
        'edgecolors': 'darkgrey',
        'linewidths': 0.7
    }
    
    # 4. 遍历每个子图
    for idx, (leaf, sg) in enumerate(subgraph_dict.items()):
        ax = axes[idx//cols][idx%cols]
        
        # 计算层次布局
        pos = hierarchical_layout(sg)
        
        # 绘制边
        edge_colors = []
        for u, v in sg.edges():
            edge_colors.append(edge_color_map.get(sg[u][v].get('dependency', 'view'), '#808080'))
        nx.draw_networkx_edges(sg, pos, ax=ax, edge_color=edge_colors, arrows=True, arrowstyle='->')
        
        # 绘制节点
        nx.draw_networkx_nodes(sg, pos, ax=ax, **node_style)
        
        # 简化标签显示
        labels = {n: f"{n}\n{sg.nodes[n].get('template','')[0][:25]}" 
                 for n in sg.nodes}
        nx.draw_networkx_labels(sg, pos, labels, ax=ax, font_size=6)
        
        # # 设置标题
        # ax.set_title(f"Leaf: {leaf}\nPaths: {len(list(nx.all_simple_paths(sg, 'configure', leaf)))}", 
        #             fontsize=10)
        # ax.axis('off')
    
    # 5. 处理多余的子图区域
    for idx in range(n, rows*cols):
        axes[idx//cols][idx%cols].axis('off')
    
    # 6. 添加图例
    # legend_handles = [
    #     plt.Line2D([0], [0], color=color, lw=4, label=label)
    #     for label, color in edge_color_map.items()
    # ]
    # fig.legend(handles=legend_handles, 
    #           title="Dependency Types",
    #           loc='lower right',
    #           bbox_to_anchor=(1, 0),
    #           framealpha=0.4)
    
    plt.tight_layout()
    plt.show()


def frequently_occured_nodes(x_labels, y_values):

    # 创建柱状图
    plt.figure(figsize=(10, 6))  # 设置画布大小
    bars = plt.bar(x_labels, y_values, color='skyblue', edgecolor='black', width=0.5)

    # 添加数据标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, 
                f'{height}', ha='center', va='bottom')

    # 自定义图表样式
    plt.title('Command Input Frequency per Configuration Node', fontsize=14, pad=20)
    plt.xlabel('模板节点', fontsize=9)
    plt.ylabel('频率', fontsize=9)
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # 添加横向网格线

    # 调整布局
    plt.tight_layout()
    plt.show()


def visualize_pyvis(G, remark=None):
    nt = Network(height="1000px", width="100%", directed=True, notebook=False)

    for node in G.nodes():
        # 基础节点设置
        node_label = G.nodes[node].get('label', '')
        
        # 特殊处理field="<cr>"的节点
        if node_label == "<cr>":
            nt.add_node(
                node,
                label=node_label,
                color="#c3c0c0",      # 灰色
                shape="diamond",      # 菱形
                size=8,             # 更小尺寸
                borderWidth=2,       # 边框宽度
                borderWidthSelected=4,
                font={"size": 14, "color": "white"},
                shadow={"enabled": True}
            )
        elif node_label == '<next-view>':
            nt.add_node(
                node,
                label=node_label,
                color="#ff0000",      # 红色
                shape="dot",      # 圆形
                size=20,             # 小尺寸
                font={"size": 12},
                shadow={"enabled": True}
            )
        else:
            nt.add_node(
                node,
                label=node_label,
                color="#97c2fc",      # 蓝色
                shape="dot",          # 圆形
                size=30,
                font={"size": 12}
            )


    for e in G.edges():
        nt.add_edge(e[0], e[1])

    nt.toggle_physics(True)
    nt.show_buttons(filter_=['physics'])
    
    if remark:
        nt.save_graph(f"dag_{remark}.html")
    else:
        nt.show("dag.html", notebook=False)


def visualize_svg(g, svg_path: str='test.svg'):

    for node in g.nodes:
        value = g.nodes[node]['label']
        if '.' in value or '<' in value or '>' in value:
            # 添加一个空格（注意：避免重复添加）
            g.nodes[node]['label'] = value + ' '

    dot_file = 'temp.dot'
    dag.graph2dot(g, dot_file)

    subprocess.run([DOT_PATH, "-Tsvg", dot_file, "-o", svg_path])

    os.remove(dot_file)




if __name__ == "__main__":

    # 【frequently_occured_nodes】
    # x_labels = ['4', '8', '61', '5', '56']  # 横轴标签（配置模板节点）
    # y_values = [113, 44, 15, 14, 6]         # 纵轴值（命令输入次数）
    # frequently_occured_nodes(x_labels, y_values)


    graph_name = "CLI echo\\sub-command\config\\router_ospf-backup.graphml"
    G = nx.read_graphml(graph_name)
    visualize_pyvis(G)
