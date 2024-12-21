from main import AutoLabelingProcesser
import unittest

# class TestAutoLabeling(unittest.TestCase):
def Test_batch_recognition():
    processor = AutoLabelingProcesser()
    processor.batch_recognition('test_data', 'test_data')

if __name__ == '__main__':
    Test_batch_recognition()

    # test.py
    pass

    # res = {"label": [[0, 10, "DATE"], [10, 17, "TIME"], [18, 21, "LOC"], [21, 24, "LOC"], [24, 27, "LOC"], [31, 39, "OORG"], [40, 42, "OPER"], [48, 56, "TIME"], [57, 60, "LOC"], [60, 63, "LOC"], [63, 66, "LOC"]], "text": "2023年12月1日上午8点12分,江苏省无锡市锡山区下雨了,江苏天坎有限公司的张三发生了事故。上午10点12分,江苏省无锡市锡山区雨停了。"}
    # tmp_label_array = []
    # for i, entity in enumerate(res['label']):
    #     if entity[2] in {'DATE':'aa'}:
    #         tmp_label_array.append(entity)
    # res['label'] = tmp_label_array
    # print(res)