# coding:utf-8
import LogID
import ToolsWorkspaces
import json
import watson_developer_cloud

conversation = LogID.getConversation()


# 获得intent的列表
def get_intents_list(conversation=LogID.getConversation(), workspace_id=ToolsWorkspaces.get_workspace_id()):
    listIntents = conversation.list_intents(ToolsWorkspaces.get_workspace_id(conversation))
    # print  type(listIntents)
    # print json.loads(listIntents,encoding="utf-8",indent = 2)
    # 获得特定intent
    # conversation.get_intent()
    intents_list = []
    for keys in listIntents:
        if keys == "intents":
            for item in listIntents[keys]:
                intents_list.append(item["intent"])
    print "成功获得列表"
    return intents_list


# 测试
# listIntents = get_intents_list()
# for item  in listIntents:
#     print  item

# 得到特定语境的测试用例

# 获得特定intent的信息
# 返回 dict
def get_intent(conversation=LogID.getConversation(), workspace_id=ToolsWorkspaces.get_workspace_id(), intent="口干"):
    return conversation.get_intent(workspace_id, intent=intent)


# 返回特定intent的example

def list_example(conversation=LogID.getConversation(), workspace_id=ToolsWorkspaces.get_workspace_id(), intent="口干"):
    exampleDict = conversation.list_examples(workspace_id, intent=intent)
    listExample = []
    for item in exampleDict["examples"]:
        listExample.append(item["text"])
    return listExample


# 测试
# for item in list_example():
#   print item

# 将example添加到特定Intent
def add_example(intent,text,conversation = LogID.getConversation(),workspace_id = ToolsWorkspaces.get_workspace_id()):
    try:
        conversation.create_example(workspace_id, intent, text)
        print "添加成功"
    except watson_developer_cloud.watson_developer_cloud_service.WatsonException:
        print "被重复添加"
        pass
    return "Ok"
# 测试用例
add_example(intent="口干",text="口干啊啊啊啊啊啊啊啊")

