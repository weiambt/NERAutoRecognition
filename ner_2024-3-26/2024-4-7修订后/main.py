from jsonl2bio import jsonl2bio

# jsonl2bio.jsonl2bio('process/GJC.jsonl', 'process/GJC.bio')
# jsonl2bio.jsonl2bio('process/TXG.jsonl', 'process/TXG.bio')


import statistics
# [('CLOSS', 63), ('DATE', 117), ('DLOC', 39), ('GPE', 118), ('LAW', 4), ('LORG', 1), ('LPER', 148), ('OORG', 38), ('OPER', 2), ('PLOSS', 15), ('PORG', 35), ('PPER', 116), ('TIME', 81), ('TYPE', 112)]
statistics.count_entities('process/GJC.bio')
# [('CLOSS', 96), ('DATE', 78), ('DLOC', 52), ('GPE', 133), ('LAW', 7), ('LPER', 22), ('OORG', 22), ('OPER', 1), ('PLOSS', 32), ('PORG', 62), ('TIME', 83), ('TYPE', 154)]
statistics.count_entities('process/TXG.bio')


# [('CLOSS', 159), ('DATE', 195), ('DLOC', 91), ('GPE', 251), ('LAW', 11), ('LORG', 1), ('LPER', 170), ('OORG', 60), ('OPER', 3), ('PLOSS', 47), ('PORG', 97), ('PPER', 116), ('TIME', 164), ('TYPE', 266)]
statistics.count_entities('train.bio')