# BIO中句子间需要加空行
def split_sentences(input_file, output_file):
    cnt = 0
    with open(input_file, "r", encoding='utf8') as file:
        str = ''
        for line in file.readlines():
            str += line
            if line[0] in ['。']:
                str += '\n'
                cnt += 1
    print('the length of sentences is %d' % cnt)
    with open(output_file, "w", encoding='utf8') as out:
        out.write(str)


if __name__ == '__main__':
    input_file = '爆炸_2024-3-23_train.bio'
    output_file = '爆炸_2024-3-23_train_solved2.bio'
    split_sentences(input_file, output_file)

    # input_file = '爆炸_2024-3-23_test.bio'
    # output_file = '爆炸_2024-3-23_test_solved.bio'
    # split_sentences(input_file, output_file)
