
def pre_process(input_path,output_path):

    with open(input_path,'r',encoding='utf-8') as f:
        with open(output_path,'a',encoding='utf-8') as out:
            for line in f.readlines():
                new_line = ''
                i = 0
                while i < len(line):
                    # if line[i]==' ':
                    #     i += 1
                    #     continue
                    if i<len(line)-1 and line[i:i+2]=='\/':
                        new_line += '/'
                        i += 2
                    else:
                        new_line += line[i]
                        i += 1
                out.write(new_line)
            out.flush()
if __name__ == '__main__':

    # input_path = "all_2023-11-29.jsonl"
    input_path = "../data_process/爆炸_2024-3-23.jsonl"
    # output_path = "all_processed_2023-12-06.jsonl"
    output_path = "../data_process/爆炸_2024-3-23_solved.jsonl"
    pre_process(input_path,output_path)
