
import sys
from hive_service import ThriftHive
from hive_service.ttypes import HiveServerException
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def hiveExe(sql):
    try:
        transport = TSocket.TSocket('192.168.3.75', 10007)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = ThriftHive.Client(protocol)
        transport.open()

        client.execute(sql)

        print "The return value is : "
        resultSets=client.fetchAll()
        for j in range(len(resultSets)):
            print resultSets[j]
        print "............"
        transport.close()
    except Thrift.TException, tx:
        print '%s' % (tx.message)
        # return resultSets

if __name__ == '__main__':
    # hiveExe("show databases")
    # hiveExe("select * from aa limit 10")
    # print 2
    hiveExe("select * from wenqi")



# print 1