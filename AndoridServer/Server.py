# -*- coding:utf-8 -*-

import socket

# 指定IP地址和端口号
ip_port = ('10.4.21.35',8888)

sk = socket.socket()
# 绑定地址（host,port）到套接字
sk.bind(ip_port)
# 开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。
sk.listen(5)

i = 0;

while True:
    print "waiting for connection"
    # 接受客户端的连接
    conn,address =  sk.accept()
    print "...connection from",address
    # 设置标记
    Flag = True
    saveFile = open(str(i)+"test.text","w")
    i=i+1;
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
