"""# 一个字符串是由若干个字符按顺序构成的
s = "hello world"
#  序列类型操作一：
# 支持正负索引，通过索引来获取值
# 语法格式： 数据对象[索引]
print(s[4])  # o
print(s[6])  # w
print(s[-7])  # o
print(s[-1])  # d"""

"""# 序列类型操作二：切片操作 获取多个值
# 语法格式： 数据对象[开始索引：结束索引：步长]  默认原则: 从左到右
# 步长为1，从左到右一个个切，步长为-1，从右向走切。默认为1。
# 左闭右开，顾头不顾尾
s = "hello world"
print(s[0:5])  #
print(s[6:])  # 取到最后1位
print(s[:5])  # 从最开始取到第4个
print(s[:])  # 完整切片
print(s[-6:-1]) # 符合从左到右
print(s[-3:-5])  # 从右到左，结果为空
# 步长为-1
print(s[-1:-6:-1])  # 从最后一个取到倒数第5个
print(s[5::-1])  # 从第4个反向取到第1个
# 步长为2
# 从左到右，切一个跳一个，如果为3则是从左到右切1个跳2个
# 步长为-2则是从右到左，切一个跳一个
print(s[::2]) # 切一个跳一个
"""


"""# 序列类型操作三：in 判断  返回布尔值
print("yuan" in "hello yuan")
print("rain" in "hello yuan")
print("yua" in "hello yuan")
print("yuan hello" in "hello yuan")"""

# 序列类型操作四: 拼接 使用 +
s1 = "hello "
s2 = " yuan"
print(s1+s2)
print("**********")
print("*"*10)




