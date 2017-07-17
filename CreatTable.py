#coding=utf-8
import json
import sys
import unicodedata
from collections import OrderedDict
from JsonToTable_Package import transJsonToHtml
reload(sys)
sys.setdefaultencoding("utf-8")

file = "C:\Users\IBM_ADMIN\Documents\GitHub\SUR\高七七的病历.json".decode("utf-8")

destFile = "C:\Users\IBM_ADMIN\Documents\GitHub\SUR".decode("utf-8")

# print  type("C:\Users\IBM_ADMIN\Documents\GitHub\SUR\高七七的病历.json")

transJsonToHtml.createHtmlTable(file, destFile)
