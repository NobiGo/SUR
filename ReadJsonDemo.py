# coding=utf-8


import json

# 解决不能读取中文文件名问题
fileName = "/Users/dx/Documents/GitHub/SUR/高七七的病历.json"
filePath = fileName.decode("UTF-8")
fileContent = open(filePath,"r")
patientInfo = fileContent.read()
# 显示文件的编码格式
# print chardet.detect(patientInfo)
# 关闭文件
fileContent.close()
print patientInfo
# 读取json文件
content = json.loads(patientInfo,encoding="utf-8")

#  print chardet.detect("姓名")
print content["姓名".decode("utf-8")]
print content["职业".decode("utf-8")]
print content["性别".decode("utf-8")]
print content["入院时间".decode("utf-8")]
print content["年龄".decode("utf-8")]
print content["记录时间".decode("utf-8")]
print content["民族".decode("utf-8")]
print content["发病节气".decode("utf-8")]
print content["婚姻状况".decode("utf-8")]
print content["病史陈述者".decode("utf-8")]
print content["出生地".decode("utf-8")]
print content["主诉".decode("utf-8")]
print content["病史".decode("utf-8")]
print content["婚育史".decode("utf-8")]
print content["家族史".decode("utf-8")]

d = {"姓名": "高七七",
  "职业": "退休教师",
  "性别": "女",
  "入院时间": "2010年09月13日12时",
  "年龄": "63岁",
  "记录时间": "2010年09月13日13时",
  "民族": "汉族",
  "发病节气": "白露",
  "婚姻状况": "已婚",
  "病史陈述者": "患者本人",
  "出生地": "北京市宣武区",
  "主诉": "间断乏力、口干4年，加重伴双下肢疼痛2周",
  "现病史": "患者2006年8月无明显诱因出现乏力、口干欲饮、就诊于**医院，查空腹血糖9.3mmol／L，餐后血糖15.2mmol／L，尿糖（+++），胰岛功能检测显示胰岛素分泌高峰延缓。诊断为“2型糖尿病”，予阿克波糖片50mg tid po，患者乏力，口干欲饮等症状明显缓解，血糖控制良好。2009年，患者劳累后出现乏力、口渴等症加重，血糖控制不佳，餐后血糖最高达17mmol／L，于我院住院治疗，住院期间胰岛素诺和灵30R早14u晚8u餐前皮下注射控制血糖，患者症状缓解、血糖控制平稳后出院。出院后患者坚持注射胰岛素，空腹血糖波动在5～6mmol／L，餐后血糖在7～9mmol／L之间。2周前，患者再次出现乏力、口渴症状加重，伴双下肢乏力、疼痛，步行5～10分钟需休息片刻方能继续行走，患者就诊于我院门诊，查空腹血糖9.5mmol／L；尿常规：尿糖1000mg／dl，尿酮体 （一），尿蛋白（一）；下肢血管超声：双下肢动脉硬化伴斑状形成，患者为求进一步系统诊治及中医药治疗，收入我科。刻下症；乏力，口干欲饮，时有胸闷，无头晕头痛，双下肢乏力，疼痛，饮食控制，眠可，小便频，夜尿1～2次／夜，大便干，1日1行。",
  "既往史": "既往有高血压病史4年，最高血压达170/100mmHg，目前口服硝苯地平缓释片10mg bid控制血压，血压维持在140/85mmHg左右，否认冠心病等其他慢性病史，否认肝炎，结核等传染病史，否认手术外伤史、输血史，否认药物及食物过敏史。",
  "个人史": "患者出生于北京，久居本地，居住环境和条件良好，未到过自然疫源地及地方病流行区，否认粉尘、毒物、放射性物质接触史。否认饮酒史。有吸烟史，5支／日。",
  "婚育史": "21岁结婚，配偶体健，育1子1女，子女体健。",
  "家族史": "否认相关疾病家族遗传病史"}
def generate_tr(name, score):
    #if score > 90:
     #   return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)


tds = [generate_tr(name, score) for name, score in d.iteritems()]

# 定义生成表格


# 新建文件用于保存病历

newFile = open("/Users/dx/Documents/GitHub/SUR/name.html", 'w+');
print >>newFile,'<table width="800" border="1" align="center" cellpadding="0">'
print >>newFile,'<tr ><th >入院记录</th >'
print >>newFile,'\n'.join(tds)
print >>newFile,'</table>'
newFile.close()

print "创建完成"