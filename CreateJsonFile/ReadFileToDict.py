#coding=utf-8
import json
import sys
import os
import unicodedata
import  collections
import TransDictToJson
from collections import OrderedDict


reload(sys)
sys.setdefaultencoding("utf-8")


def ReadFileToDict(name):
    #获取存储文件夹的相对路径
    Filepath_Direct = "AndoridServer/patientFile/"
    Filepath = os.path.join(Filepath_Direct,name)
    #获取当前文件夹内的Test_Data文件
    patientInfor=open(Filepath,"r")
    #按行来获取病人信息以及对话内容
    dict = collections.OrderedDict()
    Flag = True
    while Flag:
    # 接受来自客户端的数据
        data = patientInfor.readline()
        data.strip("\n")
        if data:
            value = data.split("：")
            dict[value[0]] = value[1].strip()
        else:
            Flag = False
            patientInfor.close()
    TransDictToJson.TransDictToJson(dict)