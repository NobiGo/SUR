# coding=utf-8
import json
import sys
import unicodedata
import collections
import codecs
from collections import OrderedDict
reload(sys)
sys.setdefaultencoding("utf-8")

#获取原始文本中的各字段
def GetInformationName(name):
    return name

# 初始化词典
def TransDictToJson(dict):
    #获取文件名
    #由orderdict转换成json
    t = json.dump(dict, open(u"病历/"+dict["姓名"]+ ".json", 'w+'), skipkeys=False,
                  ensure_ascii=0, check_circular=True, allow_nan=True, cls=None, indent=0, separators=(',', ': '),
                  default=None, sort_keys=0)

