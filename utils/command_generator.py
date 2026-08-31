import json
import random
import string
import rstr


# 【参数池】
PARA_POOL = {   
    "48b-address": [
        "0002.7D1A.9472",
        "1234.5678.90ab",
        "fedc.ba98.7531"
    ],
    "interface-type": [
        "GigabitEthernet"
    ],
    "ipv4": [
        "172.16.23.0",
        "172.29.52.28",
        "10.1.1.0",
        "10.1.4.255"
    ],
    "ipv4-address/mask": [
        "192.168.1.27 255.255.255.0",
        "192.168.6.6 255.255.255.0",
        "10.26.3.4/16",
        "10.3.32.154/8"
    ],
    "ipv6":[
        "2001:0DB8:0:1::",
        "FE80::260:3EFF:FE11:6770",
        "fe80::203:fdff:fe1b:4501",
        "3::3"
    ],
    "ipv6/prefix-length": [
        "2001:0DB8:0::/64",
        "2025:312::1509/35",
        "0:0:0:7272::72/64",
        "5::1002:2003/22"
    ],
    "mask": [
        "255.255.255.0",
        "255.255.0.0",
    ],
    "point-to-point": [
        "loopback"
    ],
    
    "GigabitEthernet":[# 1,2,3,4
        "0/0/0/0",
        "0/0/0/1",  
        "0/0/0/2",  
        "0/0/0/3"
    ],
    "loopback":[# <0-2147483647>
        0,
        1,
        2,
        3,
    ],
    "max-packets": [# <1-50>  Percentage of total packets available in the system (default: 1000 packets)
        10,
        20,
        30,
        40,
    ],  
    "rack/slot/module": [# device
        "0/0/CPU0",
        "0/RP0/CPU0"
    ],
    "seconds1": [# <4-1800>  Maximum RA Interval (sec)
        10,
        20,
        30,
        40,
    ],
    "seconds2": [# <0-9000>  RA Lifetime (seconds)
        10,
        20,
        30,
        40,
    ],
    "scavenge-timeout": [# <1-43200>  RA Lifetime (seconds)
        10,
        20,
        30,
        40,
    ],
    "TenGigE": [# null
        "INVALID"
    ],
    "timeout": [# <1-120>  Number of seconds an assembly queue will hold before timeout
        10,
        20,
        30,
        40,
    ],
    "type instance": [# it depends but below are common commands
        "GigabitEthernet 0/0/0/0",
        "GigabitEthernet 0/0/0/1",
        "GigabitEthernet 0/0/0/2"
    ]
}


PARA_MAP = {
    'H.H.H': r'^([0-9A-Fa-f]{4}[.]){2}([0-9A-Fa-f]{4}[.])$',
    'interface-type': 'GigabitEthernet',
    'A.B.C.D': r''
}


