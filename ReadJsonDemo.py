# coding=utf-8
import json
import chardet

# 解决不能读取中文文件名问题
fileName = "高七七的病历.json"
filePath = fileName.decode("UTF-8")
fileContent = open(filePath,"r")
patientInfo = fileContent.read()
# 显示文件的编码格式
print chardet.detect(patientInfo)
# 关闭文件
fileContent.close()
print patientInfo
# 读取json文件
content = json.loads(patientInfo,encoding="utf-8")

#  print chardet.detect("姓名")
print content["姓名".decode("utf-8")]
print content["出生地".decode("utf-8")]