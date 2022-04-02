# 内置方法:  数据对象.方法()
s = "hello yuan"
print(s.upper())    # 全部改为大写

print(s.lower())   # 全部改为小写

print(s.startswith("hello"))  # 是不是以hello开头，返回布尔值

print(s.endswith("uan"))       # 是不是以uan结尾，返回布尔值

print(s.isdigit())   # 判断是否是数字字符串，返回布尔值

print("100".isdigit())  # 和上面对比，是纯数字字符串返回true

s2 = "      yuan   "
print(s2.strip())  # 去掉2边空格

s3 = "北京 上海 深圳 广州"
print(s3.split(" "))    # 将字符串切割，默认为空格，返回列表类型。可以将字符转换成列表

s4 = s3.split()
print("-".join(s4))     # 将字符以什么为分隔符，可以将列表转换成字符串







