# -*- coding:utf-8 -*-
import socket
from   concurrent.futures import ThreadPoolExecutor


from  multiprocessing import  Process,Pool

# 新建线程池
# 指定线程池大小
tasksize = 10
threadpool = ThreadPoolExecutor(max_workers=tasksize)

# 指定IP地址和端口号
ip_port = ('9.234.91.176',8080)

sk = socket.socket()
# 绑定地址（host,port）到套接字
sk.bind(ip_port)
# 开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。
sk.listen(5)

i = 0;

def threadProcess(conn,i):
    # 设置标记
    Flag = True
    saveFile = open("patientFile/" + str(i) + "test.text", "w")
    i = i + 1;
    print "开始读取客户端数据"
    while Flag:
        # 接受来自客户端的数据
        data = str(conn.recv(1024))
        if data:
            saveFile.write(data)
            saveFile.flush()
        else:
            Flag = False
    conn.close()
    saveFile.close()
    print "客户端读取完成，关闭文件操作"



while True:
    print "waiting for connection"
    # 接受客户端的连接
    conn,address =  sk.accept()
    print "...connection from",address
    threadpool.submit(threadProcess,conn,i)
    i = i+1

