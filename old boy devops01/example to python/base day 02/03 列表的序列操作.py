l = [10, 20, 30, 40, 50]
"""# 列表是一个序列类型
# 一 支持正负索引 数据对象[索引]
print(l[1])
print(l[-3])"""

"""# 支持切片: 数据对象[开始索引:结束索引:步长] 顾头不顾尾
l = [10, 20, 30, 40, 50]
print(l[1:4])
print(l[-4:-1])
print(l[1:])
print(l[:3])
print(l[-2:-5:-1])"""

"""# in操作 列表的最小单位为元素
names = ["rain", "yuan", "alvin"]
print("rai" in names)
print("rai" in names[0])
print(1 in ["1", 2, 3])"""

# 拼接
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)


