# 元祖称之为可读列表,只能查询、不能改
l = [1, 2, 3]
t = (1, 2, 3, 2)
print(t, type(t))
print(t[1])
print(t[1:])
print(1 in t)

print(t.count(2))     # 重复出现次数
print(t.index(1))     # 查询出现在第几位