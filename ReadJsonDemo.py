# coding=utf-8

import json
import sys
import unicodedata
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding("utf-8")

# 解决不能读取中文文件名问题
fileName = u"/Users/dx/Documents/GitHub/SUR/高七七的病历.json"
fileContent = open(fileName, "r")
patientInfo = fileContent.read()
# 关闭文件
fileContent.close()
# 读取json文件
content = json.loads(patientInfo, encoding="utf-8", object_pairs_hook=OrderedDict)


def generate_tr(name, value):
    return '<tr><td width="100px">%s</td><td>%s</td></tr>' % (name, value)


keyValue = [generate_tr(name, content[name]) for name in content.keys()]

# 定义生成表格

# 新建文件用于保存病历

newFile = open("/Users/dx/Documents/GitHub/SUR/" + content[u"姓名"] + ".html", 'w+');
print >> newFile, '<table width="800" border="1" align="center" cellpadding="0">'
print >> newFile, '<center><h1 text-align:center>入院记录</h1></center>'
print >> newFile, '\n'.join(keyValue)
print >> newFile, '</table>'
newFile.close()

print "创建完成"
