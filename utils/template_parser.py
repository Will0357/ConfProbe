import pyparsing as p
import json


"""

输入： 某个 IR-convention template (string)   --->   输出： CLI-struc (.json形式)

"""

para_dict = {}

# 定义 leaf_gen、select_gen、option_gen 和 ele_gen 函数
def leaf_gen(tokens):
    return [["leaf", {"name": tokens[0]}]]

def select_gen(tokens):
    return [["select", tokens[0].asList()]]  # 将标记为 "select"

def option_gen(tokens):
    return [["option", tokens[0].asList()]]  # 将标记为 "option"

def ele_gen(tokens):
    if tokens.asList() != []:
        return [["ele", tokens.asList()]]
    return tokens
 


##################################################################################
# 处理【parameter尖括号中的"意外空格"】

# 定义一个函数，用于清理尖括号中的参数
def clean_parameter(tokens):
    """
    将形如 '< str >' 的字段标准化为 '<str>'。
    :param tokens: pyparsing 捕获的 Token 列表，包含 "<", 参数内容, ">"。
    :return: 标准化后的参数，例如 '<str>'
    """
    # tokens 格式 ['<', '内容', '>']
    parameter_content = ''.join(tokens[1:-1]).strip()  # 提取内容并清理空格
    return f"<{parameter_content}>"

# 定义 "parameter"，即匹配形如 '<str>' 或 '< str >' 的字段
def create_parameter_parser():
    """
    创建一个 pyparsing 的解析器，用于匹配参数字段。
    """
    # 匹配开头的 "<"
    opening_bracket = p.Literal("<")
    
    # 匹配参数内容（可包含字母、数字和连字符）
    parameter_content = p.Word(p.alphanums + "-")
    
    # 匹配可选的空格
    optional_space = p.Optional(p.White(" \t"))
    
    # 匹配结尾的 ">"
    closing_bracket = p.Literal(">")

    # 使用 Group 分组，使中间内容作为单独的 token 捕获
    parameter_parser = (
        opening_bracket + optional_space + parameter_content + optional_space + closing_bracket
    ).setParseAction(clean_parameter)
    
    return parameter_parser


# 新增：处理 &<m-n> 格式的函数
def clean_limited_loop(tokens):
    """
    处理 &<m-n> 格式的符号
    """
    # tokens 格式 ['&', '<', 'm-n', '>']
    return ''.join(tokens)

# 新增：创建 limited_loop 解析器
def create_limited_loop_parser():
    """
    创建解析 &<m-n> 格式的解析器
    """
    amp = p.Literal("&")
    opening_bracket = p.Literal("<")
    # 匹配形如 "m-n" 的内容，其中 m 和 n 都是数字
    number_range = p.Word(p.nums) + p.Literal("-") + p.Word(p.nums)
    closing_bracket = p.Literal(">")

    limited_loop_parser = (
        amp + opening_bracket + number_range + closing_bracket
    ).setParseAction(clean_limited_loop)
    
    return limited_loop_parser


##################################################################################



# 定义递归深度的层次编号生成器
def generate_index(index_stack):
    return "_".join(map(str, index_stack))

# 定义树的节点类
class Node:
    def __init__(self, name, index, node_type, ParaInfo=None, children=None):
        self.name = name  # 节点名称
        self.index = index  # 节点索引
        self.type = node_type  # 节点类型
        
        # [20241209 新增👇]
        self.ParaInfo = ParaInfo if ParaInfo is not None else []  # 【仅对parameter类型节点有效】   [str1, str2, ...]
        
        self.children = children if children else []  # 子节点列表
        

    def add_child(self, child):
        """添加子节点"""
        self.children.append(child)
    
    def to_dict(self):
        """将节点转换为字典格式"""
        return {
            "name": self.name,
            "index": self.index,
            "type": self.type,
            "ParaInfo": self.ParaInfo, 
            "children": [child.to_dict() for child in self.children]
        }
    
    def __repr__(self, level=0):
        """格式化输出树结构"""
        indent = "  " * level
        # representation = f"{indent}Node(name={self.name}, index={self.index}, type={self.type})\n"
        representation = f"{indent}Node(name={self.name}, index={self.index}, type={self.type}, ParaInfo={self.ParaInfo})\n"
        for child in self.children:
            representation += child.__repr__(level +1)
        return representation

