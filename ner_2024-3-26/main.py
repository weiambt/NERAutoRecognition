from jsonl2bio import jsonl2bio

# jsonl2bio.jsonl2bio('2024-3-31原始数据/GJC.jsonl','2024-3-31原始数据/GJC.bio')
# jsonl2bio.jsonl2bio('2024-3-31原始数据/TXG.jsonl','2024-3-31原始数据/TXG.bio')


import statistics

# [('CLOSS', 81), ('DATE', 313), ('LAW', 18), ('LOC', 33), ('LORG', 21), ('LPER', 284), ('OORG', 101), ('OPER', 61), ('PLOSS', 24), ('PORG', 65), ('PPER', 235), ('TIME', 280), ('TYPE', 134)]
# statistics.count_entities('2024-3-31原始数据/GJC.bio')

# [('CLOSS', 121), ('DATE', 169), ('LAW', 19), ('LOC', 37), ('LORG', 8), ('LPER', 54), ('OORG', 78), ('OPER', 21), ('PLOSS', 36), ('PORG', 152), ('PPER', 228), ('TIME', 266), ('TYPE', 167)]
# statistics.count_entities('2024-3-31原始数据/TXG.bio')

a = dict(
    [('CLOSS', 81), ('DATE', 313), ('LAW', 18), ('LOC', 33), ('LORG', 21), ('LPER', 284), ('OORG', 101), ('OPER', 61),
     ('PLOSS', 24), ('PORG', 65), ('PPER', 235), ('TIME', 280), ('TYPE', 134)])
b = dict(
    [('CLOSS', 121), ('DATE', 169), ('LAW', 19), ('LOC', 37), ('LORG', 8), ('LPER', 54), ('OORG', 78), ('OPER', 21),
     ('PLOSS', 36), ('PORG', 152), ('PPER', 228), ('TIME', 266), ('TYPE', 167)])

for x in a:
    a[x] += b[x]
print(sorted(list(a.items())))
# [('CLOSS', 202), ('DATE', 482), ('LAW', 37), ('LOC', 70), ('LORG', 29), ('LPER', 338), ('OORG', 179), ('OPER', 82), ('PLOSS', 60), ('PORG', 217), ('PPER', 463), ('TIME', 546), ('TYPE', 301)]