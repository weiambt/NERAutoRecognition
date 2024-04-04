

from jsonl2bio import jsonl2bio

jsonl2bio.jsonl2bio('source/GJC.jsonl','source/GJC.bio')
jsonl2bio.jsonl2bio('source/TXG.jsonl','source/TXG.bio')


import statistics
# [('CLOSS', 81), ('DATE', 313), ('LAW', 18), ('LOC', 33), ('LORG', 21), ('LPER', 284), ('OORG', 101), ('OPER', 61), ('PLOSS', 24), ('PORG', 65), ('PPER', 235), ('TIME', 280), ('TYPE', 134)]
statistics.count_entities('source/GJC.bio')

# [('CLOSS', 121), ('DATE', 169), ('LAW', 19), ('LOC', 37), ('LORG', 8), ('LPER', 54), ('OORG', 78), ('OPER', 21), ('PLOSS', 36), ('PORG', 152), ('PPER', 228), ('TIME', 266), ('TYPE', 167)]
statistics.count_entities('source/TXG.bio')