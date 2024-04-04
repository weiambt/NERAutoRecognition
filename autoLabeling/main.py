import json
import os
from datetime import datetime

from hanlp_restful import HanLPClient


# zh中文，mul多语种

class AutoLabelingProcesser():
    # ENTITY_DICT = {'DATE': 'DATE', 'TIME': 'TIME', 'LOCATION': 'LOC', 'ORGANIZATION': 'PORG','PERSON': 'PPER'}
    # 我的数据
    # ENTITY_DICT = {'DATE': 'DATE', 'TIME': 'TIME', 'ORGANIZATION': 'PORG','PERSON': 'PPER'}
    # CEC数据
    ENTITY_DICT = {'DATE': 'DATE', 'TIME': 'TIME', 'ORGANIZATION': 'OORG', 'PERSON': 'OPER'}
    def __init__(self, task='ner/msra', entity_dict=ENTITY_DICT):
        self.HanLPClient = HanLPClient('https://www.hanlp.com/hanlp/v21/redirect', auth='6602ae18eaf668ab781b7e85',
                                       language='zh')
        assert task in ['ner/msra', 'ner/ontonotes', '/ner/pku']
        self.task = task
        self.entity_dict = entity_dict

    # 调用hanlp API进行抽取
    def recognition(self, text, my_output_format=True):

        # 根据recognition函数得到的分词信息的字典，去除分词信息，得到以文本为目标的实体数组的格式的dict
        def extractor_hanlp_json(hanlp_json: dict) -> dict:
            # hanlp接口得到的输出dict是带有分词词典的，所以要进一步解析
            token_array = hanlp_json['tok/fine']
            ner_array = hanlp_json['ner/msra']
            assert len(token_array) == len(ner_array)
            result = {'label': []}
            whole_text = ''
            whole_idx = 0
            for sentence, entities in zip(token_array, ner_array):
                # 存储sentence数组中，每个词的第一个元素在整个句子中下标
                token_array_start_val2_idx = []
                idx = 0
                text = ''
                # 计算sentence对应整个句子的下标
                for x in sentence:
                    token_array_start_val2_idx.append(idx)
                    idx += len(x)
                    text += x
                token_array_start_val2_idx.append(idx)
                # 枚举句子的所有实体
                for _, label, s, e in entities:
                    startIdx = whole_idx + token_array_start_val2_idx[s]
                    endIdx = whole_idx + token_array_start_val2_idx[e]
                    print(startIdx, endIdx, label, text[startIdx:endIdx])
                    result['label'].append([startIdx, endIdx, label])
                # 更新整个文本的下标和内容
                whole_text += text
                whole_idx += idx
            result['text'] = whole_text
            return result

        # 将extractor_hanlp_json的结果中所有实体类型根据字典entity_dict进行映射
        def match_entity_name(extractor_json: dict) -> dict:
            res = extractor_json.copy()

            # 去除所有Hanlp识别出来的但是我不需要的实体
            tmp_label_array = []
            for entity in res['label']:
                if entity[2] in self.entity_dict:
                    tmp_label_array.append([entity[0], entity[1],self.entity_dict[entity[2]]])
            res['label'] = tmp_label_array
            return res

        # 给dict的所有字符串都变成双引号
        def add_double_quotes(mp: dict) -> str:
            return json.dumps(mp, ensure_ascii=False)

        result = self.HanLPClient.parse(text, tasks=self.task)
        # print(result.pretty_print())
        ans = result.to_dict()
        if not my_output_format:
            return ans
        return add_double_quotes(match_entity_name(extractor_hanlp_json(ans)))

    def solve_file(self,input_file,output_file):
        whole_text = ''
        # 读入txt文件
        with open(input_file, 'r', encoding='utf-8') as f:
            for l in f.readlines():
                whole_text += l
        res = self.recognition(whole_text)
        print(res)
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(res + '\n')

    # 根据文件夹，批量识别
    def batch_recognition(self, input_folder, output_file):
        # if not os.path.exists(output_path):
        #     os.remove(output_path)
        for filename in os.listdir(input_folder):
            file_path = os.path.join(input_folder, filename)
            if os.path.isdir(file_path):
                self.batch_recognition(file_path, output_file)
            elif filename.endswith('.txt'):
                self.solve_file(file_path,output_file)


if __name__ == '__main__':
    processor = AutoLabelingProcesser()
    # print(autoLabeling.recognition('2023年12月1日上午8点12分，1月2日'))
    # print(autoLabeling.recognition('2023年12月1日上午8点12分，白银市白银区中山路13号发生火灾'))

    text = '2023年12月1日上午8点12分,江苏省无锡市锡山区下雨了,江苏天坎有限公司的张三发生了事故。上午10点12分,江苏省无锡市锡山区雨停了。'
    # for x in list(range(len(text))):
    #     print(x, end=',')
    # s = processor.recognition(text)
    # print(s)
    # sss = str(ss)
    # print(dict(sss))


    input = r'D:\APersonal\Agraduate\AinGroup\AProjects\NER\data_process\爆炸_txt'
    output = r'D:\APersonal\Agraduate\AinGroup\AProjects\NER\data_process\data2024-3-31.jsonl'
    processor.batch_recognition(input, output)