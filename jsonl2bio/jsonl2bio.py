import os


def convert_one_jsonl_to_bio(json_data: dict, bio_path):
    text = json_data['text']
    entities = json_data.get('entities', [])
    print(entities)
    bio_labels = ['O'] * len(text)  # Initialize with 'O' (Outside) for each character
    # "id": 0,
    # "start_offset": 0,
    # "end_offset": 6,
    # "label": "ORG"
    for entity in entities:
        print(entity)
        entity_type, start, end, = entity['label'], entity['start_offset'], entity['end_offset']
        print(entity_type, start, end)
        bio_labels[start] = f'B-{entity_type}'

        for i in range(start + 1, end):
            bio_labels[i] = f'I-{entity_type}'

    # Write the BIO-formatted onedata.txt to the output file
    with open(bio_path, 'a', encoding='utf-8') as bio_file:
        last = ''
        for char, label in zip(text, bio_labels):
            # print(char)
            if char == ' ':
                pass
            # elif char == '\n':
            #     if last != char:
            #         bio_file.write(f' \n')
            # elif char == '\n': # 处理换行符
            #     bio_file.write(f'  {label}\n')
            else:
                bio_file.write(f'{char} {label}\n')
            last = char
        bio_file.flush()


def test():
    json_data = {
        "id": 856,
        "text": "2019年11月，辽宁本溪南芬区思山岭华煤集团思山岭铁矿项目部措施井施工现场，运送炸药车辆在井口发生爆炸。经初查，事故造成地表人员11人死亡，9人受伤",
        "label": [[5, 10, "EVENT_NAME"], [15, 22, "EVENT_ACTION"]],
        "Comments": []
    }
    print(type(json_data))
    bio_path = "output.bio"
    convert_one_jsonl_to_bio(json_data, bio_path)


# 读入整个jsonl文件，转换成BIO格式，并在句子间加空行
def jsonl2bio(input_path, output_path):
    if os.path.exists(output_path):
        os.remove(output_path)
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            # line.
            # print(line)
            json_data = eval(line)  # str -> dict
            print(json_data)
            # print(json_data['label'])
            convert_one_jsonl_to_bio(json_data, output_path)

    def split_sentences(input_file, output_file):
        cnt = 0
        str = ''
        with open(input_file, "r", encoding='utf-8') as file:
            for line in file.readlines():
                # print(line)
                str += line
                if line[0] in ['。']:
                    str += '\n'
                    cnt += 1
        # print(str)
        print('the length of sentences is %d' % cnt)

        with open(output_file, "w", encoding='utf-8') as out:
            out.write(str)
            out.flush()

    # BIO格式要求句子间插入空行
    split_sentences(output_path, output_path)  # 修改源文件


if __name__ == "__main__":
    # test()
    input_path = "../data_process/爆炸_2024-3-23_solved.jsonl"
    # input_path = "test.jsonl"
    output_path = "../data_process/爆炸_2024-3-23_output.bio"
    # output_path = "output_test.bio"
    jsonl2bio(input_path, output_path)
