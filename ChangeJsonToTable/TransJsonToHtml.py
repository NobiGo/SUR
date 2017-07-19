# coding=utf-8
import json
import sys
import unicodedata
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding("utf-8")


def createHtmlTable(jsonFileName, destPath):
    # 读取文件内容
    content = readJsonFile(jsonFileName)
    # 生成html文件
    geberate_html(destPath, content)

# 读取Json文件
def readJsonFile(fileName):
    fileContent = open(fileName, "r")
    patientInfo = fileContent.read()
    # 关闭文件
    fileContent.close()
    # 读取json文件，并保持健有序
    content = json.loads(patientInfo, encoding="utf-8", object_pairs_hook=OrderedDict)
    return content

#  生成表格内容
def generate_tr(name, value):
    return '<tr><td width="100px">%s</td><td>%s</td></tr>' % (name, value)

# 生成html文件
def geberate_html(destPath, content):
    keyValue = [generate_tr(name, content[name]) for name in content.keys()]
    # 定义生成表格
    # 新建文件用于保存病历
    newFile = open(destPath + content[u"姓名"] + ".html", 'w+');
    print >> newFile, '<table width="800" border="1" align="center" cellpadding="0">'
    print >> newFile, '<center><h1 text-align:center>入院记录</h1></center>'
    print >> newFile, '\n'.join(keyValue)
    print >> newFile, '</table>'
    newFile.close()
    print "创建完成"
