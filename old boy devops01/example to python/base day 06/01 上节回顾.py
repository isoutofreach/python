'''
模块:
本质是一个.py文件
分类:
1. 解释器模块: time模块
2. python库模块： python 自带模块
3. 第三方模块: 用pip下载
4. 自定义模块: 自己写的一些功能模块
使用方法:
1. import   2. form 文件名 import 模块名
调用顺序:
解释器内置模块 --> sys.path:[执行文件所在目录,本地python库]

包:
本质上是一个带有__init__文件的文件夹
'''
import re

#
ret = re.findall("y..n?", "'123','yuan','yu,n','yubn','yuabn','34','rain','56','789'")
print(ret)

# search : 查询匹配到第一个结果,返回（返回一个对象）
ret = re.search("(?P<xieyi>https?)://www\.[a-zA-Z0-9]+\.(?:com|cn)",
                "http://www.baidu.com,https://www.jd.com,http://www.python.cn")
print(ret)  # 打印结果: <_sre.SRE_Match object; span=(0, 20), match='http://www.baidu.com'>
print(ret.group("xieyi"))  # 打印结果: http
# 用?P<> 来给分组起名，在调用对象的时候，可以取出对应分组

# match :匹配的规则必须在字符串的第一个匹配到,否则返回空
ret = re.match("(?P<xieyi>https?)://www\.[a-zA-Z0-9]+\.(?:com|cn)",
               "hello world,http://www.baidu.com,https://www.jd.com,http://www.python.cn")
print(ret)  # 打印结果: None
