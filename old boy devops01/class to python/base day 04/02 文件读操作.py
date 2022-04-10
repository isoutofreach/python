"""s = "袁浩"

ret = s.encode("utf8")  # 编码: 将字符串转为字节数据.默认用utf8
print(ret)

s1 = b"hello world"    # 添加一个b，代表这个是字节类型
print(s1, type(s1))

ret2 = ret.decode("utf8")
print(ret2)"""

# 打开文件: open(文件路径,mode="r",include)
# mode默认不写则是读模式  encoding 使用的编码格式，不写默认用的GBK
f = open("自嘲诗.txt", mode="r")
f1 = open("自嘲诗.txt", mode="rb")  # rb为读字节

# 读所有数据: read()
data = f.read()
data1 = f1.read()
print(data)
print(data1.decode("GBK"))

# 读几个数据
f = open("自嘲诗.txt", mode="r")
data = f.read(2)  # 读取多少字符就写多少，这里是读取2个字符
print(data, "\n")

# 循环读字符，因为第一种读文件，如果文件太大，会占用内存，推荐使用这种
# 跟着光标的位置来决定输出的内容
f = open("自嘲诗.txt", mode="r")
for line in f:
    print(line)




