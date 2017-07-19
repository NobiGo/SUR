# coding:utf-8
import LogID

import ToolsWorkspaces
# 获取链接
conversion = LogID.getConversation()

# print  conversion.list_workspaces().keys()

ToolsWorkspaces.get_workspaces_list(conversion)





