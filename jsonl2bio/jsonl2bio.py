def convert_jsonl_to_bio(json_data:dict, bio_path):
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
        entity_type,start, end, = entity['label'], entity['start_offset'], entity['end_offset']
        print(entity_type, start, end)
        bio_labels[start] = f'B-{entity_type}'

        for i in range(start + 1, end):
            bio_labels[i] = f'I-{entity_type}'

    # Write the BIO-formatted onedata.txt to the output file
    with open(bio_path, 'a', encoding='utf-8') as bio_file:
        last = ''
        for char, label in zip(text, bio_labels):
            print(char)
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
        # bio_file.write('\n')
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
    convert_jsonl_to_bio(json_data, bio_path)

def jsonl2bio(jsonl_path, bio_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            # line.
            # print(line)
            json_data = eval(line)  # str -> dict
            print(json_data)
            # print(json_data['label'])
            convert_jsonl_to_bio(json_data, output_path)

if __name__ == "__main__":
    # test()
    input_path = "../data_process/爆炸_2024-3-23_solved.jsonl"
    # input_path = "test.jsonl"
    output_path = "../data_process/爆炸_2024-3-23_output.bio"
    # output_path = "output_test.bio"
    jsonl2bio(input_path, output_path)

