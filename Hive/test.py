#coding:utf-8
import pyhs2

with pyhs2.connect(host='192.168.3.75',
                   port=10007,
                   # authMechanism='NONE',
                   authMechanism='NOSASL',
                   user='hdfs',
                   password='',
                   database='sur')as conn:
    with conn.cursor() as cur:
        #Show databases
        print cur.getDatabases()
        #Execute query 
        # cur.execute("")

        # cur.execute(sqlCreat)
        #Return column info from query  
        print cur.getSchema()
        #Fetch table results  
        for i in cur.fetch():
            print i
