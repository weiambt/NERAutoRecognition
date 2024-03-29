from collections import Counter

def count_entities(input_file, entities):
    mp = Counter()
    with open(input_file, 'r', encoding='utf-8') as f:
        cnt = 0

        for l in f.readlines():
            # 末尾会多空行。l = 'a O\n'
            line = l[:-1] if l[-1] == '\n' else l
            char_label = line.split(' ')[1]
            cnt += 1
            if char_label == 'O': continue
            tmp = char_label.split('-')
            print(tmp, cnt)
            pos, entity = tmp[0], tmp[1]
            if entity in entities and pos == 'B':
                mp[entity] += 1
    print(mp)


def count_sentences(input_file):
    cnt = 0
    with open(input_file, "r", encoding='utf-8') as file:
        for line in file.readlines():
            if line[0] in ['。']:
                cnt += 1
    # print(str)
    print('the length of sentences is %d' % cnt)


if __name__ == '__main__':
    # Counter({'TYPE': 194, 'CASUALTY': 43, 'PROPERTYLOSS': 21})
    # count_entities('爆炸_2024-3-23_output.bio',['TYPE','PROPERTYLOSS','CASUALTY'])

    # Counter({'TYPE': 150, 'CASUALTY': 36, 'PROPERTYLOSS': 15})
    count_entities('爆炸_2024-3-23_train.bio', ['TYPE', 'PROPERTYLOSS', 'CASUALTY'])
    count_sentences('爆炸_2024-3-23_train.bio')
    # 训练集占比
    # Type:0.77,CASUALTY:0.83,PROPERTYLOSS:0.71

    count_sentences('爆炸_2024-3-23_test.bio')
