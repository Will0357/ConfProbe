import networkx as nx
import uuid
import scipy.sparse as sp
from pyvis.network import Network
import matplotlib.pyplot as plt
import math
from itertools import combinations
import sys
from datetime import datetime
import os


from utils.eve_drivers import *


################################################################################

def extract_previous_sentences(input_file, output_file, keyword="CHANGE VIEW"):
    """
    从文本文件中提取包含关键词的句子的上一句
    
    参数:
        input_file: 输入文件路径
        output_file: 输出文件路径
        keyword: 要查找的关键词(默认是"change view")
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    previous_sentences = []
    
    # 遍历句子(从第二句开始检查)
    for i in range(1, len(lines)):
        if keyword.lower() in lines[i].lower():
            previous_sentences.append(lines[i-1])
    
    # 将结果写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(previous_sentences))
    
    print(f"成功提取了{len(previous_sentences)}条符合条件的句子到{output_file}")


def extract_config_fields(input_file, output_file):
    """
    从配置命令模板文件中提取所有不同的字段
    
    :param input_file: 输入文件路径
    :param output_file: 输出文件路径
    """
    
    unique_fields = set()
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                # 查找所有匹配的字段
                fields = line.split()
                for field in fields:
                    unique_fields.add(field)
        
        # 将字段按字母顺序排序
        sorted_fields = sorted(unique_fields)
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(sorted_fields))
            
        print(f"成功提取 {len(sorted_fields)} 个不同的配置字段，已保存到 {output_file}")
        
    except FileNotFoundError:
        print(f"错误：找不到输入文件 {input_file}")
    except Exception as e:
        print(f"处理文件时发生错误: {str(e)}")


def calculate_permutation():
    # 变体数量
    # k = [2, 1, 1, 1, 1, 1]
    # k = [2, 1, 3]
    k = [1, 1, 1, 1, 1, 1]
    n = len(k)

    total_paths = 0
    for m in range(n + 1):
        # 计算 e_m：所有大小为 m 的子集的变体数乘积之和
        e_m = sum(math.prod(comb) for comb in combinations(k, m))
        total_paths += math.factorial(m) * e_m

    print(f"总探索路径数: {total_paths}")
    # 输出: 总探索路径数: 3267




        


if __name__ == "__main__":
    # input = 'CLI echo\sub-command\config\\router_bgp-backup-old.log'
    # output = 'unique_fields.txt'
    
    # extract_config_fields(input, output)

    # calculate_permutation()
    r = IosModel('R1')
    x= 1