# 定义树类
class Tree:
    def __init__(self, root=None):
        self.root = root  # 树的根节点
    
    def to_dict(self):
        """将树转换为字典格式"""
        if self.root:
            return self.root.to_dict()
        return {}

# 定义解析动作
def recursive_parse_action(tokens, current_index, parent_node=None):
    result = []
    for i, item in enumerate(tokens):
        # 如果有父节点，则基于父节点构建新节点的索引；否则使用当前索引
        updated_index = current_index + [i + 1]
        
        if isinstance(item, list):
            # 如果子项是列表，则为特殊标记节点（如 select, option 等）
            if len(item) == 2 and isinstance(item[0], str):
                tag, content = item
                node_type = "select" if tag == "select" else "option" if tag == "option" else "keyword"
                node = Node(tag, generate_index(updated_index), node_type)
                # 递归处理子节点
                children = recursive_parse_action(content, updated_index, node)
                node.children.extend(children)
                result.append(node)
            else:
                # 普通列表，继续递归处理
                children = recursive_parse_action(item, updated_index)
                result.extend(children)
        else:
            # 处理叶子节点
            if item == "|":
                node = Node(item, generate_index(updated_index), "OR")
            
            # 👇 【20241207  update】
            elif item == "*":
                node = Node(item, generate_index(updated_index), "Loop")
            elif item.startswith("&<") and item.endswith(">"):
                node = Node(item, generate_index(updated_index), "limitedLoop")
                
            elif item.startswith("<") and item.endswith(">"):   # 【20250325  新增parainfo参数内容】
                node = Node(item, generate_index(updated_index), "parameter", ParaInfo=para_dict[item[1:-1]])
                # print(item + " " + str(para_dict[item[1:-1]]))
            elif item in ["{", "}", "[", "]"]:
                node = Node(item, generate_index(updated_index), "brackets")
            else:
                node = Node(item, generate_index(updated_index), "keyword")
            result.append(node)
    return result




# 初始化解析器
def initialize_parser():
    word = p.Word(p.printables, exclude_chars="{}[]#\n")
    star = p.Literal("*")
    limited_loop = create_limited_loop_parser()
    parameter = create_parameter_parser()
    ele = p.Forward()

    basic_element = parameter | star | limited_loop | word
    option = p.Group("[" + p.delimitedList(ele, "|") + "]").setParseAction(option_gen)
    select = p.Group("{" + p.delimitedList(ele, "|") + "}").setParseAction(select_gen)
    
    items = (basic_element | option | select)
    
    ele <<= p.OneOrMore(items)
    ####################################################################################################
    
    return ele



# 解析函数
def parse_with_indexing(command, para={}):
    global para_dict
    para_dict = para

    syntax_parser = initialize_parser()
    processed_command = command.replace("[", "[{").replace("]", "}]")
    parsed = syntax_parser.parseString(processed_command).asList()

    root_node = Node("root", "0", "root")
    children = recursive_parse_action(parsed, [], root_node)
    root_node.children.extend(children)

    end_index = 99999999
    end_node = Node("END", str(end_index), "END")
    root_node.add_child(end_node)

    return Tree(root_node)

def module_1_3__save_tree_to_json(tree, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(json.dumps(tree.to_dict(), indent=4))








if __name__ == "__main__":
    command = "clear access-list ipv4 <access-list-name>[<sequence-number> | hardware{ingress | egress}][interface <type><interface-path-id>][location <node-id> | sequence <number>]"
    # command = "[<sequence-number>] deny <source>[<source-wildcard>] counter <counter-name>[log | log-input]"
    para = {
        "access-list-name": "name",
        "sequence-number": ["int", 1, 2147483644],
        "type": "interface-type",
        "interface-path-id": "!",
        "node-id": "rack/slot/module",
        "number": ["int", 1, 2147483644],
        "text": "https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/ip-addresses/command/reference/b-ip-addresses-cr-asr9000/b-ipaddr-cr-asr9k_chapter_01.html#wp3748993831"
    }

    
    # 调用解析函数
    tree = parse_with_indexing(command, para)

    # 输出到文件
    output_path = "test/test_template.json"
    module_1_3__save_tree_to_json(tree, output_path)
    print(f"解析结果已保存到 {output_path}")