# coding:utf-8
import json
import LogID

conversation = LogID.getConversation()

# 获取Workspaces列表
def get_workspaces_list(conversation = conversation):
    workspaces = conversation.list_workspaces()
    jsonFile = json.dumps(workspaces, indent=2)
    # print(jsonFile)
    print ("================获取Workspaces列表成功==================")
    return jsonFile

# 测试
get_workspaces_list(LogID.getConversation())

# 创建Workspaces列表
# conversation.create_workspace



# 获取workspaces的ID
def get_workspace_id(conversation = conversation):
    workspaces = conversation.list_workspaces()
    # print type(workspaces)
    # print workspaces["workspaces"]
    return  workspaces["workspaces"][0]["workspace_id"]

# 测试
# print get_workspace_id(conversation)