def get_instances(tree_json, file_path='test/test_instance.txt'):
    """
    生成模板实例，并保存在配置文件中
    无返回值
    """

    instance_list = []  # 【3.31 保存生成的所有实例】

    def process_node_for_list(node, result_list=None):
        if result_list is None:
            result_list = []
        
        # 将当前节点加入结果列表（如果不存在）
        if node not in result_list:
            result_list.append(node)
        
        # 递归处理子节点
        if node["children"]:
            for child in node["children"]:
                process_node_for_list(child, result_list)
        
        return result_list
    
    def compare_indexes(index1, index2):
        if not index1 or not index2:
            raise ValueError(f"Invalid index format: index1='{index1}', index2='{index2}'")
        
        try:
            parts1 = list(map(int, index1.split('_')))
            parts2 = list(map(int, index2.split('_')))
            
            for p1, p2 in zip(parts1, parts2):
                if p1 < p2:
                    return -1
                elif p1 > p2:
                    return 1
            return 0
        except ValueError:
            raise ValueError(f"Invalid index format: Unable to convert to integers. index1='{index1}', index2='{index2}'")

    def get_next_node(current_index, nodes_list):
        try:
            # 添加输入验证
            if not nodes_list:
                return None
                
            # 过滤掉无效的节点
            valid_nodes = [n for n in nodes_list if 'index' in n]
            if not valid_nodes:
                return None
                
            # 获取候选节点
            candidates = []
            for node in valid_nodes:
                try:
                    if compare_indexes(node['index'], current_index) > 0:
                        candidates.append(node)
                except Exception as e:
                    print(f"Warning: Error comparing indexes: {node['index']} vs {current_index}")
                    continue
                    
            if not candidates:
                return None
                
            # 找出最小的下一个节点
            min_node = candidates[0]
            for node in candidates[1:]:
                if compare_indexes(node['index'], min_node['index']) < 0:
                    min_node = node
                    
            return min_node
            
        except Exception as e:
            print(f"Error in get_next_node: current_index={current_index}")
            print(f"Nodes indexes: {[n.get('index', 'NO_INDEX') for n in nodes_list]}")
            raise

    def get_last_node(current_index, nodes_list, nearest=False):    # 【3.30 如果nearest为真，最近节点优先】
        candidates = [n for n in nodes_list if compare_indexes(n['index'], current_index) < 0]
        
        if not candidates:
            return None
        
        # 找出最大的前一个节点
        max_node = candidates[0]
        if nearest:
            for node in candidates[1:]:
                # 如果当前节点不小于max_node，则更新max_node，即最近节点优先
                if compare_indexes(node['index'], max_node['index']) >= 0:
                    max_node = node
        else:
            for node in candidates[1:]:
                # 如果当前节点比max_node大，则更新max_node，即最远节点优先
                if compare_indexes(node['index'], max_node['index']) > 0:
                    max_node = node
        
        return max_node    

    def generate_para_instance(para_info, current_string=""):
        if isinstance(para_info, str):                                  # 字符串类型,在参数池中随机获取
            if para_info == '?':                                                    # 参数解析错误
                para_instance = "INVALID"
            elif para_info == '!':                                                  # 参数取值依赖于前一个参数的类型
                words = current_string.strip().split()
                last_word = words[-1] if words else ""
                para_instance = random.choice(PARA_POOL[last_word])
            elif para_info == 'name':                                               # 参数是name，生成随机字符串
                para_instance = ''.join(random.sample(string.ascii_letters, 7))
            elif para_info in PARA_POOL:                                            # 参数是预定义类型，从参数池中选择一个实例
                para_instance = random.choice(PARA_POOL[para_info])  
            else:
                raise ValueError("关键词未找到")
        elif isinstance(para_info, list):                               # 列表类型,从列表中获取
            if any(isinstance(item, list) for item in para_info):                   # 参数是二维列表，说明参数有多种类型
                para_instance = generate_para_instance(para_info[0], current_string)            # 迭代访问，这里先默认只处理列表中第一个
                
            elif para_info[0] == 'int':                                             # 参数是数字，从给定的范围中选择
                para_instance = random.randint(para_info[1],para_info[2])
            elif (para_info[0] in PARA_POOL) and isinstance(para_info[1], int):     # 参数是预定义类型，从参数池中选择x个实例
                x = random.randint(para_info[1], min(para_info[2], len(PARA_POOL[para_info[0]])))   # 确保 x 不超过列表长度
                x_list = random.sample(PARA_POOL[para_info[0]], k=x)
                para_instance = " ".join(map(str, x_list))
            else:                                                                   # 参数是有限集合，从集合中选择
                para_instance = random.choice(para_info)
        else:
            raise ValueError("para类型错误")

        return para_instance

    def write_to_file(current_string, path='test/test_instance.txt'):
        print(current_string)
        with open(path, 'a', encoding='utf-8') as file:
            file.write(current_string)
            file.write('\n')
    
    def get_node(node, current_string="", nodes_list=[]):      

        if node['type'] == 'parameter':  # 【匹配parameter】   

            para_instance = generate_para_instance(node['ParaInfo'], current_string)

            current_string += str(para_instance) + " "
                            
            next_node = get_next_node(node['index'], nodes_list)
            if next_node:
                get_node(next_node, current_string, nodes_list)
            else:
                raise ValueError('json缺失END')
        
        
        elif node['type'] == 'keyword':  # 【匹配keyword】                      
            
            current_string += node['name'] + " "
            next_node = get_next_node(node['index'], nodes_list)
            if next_node:
                get_node(next_node, current_string, nodes_list)
            else:
                raise ValueError(node['name'])


        elif node['type'] == 'select':
            if 'visited' not in node['ParaInfo']:
                segments = []
                current_segment = []
                for child in node['children']:
                    if child['type'] == 'OR':
                        if current_segment:
                            segments.append(current_segment[:])
                            current_segment = []
                    else:
                        current_segment.append(child)
                if current_segment:
                    segments.append(current_segment[:])

                # 尝试每个选择分支
                for segment in segments:
                    if segment:
                        get_node(segment[0], current_string, nodes_list)
                    if segment == segments[-1]:
                        node['ParaInfo'].append('visited')

            else:   # 【3.31 若已全部遍历过，之后再经过时默认走第一个分支】
                for child in node['children']:
                    if child['type'] == 'keyword' or child['type'] == 'parameter':
                        get_node(child, current_string, nodes_list)
                        break
                    

        elif node['type'] == 'option':
            
            # 尝试进入option  (👈 随着游走推进，如果[option]中的内容能匹配上，则一定会自动走到 [option]之后的*(Loop)那里，之后执行Loop的逻辑)            
            valid_children = node['children']  
            if valid_children:
                get_node(valid_children[0], current_string, nodes_list)     # 【走select的逻辑】
      
            
            # 尝试跳过option （【20241207  update】   考虑后面可能有'*'(Loop)，如果要跳，判断后面有没有'*'，有的话一起跳过  ---  否则会【 [] <--> * 】往返递归 --> 死循环）  
            if 'visited' not in node['ParaInfo']:         
                next_node = get_next_node(node['index'], nodes_list)
                if ((next_node['type'] == "Loop") or (next_node['type'] == "limitedLoop")):
                    next_node = get_next_node(next_node['index'], nodes_list)
                if next_node:
                    get_node(next_node, current_string, nodes_list)
                    node['ParaInfo'].append('visited')                      # 【3.31 若已全部遍历过，之后再经过时默认走第一个分支】


        elif node['type'] == "OR":
            parts_current_index = node['index'].split('_')
            parent_index = '_'.join(parts_current_index[:-1])
            next_node = get_next_node(parent_index, nodes_list)
            if next_node:
                get_node(next_node, current_string, nodes_list)
            
        
        elif node['type'] == "Loop":
            
            # 获取下一个节点和最近的上一个节点
            next_node = get_next_node(node['index'], nodes_list)
            last_node = get_last_node(node['index'], nodes_list, nearest=True)
        
            
            if "visited" not in node['ParaInfo']:
                # 回到循环起始处（继续 *循环）策略暂为再生成一个和前一个分支中最后那个相同的实例(这里默认*前面必然存在至少一个分支？)
                while True:
                    if last_node['type'] == 'keyword' or last_node['type'] == 'parameter':
                        node['ParaInfo'].append('visited')
                        get_node(last_node, current_string, nodes_list)
                        break
                    else:
                        last_node = get_last_node(last_node['index'], nodes_list, nearest=True)
                
                get_node(next_node, current_string, nodes_list)             
            else:
                # 继续向前匹配（跳出 *循环）
                if next_node:
                    get_node(next_node, current_string, nodes_list)
                else:
                    raise ValueError('json缺失END')
  

        elif node['type'] == "limitedLoop":
            
            # 解析字段 && 初始化该节点的计数器
            node_id = node['index']  # 使用节点的index作为唯一标识符
            node_name = node['name']

            # 解析 node_name 获取 m 和 n
            if node_name.startswith('&<') and node_name.endswith('>'):
                # 提取 "<m-n>" 中的数字部分
                numbers_part = node_name[2:-1]  # 去掉 "&<" 和 ">"
                try:
                    m, n = map(int, numbers_part.split('-'))
                    if m > 0 and n > 0 and m <= n:  # 确保 m 和 n 是正整数且 m <= n
                        floor = m  # 设置最小循环次数
                        ceiling = n  # 设置最大循环次数
                except ValueError:
                    raise ValueError(f"Invalid limitedLoop format: {node_name}. It's index is [{node_id}]")

            
            next_node = get_next_node(node['index'], nodes_list)
            last_node = get_last_node(node['index'], nodes_list)
        
            # 最小次数跳出循环 &<m-n>
            if floor > 1:
                for i in range(floor-1):
                    current_string += str(generate_para_instance(last_node['ParaInfo'], current_string)) + ' '
            get_node(next_node, current_string, nodes_list)

            if 'visited' not in node['ParaInfo']:
                node['ParaInfo'].append('visited')  
                # 最大次数跳出循环 &<m-n>             
                for i in range(ceiling-floor):
                    current_string += str(generate_para_instance(last_node['ParaInfo'], current_string)) + ' '
                get_node(next_node, current_string, nodes_list)
        

        else:  # root 和 brackets, 暂时越过了括号部分
            next_node = get_next_node(node['index'], nodes_list)
            if next_node:
                get_node(next_node, current_string, nodes_list)
            else:   # 【这里是最终输出出口】
                # write_to_file(current_string)
                # print(current_string)
                instance_list.append(current_string)


    # 主逻辑开始
    all_nodes = process_node_for_list(tree_json)
    get_node(tree_json, nodes_list=all_nodes)

    return instance_list



