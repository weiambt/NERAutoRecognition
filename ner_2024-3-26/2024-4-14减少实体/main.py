import statistics
# 清除其他的实体类型
def removeEntities(input,output,saved_entities):
    with open(input, 'r', encoding='utf') as infile:
        with open(output, 'w', encoding='utf') as outfile:
            for line in infile:
                print(line)
                if line == '\n':
                    outfile.write(line)
                    continue
                ss = line.split(' ')
                # 是否要修改
                flag = 1
                for x in saved_entities:
                    if x in ss[1]:
                        flag = 0
                        break
                if flag:
                    ss[1] = 'O\n'
                s = ss[0] + " " + ss[1]
                outfile.write(s)


if __name__ == '__main__':
    # removeEntities('train.bio','train_solved.bio',{'TYPE', 'CLOSS', 'PLOSS'})

    statistics.count_entities('train_solved.bio')
    # [('CLOSS', 159), ('PLOSS', 47), ('TYPE', 266)]