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
#s={"姓名": "会","婚":"打折"}
def TransDictToJson(dict):
    #print dict["姓名"]
    #for  item in dict.keys():
        #print item,dict[item]
    # 获取文件名
    # 由orderdict转换成json
   # t = json.dump(dict,open(u"../病历/"+dict["姓名"]+ ".json", 'w+'),ensure_ascii=0,check_circular=True,allow_nan=True, cls=None, indent=0, separators=(',', ': '),default=None, sort_keys=0)
    # open(u"../病历/"+dict["姓名"]+ ".json", 'w+'),
    with open(u"../病历/"+dict["姓名"]+ ".json", 'w+') as file:
        file.write(json.dumps(dict, sort_keys=0, indent=4, ensure_ascii=False))
        #print json.dumps(dict, sort_keys=True, indent=4, ensure_ascii=False)
        file.close()
#TransDictToJson(s)