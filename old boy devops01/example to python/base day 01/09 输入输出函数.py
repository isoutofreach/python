"""name = "yuan"
age = 23
print(name,age)
# 打印内容默认为换行符结尾
print(111,end=";")  # 用;作为结尾
print(222)
# 打印内容默认用空格进行隔开
print(name,age,sep="--")  # 用--进行隔开"""

#  输出函数
# input 函数接收的一定是字符串
name = input("请输入一个姓名: ")   # 要用用户在终端输入一个值
age = input("请输入一个年龄: ")
print("姓名: %s , 年龄: %d"%(name,int(age)))