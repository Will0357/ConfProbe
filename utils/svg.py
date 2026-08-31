import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
import os
import re

def create_sample_dag():
    """创建一个示例有向无环图（使用英文节点名避免编码问题）"""
    G = nx.DiGraph()
    
    # 使用英文节点名，避免编码问题
    edges = [
        ('DataSource', 'DataCleaning'), ('DataSource', 'DataValidation'),
        ('DataCleaning', 'FeatureExtraction'), ('DataValidation', 'FeatureExtraction'),
        ('FeatureExtraction', 'ModelTraining'), ('FeatureExtraction', 'FeatureSelection'),
        ('FeatureSelection', 'ModelTraining'), ('ModelTraining', 'ModelEvaluation'),
        ('ModelEvaluation', 'ResultOutput'), ('ModelEvaluation', 'PerformanceAnalysis'),
        ('PerformanceAnalysis', 'ParameterTuning'), ('ParameterTuning', 'ModelTraining')
    ]
    
    G.add_edges_from(edges)
    
    # 添加节点属性（使用英文）
    node_attributes = {
        'DataSource': {'label': 'Data Source', 'color': 'lightgreen', 'shape': 'ellipse'},
        'DataCleaning': {'label': 'Data Cleaning', 'color': 'lightblue', 'shape': 'box'},
        'DataValidation': {'label': 'Data Validation', 'color': 'lightblue', 'shape': 'box'},
        'FeatureExtraction': {'label': 'Feature Extraction', 'color': 'lightyellow', 'shape': 'component'},
        'FeatureSelection': {'label': 'Feature Selection', 'color': 'lightyellow', 'shape': 'component'},
        'ModelTraining': {'label': 'Model Training', 'color': 'lightcoral', 'shape': 'folder'},
        'ModelEvaluation': {'label': 'Model Evaluation', 'color': 'lightpink', 'shape': 'tab'},
        'PerformanceAnalysis': {'label': 'Performance Analysis', 'color': 'lavender', 'shape': 'note'},
        'ParameterTuning': {'label': 'Parameter Tuning', 'color': 'lightcyan', 'shape': 'parallelogram'},
        'ResultOutput': {'label': 'Result Output', 'color': 'wheat', 'shape': 'doublecircle'}
    }
    
    for node, attrs in node_attributes.items():
        if node in G.nodes():
            G.nodes[node].update(attrs)
    
    return G

def sanitize_dot_attributes(G):
    """清理图属性，确保DOT语法正确"""
    # 创建一个干净的图副本
    G_clean = nx.DiGraph()
    
    # 添加节点（清理属性值）
    for node, attrs in G.nodes(data=True):
        clean_attrs = {}
        for key, value in attrs.items():
            # 确保值是字符串且不包含特殊字符
            if isinstance(value, str):
                # 移除可能引起语法错误的字符
                clean_value = re.sub(r'[^\w\s\-\.]', '', value)
                clean_attrs[key] = clean_value
            else:
                clean_attrs[key] = str(value)
        G_clean.add_node(node, **clean_attrs)
    
    # 添加边
    for u, v, attrs in G.edges(data=True):
        clean_attrs = {}
        for key, value in attrs.items():
            if isinstance(value, str):
                clean_value = re.sub(r'[^\w\s\-\.]', '', value)
                clean_attrs[key] = clean_value
            else:
                clean_attrs[key] = str(value)
        G_clean.add_edge(u, v, **clean_attrs)
    
    return G_clean

def visualize_with_dot_layout(G, output_file='dag_dot.svg'):
    """使用dot布局（层次化布局）"""
    try:
        # 清理图属性
        G_clean = sanitize_dot_attributes(G)
        
        # 转换为pydot图
        P = nx.nx_pydot.to_pydot(G_clean)
        
        # 设置基本属性（避免复杂属性）
        P.set('rankdir', 'TB')
        P.set('overlap', 'false')
        P.set('splines', 'true')
        
        # 简化节点显示
        for node in P.get_nodes():
            node.set('shape', 'box')
            node.set('style', 'filled')
            node.set('fillcolor', 'lightblue')
            # 移除可能引起问题的复杂属性
            if 'label' in node.obj_dict['attributes']:
                node.set('label', str(node.obj_dict['attributes']['label']))
        
        P.write_svg(output_file, encoding='utf-8')
        print(f"✓ dot布局已保存: {output_file}")
        return True
    except Exception as e:
        print(f"✗ dot布局失败: {e}")
        # 尝试更简单的方法
        return simple_visualization(G, output_file, 'dot')

def visualize_with_neato_layout(G, output_file='dag_neato.svg'):
    """使用neato布局（力导向布局）"""
    try:
        G_clean = sanitize_dot_attributes(G)
        P = nx.nx_pydot.to_pydot(G_clean)
        P.set('layout', 'neato')
        
        P.write_svg(output_file, encoding='utf-8')
        print(f"✓ neato布局已保存: {output_file}")
        return True
    except Exception as e:
        print(f"✗ neato布局失败: {e}")
        return simple_visualization(G, output_file, 'neato')

