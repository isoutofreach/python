# 经典组合:  .*?  .+?
import re

# 取消贪婪匹配, 否则会匹配到最后一个</div>
ret = re.findall("<div class='c1'>.+?</div>", "<div><div class='c1'>yuan</div></div><div><div class='c2'></div></div>")
print(ret)

f = open("豆瓣.html","r",encoding="utf8")
data = f.read()

ret = re.findall('<div class="item">.*?<span class="title">(.+?)</span>', data, re.S)
print(ret)