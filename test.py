#coding=utf-8
import json
import sys
import os
import unicodedata
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding("utf-8")

from CreateJsonFile import TransDictToJson
from ChangeJsonToTable import TransJsonToHtml

BASE_DIR=os.path.dirname(__file__)
#获取当前文件夹的绝对路径
file_path=os.path.join(BASE_DIR,"AppTxtToTxt.txt")
#获取当前文件夹内的Test_Data文件
Test_Data=open(file_path,"r")

#按行来获取病人信息以及对话内容
lnum = 0
with open("AppTxtToTxt.txt") as fd:
    for line in fd:
        lnum += 1
        if(lnum >= 1)&(lnum <= 5):
           # for lnum in range(1, 5, 1):
                if (lnum == 1):
                   strName=TransDictToJson.GetInformationName(line)
                elif (lnum== 2):
                    strSex = TransDictToJson.GetInformationName(line)
                elif (lnum == 3):
                    strAge = TransDictToJson.GetInformationName(line)
                elif (lnum==4):
                    strAddress = TransDictToJson.GetInformationName(line)
                else:
                    strDialog = TransDictToJson.GetInformationName(line)
#关闭文件
Test_Data.close()

#传递病人信息并且调用函数转成json

TransDictToJson.ReInformation(strName, strSex, strAge, strAddress, strDialog)

#由JSON生成表格
BASE_DIR=os.path.dirname(__file__)
#获取当前文件夹的绝对路径
file_path=os.path.join(BASE_DIR,"GAO.json")
#生成表格
TransJsonToHtml.createHtmlTable(file_path,BASE_DIR)