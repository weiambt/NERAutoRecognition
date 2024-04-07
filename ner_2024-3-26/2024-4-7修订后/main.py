from jsonl2bio import jsonl2bio

jsonl2bio.jsonl2bio('process/GJC.jsonl', 'process/GJC.bio')
jsonl2bio.jsonl2bio('process/TXG.jsonl', 'process/TXG.bio')


import statistics
# [('CLOSS', 63), ('DATE', 117), ('DLOC', 39), ('GPE', 118), ('LAW', 4), ('LORG', 1), ('LPER', 148), ('OORG', 38), ('OPER', 2), ('PLOSS', 15), ('PORG', 35), ('PPER', 116), ('TIME', 81), ('TYPE', 112)]
statistics.count_entities('process/GJC.bio')
# [('CLOSS', 96), ('DATE', 78), ('DLOC', 52), ('GPE', 133), ('LAW', 7), ('LPER', 22), ('OORG', 22), ('OPER', 1), ('PLOSS', 32), ('PORG', 62), ('TIME', 83), ('TYPE', 154)]
statistics.count_entities('process/TXG.bio')

# a = dict(
#     [('CLOSS', 81), ('DATE', 313), ('LAW', 18), ('LOC', 33), ('LORG', 21), ('LPER', 284), ('OORG', 101), ('OPER', 61),
#      ('PLOSS', 24), ('PORG', 65), ('PPER', 235), ('TIME', 280), ('TYPE', 134)])
# b = dict(
#     [('CLOSS', 121), ('DATE', 169), ('LAW', 19), ('LOC', 37), ('LORG', 8), ('LPER', 54), ('OORG', 78), ('OPER', 21),
#      ('PLOSS', 36), ('PORG', 152), ('PPER', 228), ('TIME', 266), ('TYPE', 167)])
#
# for x in a:
#     a[x] += b[x]
# print(sorted(list(a.items())))
# [('CLOSS', 202), ('DATE', 482), ('LAW', 37), ('LOC', 70), ('LORG', 29), ('LPER', 338), ('OORG', 179), ('OPER', 82), ('PLOSS', 60), ('PORG', 217), ('PPER', 463), ('TIME', 546), ('TYPE', 301)]