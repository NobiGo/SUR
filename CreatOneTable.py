#coding=utf-8
import json
import sys
import unicodedata
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding("utf-8")

from JsonToTable_Package import transJsonToHtml
transJsonToHtml.createHtmlTable("/Users/dx/Documents/GitHub/SUR/高七七的病历.json", "/Users/dx/Documents/GitHub/SUR/")
