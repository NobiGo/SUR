#coding=utf-8
import json
import sys
import os
import unicodedata
from collections import OrderedDict
reload(sys)
sys.setdefaultencoding("utf-8")
from ChangeJsonToTable import TransJsonToHtml

BASE_DIR=os.path.dirname(__file__)
#获取当前文件夹的绝对路径
file_path=os.path.join(BASE_DIR,u'高七七.json')
#获取当前文件夹内的Test_Data文件
Test_Data=open(file_path,"r")
#关闭文件
Test_Data.close()
#生成表格
TransJsonToHtml.createHtmlTable(file_path, BASE_DIR)
