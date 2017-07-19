# coding:utf-8
from watson_developer_cloud import ConversationV1

userName = "ebd18e93-acc7-4dac-98ea-9674e2ff973d"
passWord = "Afd2qew1Rxo4"
version  = "2017-07-14"

def getConversation(username=userName,password=passWord,version=version):
    conversation = ConversationV1(username=userName,password=passWord,version=version)
    return conversation