######################################################################


def get_instances_complete(tree_json, file_path='test/test_instance.txt'):
    """
    生成模板实例，并保存在配置文件中
    无返回值
    """

    instance_list = []  # 【3.31 保存生成的所有实例】

    def process_node_for_list(node, result_list=None):
        if result_list is None:
            result_list = []
        
        # 将当前节点加入结果列表（如果不存在）
        if node not in result_list:
            result_list.append(node)
        
        # 递归处理子节点
        if node["children"]:
            for child in node["children"]:
                process_node_for_list(child, result_list)
        
        return result_list
    
    def compare_indexes(index1, index2):
        if not index1 or not index2:
            raise ValueError(f"Invalid index format: index1='{index1}', index2='{index2}'")
        
        try:
            parts1 = list(map(int, index1.split('_')))
            parts2 = list(map(int, index2.split('_')))
            
            for p1, p2 in zip(parts1, parts2):
                if p1 < p2:
                    return -1
                elif p1 > p2:
                    return 1
            return 0
        except ValueError:
            raise ValueError(f"Invalid index format: Unable to convert to integers. index1='{index1}', index2='{index2}'")

    def get_next_node(current_index, nodes_list):
        try:
            # 添加输入验证
            if not nodes_list:
                return None
                
            # 过滤掉无效的节点
            valid_nodes = [n for n in nodes_list if 'index' in n]
            if not valid_nodes:
                return None
                
            # 获取候选节点
            candidates = []
            for node in valid_nodes:
                try:
                    if compare_indexes(node['index'], current_index) > 0:
                        candidates.append(node)
                except Exception as e:
                    print(f"Warning: Error comparing indexes: {node['index']} vs {current_index}")
                    continue
                    
            if not candidates:
                return None
                
            # 找出最小的下一个节点
            min_node = candidates[0]
            for node in candidates[1:]:
                if compare_indexes(node['index'], min_node['index']) < 0:
                    min_node = node
                    
            return min_node
            
        except Exception as e:
            print(f"Error in get_next_node: current_index={current_index}")
            print(f"Nodes indexes: {[n.get('index', 'NO_INDEX') for n in nodes_list]}")
            raise

    def get_last_node(current_index, nodes_list, nearest=False):    # 【3.30 如果nearest为真，最近节点优先】
        candidates = [n for n in nodes_list if compare_indexes(n['index'], current_index) < 0]
        
        if not candidates:
            return None
        
        # 找出最大的前一个节点
        max_node = candidates[0]
        if nearest:
            for node in candidates[1:]:
                # 如果当前节点不小于max_node，则更新max_node，即最近节点优先
                if compare_indexes(node['index'], max_node['index']) >= 0:
                    max_node = node
        else:
            for node in candidates[1:]:
                # 如果当前节点比max_node大，则更新max_node，即最远节点优先
                if compare_indexes(node['index'], max_node['index']) > 0:
                    max_node = node
        
        return max_node    

    def generate_para_instance(para_info, current_string=""):
        if isinstance(para_info, str):                                  # 字符串类型,在参数池中随机获取
            if para_info == '?':                                                    # 参数解析错误
                para_instance = "INVALID"
            elif para_info == '!':                                                  # 参数取值依赖于前一个参数的类型
                words = current_string.strip().split()
                last_word = words[-1] if words else ""
                para_instance = random.choice(PARA_POOL[last_word])
            elif para_info == 'name':                                               # 参数是name，生成随机字符串
                para_instance = ''.join(random.sample(string.ascii_letters, 7))
            elif para_info in PARA_POOL:                                            # 参数是预定义类型，从参数池中选择一个实例
                para_instance = random.choice(PARA_POOL[para_info])  
            else:
                raise ValueError("关键词未找到")
        elif isinstance(para_info, list):                               # 列表类型,从列表中获取
            if any(isinstance(item, list) for item in para_info):                   # 参数是二维列表，说明参数有多种类型
                para_instance = generate_para_instance(para_info[0], current_string)            # 迭代访问，这里先默认只处理列表中第一个
                
            elif para_info[0] == 'int':                                             # 参数是数字，从给定的范围中选择
                para_instance = random.randint(para_info[1],para_info[2])
            elif (para_info[0] in PARA_POOL) and isinstance(para_info[1], int):     # 参数是预定义类型，从参数池中选择x个实例
                x = random.randint(para_info[1], min(para_info[2], len(PARA_POOL[para_info[0]])))   # 确保 x 不超过列表长度
                x_list = random.sample(PARA_POOL[para_info[0]], k=x)
                para_instance = " ".join(map(str, x_list))
            else:                                                                   # 参数是有限集合，从集合中选择
                para_instance = random.choice(para_info)
        else:
            raise ValueError("para类型错误")

        return para_instance

    def write_to_file(current_string, path='test/test_instance.txt'):
        print(current_string)
        with open(path, 'a', encoding='utf-8') as file:
            file.write(current_string)
            file.write('\n')
    
    def get_node(node, current_string="", nodes_list=[]):      

        if node['type'] == 'parameter':  # 【匹配parameter】   

            para_instance = generate_para_instance(node['ParaInfo'], current_string)

            current_string += str(para_instance) + " "
                            
            next_node = get_next_node(node['index'], nodes_list)
            if next_node:
                get_node(next_node, current_string, nodes_list)
            else:
                raise ValueError('json缺失END')
        
        
        elif node['type'] == 'keyword':  # 【匹配keyword】                      
            
            current_string += node['name'] + " "
            next_node = get_next_node(node['index'], nodes_list)
            if next_node:
                get_node(next_node, current_string, nodes_list)
            else:
                raise ValueError(node['name'])


        elif node['type'] == 'select':
            segments = []
            current_segment = []
            for child in node['children']:
                if child['type'] == 'OR':
                    if current_segment:
                        segments.append(current_segment[:])
                        current_segment = []
                else:
                    current_segment.append(child)
            if current_segment:
                segments.append(current_segment[:])

            # 尝试每个选择分支
            for segment in segments:
                if segment:
                    get_node(segment[0], current_string, nodes_list)
                    

        elif node['type'] == 'option':
            
            # 尝试进入option  (👈 随着游走推进，如果[option]中的内容能匹配上，则一定会自动走到 [option]之后的*(Loop)那里，之后执行Loop的逻辑)            
            valid_children = node['children']  
            if valid_children:
                get_node(valid_children[0], current_string, nodes_list)     # 【走select的逻辑】
      
            
            # 尝试跳过option （【20241207  update】   考虑后面可能有'*'(Loop)，如果要跳，判断后面有没有'*'，有的话一起跳过  ---  否则会【 [] <--> * 】往返递归 --> 死循环）         
            next_node = get_next_node(node['index'], nodes_list)
            if ((next_node['type'] == "Loop") or (next_node['type'] == "limitedLoop")):
                next_node = get_next_node(next_node['index'], nodes_list)
            if next_node:
                get_node(next_node, current_string, nodes_list)
                    

        elif node['type'] == "OR":
            parts_current_index = node['index'].split('_')
            parent_index = '_'.join(parts_current_index[:-1])
            next_node = get_next_node(parent_index, nodes_list)
            if next_node:
                get_node(next_node, current_string, nodes_list)
            
        
        elif node['type'] == "Loop":
            
            # 获取下一个节点和最近的上一个节点
            next_node = get_next_node(node['index'], nodes_list)
            last_node = get_last_node(node['index'], nodes_list, nearest=True)
        
        
            # 回到循环起始处（继续 *循环）策略暂为再生成一个和前一个分支中最后那个相同的实例(这里默认*前面必然存在至少一个分支？)
            while True:
                if last_node['type'] == 'keyword' or last_node['type'] == 'parameter':
                    get_node(last_node, current_string, nodes_list)
                    break
                else:
                    last_node = get_last_node(last_node['index'], nodes_list, nearest=True)
            
            get_node(next_node, current_string, nodes_list)             
  

        elif node['type'] == "limitedLoop":
            
            # 解析字段 && 初始化该节点的计数器
            node_id = node['index']  # 使用节点的index作为唯一标识符
            node_name = node['name']

            # 解析 node_name 获取 m 和 n
            if node_name.startswith('&<') and node_name.endswith('>'):
                # 提取 "<m-n>" 中的数字部分
                numbers_part = node_name[2:-1]  # 去掉 "&<" 和 ">"
                try:
                    m, n = map(int, numbers_part.split('-'))
                    if m > 0 and n > 0 and m <= n:  # 确保 m 和 n 是正整数且 m <= n
                        floor = m  # 设置最小循环次数
                        ceiling = n  # 设置最大循环次数
                except ValueError:
                    raise ValueError(f"Invalid limitedLoop format: {node_name}. It's index is [{node_id}]")

            
            next_node = get_next_node(node['index'], nodes_list)
            last_node = get_last_node(node['index'], nodes_list)
        
            # 最小次数跳出循环 &<m-n>
            if floor > 1:
                for i in range(floor-1):
                    current_string += str(generate_para_instance(last_node['ParaInfo'], current_string)) + ' '
            get_node(next_node, current_string, nodes_list)

            # 最大次数跳出循环 &<m-n>             
            for i in range(ceiling-floor):
                current_string += str(generate_para_instance(last_node['ParaInfo'], current_string)) + ' '
            get_node(next_node, current_string, nodes_list)
        

        else:  # root 和 brackets, 暂时越过了括号部分
            next_node = get_next_node(node['index'], nodes_list)
            if next_node:
                get_node(next_node, current_string, nodes_list)
            else:   # 【这里是最终输出出口】
                # write_to_file(current_string)
                # print(current_string)
                instance_list.append(current_string)


    # 主逻辑开始
    all_nodes = process_node_for_list(tree_json)
    get_node(tree_json, nodes_list=all_nodes)

    return instance_list


####################################################################################################################


# 使用示例
if __name__ == "__main__":
    parsed_template_tree_path = "test/test_template.json"  # 👈 template的CLI-struc文件
    
    
    with open(parsed_template_tree_path, 'r', encoding='utf-8') as f:
        tree_json = json.load(f)
    
    # instances = get_instances_complete(tree_json)
    instances = get_instances(tree_json)
    for instance in instances:
        print(instance)
