#coding=utf-8
import json
import sys
import os
import unicodedata
import  collections
import TransDictToJson
from collections import OrderedDict
from  WatsonConversation import MessageTools

reload(sys)
sys.setdefaultencoding("utf-8")


def ReadFileToDict(name):
    # 获取存储文件夹的相对路径
    Filepath_Direct = "../AndoridServer/patientFile/"
    Filepath = os.path.join(Filepath_Direct,name)
    # 获取当前文件夹内的Test_Data文件
    #print Filepath
    patientInfor=open(str(Filepath),"r")
    #按行来获取病人信息以及对话内容
    dict = collections.OrderedDict()
    Flag = True
    while Flag:
    # 接受来自客户端的数据
        data = patientInfor.readline()
        data.strip("\n")
        if data:
            value = data.split("：")
            if(value[0]==u"主诉"):
                dict[value[0]] = value[1].strip()
                #  print value[1]
                list = value[1].split("。")
                setvalue = set()
                for item in list:
                    # print unicode(item).encode("utf-8")
                    # print item.encode("utf-8")
                    # print  MessageTools.getResult(textFile=item.strip().decode("utf-8"))
                    value = MessageTools.getResult(textFile=item.strip())
                    if value:
                        setvalue.add(value)
                # print setvalue
                itemValue = ""
                for item in setvalue:
                      itemValue = itemValue+item+"、"
                dict[u"病情"] = itemValue
            else:
                dict[value[0]] = value[1].strip()
        else:
            Flag = False
            patientInfor.close()
    # for  item in  dict.keys():
    #     print  item
    TransDictToJson.TransDictToJson(dict)