# -*- coding: UTF-8 -*-
import pandas as pd
import pymysql
import MySQLdb
import MySQLdb.cursors
import collections
import json
from sqlalchemy import create_engine
from CreateJsonFile import ReadFileToDict
from collections import OrderedDict

def MysqlMerged(id):

    #数据库连接
    conn = MySQLdb.connect(host="127.0.0.1",user="root",passwd="123456",
                       db="hospital",charset='utf8',cursorclass = MySQLdb.cursors.DictCursor)
    #游标
    cur = conn.cursor()

    #转换类型以匹配键值
    x=int(id)
    #执行数据库的操作cur.execute
    sql = "select * from sur_app_patient_test where patientID =%d"%(x)
    cur.execute(sql)

    #获取病人口述病历
    id_str = str(id)
    filename = id_str + "test.text"
    # print filename
    dict1 = OrderedDict()
    dict1 = ReadFileToDict.ReadFileToDict(filename)

    #获取检查结果
    rows = OrderedDict()
    # rows=cur.fetchall()
    dict_0 = OrderedDict()
    dict_0=cur.fetchall()
    #解决乱序问题，使用键值对的方法，由键名字来获取数据
    for row in dict_0:
        #patientID,blood_sugar,blood_pressure,glucose_in_urine,Glucose_tolerance,Insulin,temperature
        rows["patientID"] =row["patientID"]
        rows["blood_sugar"] = row["blood_sugar"]
        rows["blood_pressure"] = row["blood_pressure"]
        rows["glucose_in_urine"] = row["glucose_in_urine"]
        rows["Glucose_tolerance"] = row["Glucose_tolerance"]
        rows["patientID"] = row["patientID"]
        rows["Insulin"] = row["Insulin"]
        rows["temperature"] = row["temperature"]

    #口述病情与检查结果进行合并
    dictMerged2=OrderedDict()
    dictMerged2 = dict1.copy()
    dictMerged2.update(rows)
    # dictMerged2 =Dict(dict1, **rows)
    #以json格式输出
    # print json.dumps(dictMerged2, sort_keys=0, indent=4, ensure_ascii=False)
    # return dictMerged2
    def TranDicToTxt(dic):
        rt = []
        fp = open("../AndoridServer/patientFile/"+filename, 'w')
        for (k, v) in dic.items():
            fp.write('%s：%s\n' % (k, v))
        fp.close()
    TranDicToTxt(dictMerged2)
# MysqlMerged(1)