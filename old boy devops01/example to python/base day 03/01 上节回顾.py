# 构建一个列表: 1.[元素1,元素2]  2. list([元素1,元素2])
l1 = [1, 2, 3]
l2 = list([4, 5, 6])
print(type(l2))

# 特点: 1. 元素个数没有限制   2. 元素的数据类型没有限制
# 基本操作: 1. 属于序列类型(索引、切片、拼接、in操作)
#       索引: 列表[索引]      切片: 列表[开始索引:结束索引:步长]

# 切片
print(l1[1:])

# 拼接
print([1, 2, 3] + [2, 3, 4])

# in操作
print("yuan" in "hello yuan")
info = {"name":"yuan","age":22}
print(info.get("xx","none"))

print(len(info.keys()))
