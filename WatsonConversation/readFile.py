# coding:utf-8
import MessageTools

# File: readline-example-1.py
file = open("patientfile")
while 1:
    line = file.readline()
    if not line:
        break
    else:
        line =  line.strip('\n')
        print  MessageTools.getResult(textFile=line)