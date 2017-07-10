# coding=utf-8
d = { 'Adam': 95, 'Lisa': 98, 'Bart': 100 }

# 定义生成表格
def generate_tr(name, score):
        if score > 90:
            return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.iteritems()]

# 新建文件用于保存病历
newFile = open("name.html", 'w+');
print >>newFile,'<table border="1">'
print >>newFile,'<tr><th>Name</th><th>Score</th><tr>'
print >>newFile,'\n'.join(tds)
print >>newFile,'</table>'