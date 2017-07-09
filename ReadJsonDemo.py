# coding=utf-8
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 解决不能读取中文文件名问题
fileName = "高七七的病历.json"
filePath = unicode(fileName,"utf8")
fileContent = open(filePath,"r")
patientInfo = fileContent.read()
# 关闭文件
fileContent.close()
print patientInfo
# 读取json文件
content = json.loads(patientInfo,encoding="utf-8")
print content['姓名']
