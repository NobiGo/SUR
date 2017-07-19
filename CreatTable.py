#coding=utf-8
import json
import sys
import os
import unicodedata
from collections import OrderedDict
reload(sys)
sys.setdefaultencoding("utf-8")
from ChangeJsonToTable import TransJsonToHtml
#from  CreateJsonFile import ReadFileToDict
#ReadFileToDict.ReadFileToDict("0test.text")
TransJsonToHtml.createHtmlTable(u"病历/陈力豪.json",os.path.dirname(__file__))
