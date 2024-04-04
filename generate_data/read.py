import os
# 批量打开500个文件，查看内容并选择
# debug模式运行这个程序，在18行加断点，

if __name__ == '__main__':
    input_floder = r'D:\APersonal\Agraduate\AinGroup\AProjects\NER\generate_data\CEC-Corpus_solved'
    cnt = 0
    for filename in os.listdir(input_floder):
        if filename.endswith('.txt'):
            print(cnt, filename)
            with open(os.path.join(input_floder, filename), 'r', encoding='utf-8') as f:
                cc = 0
                for x in f.readlines():
                    print(x)
                    cc += 1
                    if cc == 8: break
            cnt += 1
            print('------------------------next')
            ## id  198
