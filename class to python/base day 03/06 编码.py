'''
B = 8b  # 一个B等于8个比特位
KB = 1024B
MB = 1024KB
GB = 1024MB

一个汉字在ASCII编码用2个字节，在Unicode编码用4个字节，在utf8编码用3个字节
如果一个文件是纯英文的，用任何编码方式都可以，因为所有编码方式都是兼容ASCII表
如果是其他文字可能会变成，因为编码的方式不一样
'''

# 编码
s = "袁浩"
# 字符串的编码方法: 字符串转换成二进制数字的过程叫编码
ret1 = s.encode("utf8")
ret2 = s.encode("GBK")
print(ret1,type(ret1))
print(ret2)

# 解码
s1 = ret1.decode("utf8")
print(s1)
s2 = ret2.decode("GBK")
print(s2)

