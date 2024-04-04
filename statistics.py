from collections import Counter


def count_entities(input_file):
    mp = Counter()
    with open(input_file, 'r', encoding='utf-8') as f:
        cnt = 0

        for l in f.readlines():
            # 末尾会多空行。l = 'a O\n'
            line = l[:-1] if l[-1] == '\n' else l
            if len(line)==0:continue
            char_label = line.split(' ')[1]
            cnt += 1
            if char_label == 'O': continue
            tmp = char_label.split('-')
            # print(tmp, cnt)
            pos, entity = tmp[0], tmp[1]
            if pos == 'B':
                mp[entity] += 1
    print('The number of each entity in the file named 【%s】' % input_file, end='--->')
    print(sorted(list(mp.items())))


def count_sentences(input_file):
    cnt = 0
    with open(input_file, "r", encoding='utf-8') as file:
        for line in file.readlines():
            if line[0] in ['。']:
                cnt += 1
    # print(str)
    print('The length of sentences in the file named 【%s】 is %d' % (input_file, cnt))


if __name__ == '__main__':
    # Counter({'TYPE': 194, 'CASUALTY': 43, 'PROPERTYLOSS': 21})
    # count_entities('爆炸_2024-3-23_output.bio',['TYPE','PROPERTYLOSS','CASUALTY'])

    # Counter({'TYPE': 150, 'CASUALTY': 36, 'PROPERTYLOSS': 15})
    count_entities('爆炸_2024-3-23_train.bio')
    count_sentences('爆炸_2024-3-23_train.bio')
    # 训练集占比
    # Type:0.77,CASUALTY:0.83,PROPERTYLOSS:0.71

    count_sentences('爆炸_2024-3-23_test.bio')