def visualize_with_twopi_layout(G, output_file='dag_twopi.svg'):
    """使用twopi布局（径向布局）"""
    try:
        G_clean = sanitize_dot_attributes(G)
        P = nx.nx_pydot.to_pydot(G_clean)
        P.set('layout', 'twopi')
        
        P.write_svg(output_file, encoding='utf-8')
        print(f"✓ twopi布局已保存: {output_file}")
        return True
    except Exception as e:
        print(f"✗ twopi布局失败: {e}")
        return simple_visualization(G, output_file, 'twopi')

def visualize_with_circo_layout(G, output_file='dag_circo.svg'):
    """使用circo布局（环形布局）"""
    try:
        G_clean = sanitize_dot_attributes(G)
        P = nx.nx_pydot.to_pydot(G_clean)
        P.set('layout', 'circo')
        
        P.write_svg(output_file, encoding='utf-8')
        print(f"✓ circo布局已保存: {output_file}")
        return True
    except Exception as e:
        print(f"✗ circo布局失败: {e}")
        return simple_visualization(G, output_file, 'circo')

def visualize_with_fdp_layout(G, output_file='dag_fdp.svg'):
    """使用fdp布局（力导向布局-无向图优化）"""
    try:
        G_clean = sanitize_dot_attributes(G)
        P = nx.nx_pydot.to_pydot(G_clean)
        P.set('layout', 'fdp')
        
        P.write_svg(output_file, encoding='utf-8')
        print(f"✓ fdp布局已保存: {output_file}")
        return True
    except Exception as e:
        print(f"✗ fdp布局失败: {e}")
        return simple_visualization(G, output_file, 'fdp')

def simple_visualization(G, output_file, layout_engine):
    """简化版可视化，避免属性问题"""
    try:
        # 创建最简单的DOT内容
        dot_lines = ['digraph G {']
        
        # 添加基本图形属性
        dot_lines.append('  rankdir=TB;')
        dot_lines.append('  node [shape=box, style=filled, fillcolor=lightblue];')
        dot_lines.append('  edge [arrowsize=0.8];')
        
        # 添加节点（只使用节点ID，不添加属性）
        for node in G.nodes():
            dot_lines.append(f'  "{node}";')
        
        # 添加边
        for u, v in G.edges():
            dot_lines.append(f'  "{u}" -> "{v}";')
        
        dot_lines.append('}')
        
        dot_content = '\n'.join(dot_lines)
        
        # 使用graphviz直接渲染
        import graphviz
        graph = graphviz.Source(dot_content, engine=layout_engine)
        graph.render(output_file.replace('.svg', ''), format='svg', cleanup=True)
        print(f"✓ {layout_engine}布局（简化版）已保存: {output_file}")
        return True
    except Exception as e:
        print(f"✗ {layout_engine}简化版也失败: {e}")
        return False

def debug_dot_generation(G):
    """调试DOT文件生成"""
    try:
        P = nx.nx_pydot.to_pydot(G)
        dot_content = P.to_string()
        print("生成的DOT内容:")
        print("=" * 50)
        print(dot_content)
        print("=" * 50)
        return dot_content
    except Exception as e:
        print(f"调试失败: {e}")
        return None

def visualize_all_layouts(G, output_dir='layout_results'):
    """使用所有可用布局引擎生成可视化"""
    
    # 创建输出目录
    Path(output_dir).mkdir(exist_ok=True)
    
    # 先调试DOT生成
    print("调试DOT文件生成...")
    debug_dot_generation(G)
    
    # 布局引擎配置
    layouts = {
        'dot': {'function': visualize_with_dot_layout, 'description': '层次化布局'},
        'neato': {'function': visualize_with_neato_layout, 'description': '力导向布局'},
        'fdp': {'function': visualize_with_fdp_layout, 'description': '力导向布局(优化)'},
        'twopi': {'function': visualize_with_twopi_layout, 'description': '径向布局'},
        'circo': {'function': visualize_with_circo_layout, 'description': '环形布局'}
    }
    
    print("开始生成多种布局的可视化...")
    print("=" * 50)
    
    results = {}
    for layout_name, config in layouts.items():
        output_file = Path(output_dir) / f'dag_{layout_name}.svg'
        success = config['function'](G, str(output_file))
        results[layout_name] = {
            'success': success,
            'file': output_file,
            'description': config['description']
        }
    
    return results

# 主程序
if __name__ == "__main__":
    # 创建示例图（使用英文节点名）
    print("创建示例有向图...")
    G = create_sample_dag()
    
    print(f"图信息: 节点数: {G.number_of_nodes()}, 边数: {G.number_of_edges()}")
    print("是否为有向无环图(DAG):", nx.is_directed_acyclic_graph(G))
    
    # 生成所有布局的可视化
    results = visualize_all_layouts(G)
    
    # 显示结果汇总
    print("\n" + "=" * 50)
    print("布局生成结果汇总:")
    print("=" * 50)
    
    for layout_name, result in results.items():
        status = "✓ 成功" if result['success'] else "✗ 失败"
        print(f"{layout_name:10} | {status:8} | {result['description']}")
        