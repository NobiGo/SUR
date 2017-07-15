# coding=utf-8
import json
import sys
import unicodedata
import collections
import codecs
from collections import OrderedDict
reload(sys)
sys.setdefaultencoding("utf-8")

# 初始化词典
d=collections.OrderedDict()
d['a']="中文"
d['b']="英文"
d['c']="汉语"
for k,v in  d.items():
    print k,v
# 给词典赋值
#由orderdict转换成json
t = json.dump(d, open("dx" + ".json", 'w+'), skipkeys=False,
                  ensure_ascii=0, check_circular=True, allow_nan=True, cls=None, indent=0, separators=(',', ': '),
                  default=None, sort_keys=1)
#skipkeys（key的值不是基本类型str,unicode,int,long,float,bool,None时，设置为true）
#ensure_ascii（true时，\u的格式；false时，显示中文）
#indent（true时，一行；false时，分行）
#separators(分隔符)
#sort_key(根据keys 值排序)


#读取txt文件并且转成json文件
# def readtxt(txtname,txtpath,name):
#     f=open(txtname,'r')
#     str=f.read()
#     s=str.decode('gbk','ignore').encode('utf-8')
#     b=eval(f, encoding="utf-8", object_pairs_hook=OrderedDict)
#     for  item  in  b:
#         print  item
#     t = json.dump(b, open(txtpath +name + ".json", 'w+'), skipkeys=False,
#                   ensure_ascii=0, check_circular=True, allow_nan=True, cls=None, indent=0, separators=(',', ': '),
#                   default=None, sort_keys=1)
#readtxt("C:\Users\WXK\Desktop\SUR-master\SUR-master\GAOQIQI.txt", "C:\Users\WXK\Desktop\SUR-master\SUR-master", 'GAOQIQI')
