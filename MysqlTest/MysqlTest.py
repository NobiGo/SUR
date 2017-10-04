#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
from MysqlTools import Merged

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "hospital")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()
print "Database version : %s " % data

# 创建数据表SQL语句
# sqlCreat = """CREATE TABLE PATIENT (
#          patientID int primary key,
#          blood_sugar VARCHAR(20),
#          blood_pressure VARCHAR(20),
#          glucose_in_urine VARCHAR(20),
#          Glucose_tolerance VARCHAR(20),
#          Insulin VARCHAR(20),
#          temperature VARCHAR(20)
#          )"""
# cursor.execute(sqlCreat)
for i in range(1, 5):
    # # SQL 插入语句
    # sqlInsert = """INSERT INTO patient(patientID,blood_sugar,
    #               blood_pressure,glucose_in_urine,Glucose_tolerance,Insulin,temperature)
    #               VALUES (%d,"102mmol/L", "91kpa","79mmol/L","92mmol/L","89mmol/L","36.9C")""" % (i)
    # # print sqlInsert
    # try:
    #     # 执行sql语句
    #     cursor.execute(sqlInsert)
    #     # 提交到数据库执行
    #     db.commit()
    # except:
    #     # Rollback in case there is any error
    #     print  "异常"
    #     # db.rollback()

    #调用MysqlMerged()方法，实现病人口述文本与所插入检查结果的合并
    Merged.MysqlMerged(i)

# 关闭数据库连接
db.close()
