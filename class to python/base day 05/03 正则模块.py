import re

#################### 元字符 ##################

# （1）通配符 .    . ：除了换行符意外的任意符号,一个点代表一个字符,如果需要匹配换行符,需要在后面添加re.s
ret = re.findall("y..n", "hello yu\nn,hello rain,hello yabn", re.S)  # 以y开头n结尾，中间2个任意
print(ret)  # 打印结果:   ['yu\nn', 'yabn']

# （2）重复: *[0到无穷次]  +[1到无穷次]  ?[0到1次]  {} 指定范围
# 默认贪婪匹配   按照最长的字符串匹配方式
ret = re.findall("\d", "1,2,3,55,yuan,33")  # /d 只能代表一个数字
print(ret)  # 打印结果['1', '2', '3', '5', '5', '3', '3']

ret = re.findall("hi \d{2}", "hi 1,hi 66,hi 188")  # 匹配hi后面带2个数字的
print(ret)  # 打印结果: ['hi 66', 'hi 18']    因为1后面没有数字,匹配不到2位,所以不显示

ret = re.findall("hi \d*", "hi 1,hi 66,hi 188")  # 匹配hi后面带任意数字的,空也可以
print(ret)  # 打印结果:  ['hi 1', 'hi 66', 'hi 188']

# 取消贪婪在后面接?  取消贪婪: 按照最低的匹配
ret = re.findall("\d+?", "66,188,2,12222,hello")  # 匹配hi后面至少到一个数字的字符串
print(ret)  # 打印结果:  ['6', '6', '1', '8', '8', '2', '1', '2', '2', '2', '2']

ret = re.findall("hi \d?", "hi 1,hi 66,hi 188")  # 匹配hi后面带数字0次或者1次
print(ret)  # 打印结果:  ['hi 1', 'hi 6', 'hi 1']

# (3) 开头和结尾:  ^ $
ret = re.findall("^good/.{4}/.{4}", "hello/good/food/meat")  # 必须以good开头
print(ret)  # 结果为空

ret = re.findall("^good/.{4}/meat$", "good/food/meat/羊肉")  # 必须以meat结尾
print(ret)  # 结果为空

ret = re.findall("^good/.{4}/meat$", "good/food/meat")  # 以good开头，meat作为结尾
print(ret)  # ['good/food/meat']

import re

# （4）字符集 []  匹配[]中任意一个符号,
ret = re.findall("yu[abc]n", "yuan yubn yucn")  # 匹配[]里面abc中的任意一个
print(ret)  # 打印结果: ['yuan', 'yubn', 'yucn']

# 字符集两个特殊符号: -：范围  ^: 取反
ret = re.findall("yu[0-5]n", "yuan yu8n yucn yu2n")  # 匹配[]里面0到9中的任意一个,超过范围会匹配不到
print(ret)  # 打印结果: ['yu2n']

ret = re.findall("[a-zA-Z]+", "yuan,22,alvin,45,rain")  # 匹配A-Z和a-z 匹配无穷次
print(ret)  # 打印结果:['yuan', 'alvin', 'rain']

ret = re.findall("[^0-9]+", "yuan,22,alvin,45,rain")  # 匹配0-9以外的任意字符
print(ret)  # 打印结果:['yuan,', ',alvin,', ',rain']

# (5) () :分组   |: 或者关系
# 结果会优先提取分组为结果,取消提取分组结果,使用?:
ret = re.findall("https?://www\.[a-zA-Z0-9]+\.(?:com|cn)",
                 "http://www.baidu.com,https://www.jd.com,http://www.python.cn")
print(ret)  # 结果: ['http://www.baidu.com', 'https://www.jd.com', 'http://www.python.cn']

# (6) 转义符 \
# 1. 赋予普通符号以特殊功能 2. 取消特殊符号特殊功能
# \d
# 匹配任何十进制数；它相当于类[0-9]。
# \D
# 匹配任何非数字字符；它相当于类[^0-9]。
# \s
# 匹配任何空白字符；它相当于类[\t\n\r\f\v]。
# \S
# 匹配任何非空白字符；它相当于类[^\t\n\r\f\v]。
# \w
# 匹配任何字母数字字符；它相当于类[a-zA-Z0-9_]。
# \W
# 匹配任何非字母数字字符；它相当于类[^a-zA-Z0-9_]
# \b
# 匹配一个特殊字符边界，比如空格 ， & ，＃等
ret = re.findall("\d+", "12312wsdqaw13213")
print(ret)  # 打印结果: ['12312', '13213']

# 经典组合: .*?  .+?

















