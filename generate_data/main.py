import statistics
from data_process import preprocess

# preprocess.txt_to_txt('数据.txt', '数据_solved.txt')

from 全角转半角 import AllCornerCharacterProcessor

# AllCornerCharacterProcessor().solve_file('数据_solved.txt', '数据_solved2.txt')

from autoLabeling import main

# main.AutoLabelingProcesser().solve_file('数据_solved2.txt','数据_solved3.json')

# 人工标注。。。

# 导出
from jsonl2bio import jsonl2bio

# the length of sentences is 224
# jsonl2bio.jsonl2bio('数据.jsonl', '数据.bio')
# jsonl2bio.jsonl2bio('admin.jsonl', 'admin.bio')

# The length of sentences in the file named 【admin.bio】 is 224
# statistics.count_sentences('admin.bio')

# The number of each entity in the file named 【admin.bio】--->
# [('TIME', 85), ('LOC', 88), ('CLOSS', 197), ('OORG', 131), ('DATE', 162), ('OPER', 66), ('TYPE', 143), ('PORG', 6), ('LPER', 1), ('PLOSS', 2), ('PPER', 3)]
# statistics.count_entities('admin.bio')

# 人工筛bio后，将admin_solved.bio分为两个文件


# The number of each entity in the file named 【train.bio】--->
# [('TIME', 58), ('LOC', 63), ('CLOSS', 144), ('OORG', 87), ('DATE', 116), ('OPER', 39), ('TYPE', 104), ('PORG', 4), ('LPER', 1), ('PLOSS', 2)]

statistics.count_entities('train.bio')

# The number of each entity in the file named 【test.bio】--->
# [('OPER', 28), ('OORG', 43), ('DATE', 46), ('TIME', 27), ('LOC', 25), ('TYPE', 39), ('CLOSS', 53), ('PPER', 3), ('PORG', 2)]

statistics.count_entities('test.bio')