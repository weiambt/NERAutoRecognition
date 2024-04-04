import datetime

from hanlp_restful import HanLPClient
    #zh中文，mul多语种

HanLP = HanLPClient('https://www.hanlp.com/hanlp/v21/redirect', auth='6602ae18eaf668ab781b7e85', language='zh')

# HanLP.parse('晓美焰来到北京立方庭参观自然语义科技公司。', tasks='ner/msra').pretty_print()