# 1. 关于变量赋值：交换a和b两变量的值
a = 1
b = 2
a ,b = b, a

# 2.如何用多个变量接收列表或者元组的值
a, b = [1, 2]
a, *b = [1, 2, 3]

# 3. 输入一个字符串, 返回倒序排列的结果 如: abcdef, 返回 fedcba
a = "abcdef"
print(a[::-1])

# 4. 将"北京 上海 广州 深圳"转换为 “北京,上海,广州,深圳”
a = "北京 上海 广州 深圳"
print((",").join(a.split(" ")))

# 5.短路计算
print( 3 or 2)
print( 3 and 2)
user = None
def foo():
		return user or "root"
print(foo())

# 6. 0 or 1 and 5 的结果
print(not 1)
print(not 0)
print(0 or 1 and 5)
print(6 and not 1 and 5)

# 7. 零值概念
print("-1的零值是: ",bool(-1),  "1的零值是: ",bool(0))

# 8. is和==的区别
l1 = [1,2,3]
l2 = [1,2,3]
print(l1 == l2)
print(id(l1) == id(l2))

#9. 将两个列表[1, 5, 7, 9],[2, 2, 6, 8]合并为[1, 2, 2, 5, 6, 7, 8, 9]
l1 = [1, 5, 7, 9]
l2 = [2, 2, 6, 8]
l1.extend(l2)
l1.sort()
print(l1)

#10. a = [1,2,3,4,5,6]，a[::-3] 的结果是
print("6,3")

#11. 列表去重再排序
l = [1, 4, 5, 6, 6, 4, 2, 1]
l2 = list(set(l))
l2.sort()
print(l2)

#12. s = ‘ajldjlajfdljfddd’，去重并从小到大排序输出’adfjl'
s = 'ajldjlajfdljfddd'
s1 = list(set(s))
s1.sort()
print(("").join(s1))

#13. 列表和元组有什么不同？
# 1. 列表可以进行增删改查, 但是元组不能进行修改操作
# 2. 元组是不可变数据类型, 可以作为字典的键值, 列表是可变数据类型, 不可以作为字典键值

#14. python中哪些是可变类型 ,哪些是不可变类型
# 可变类型: 列表 字典
# 不可变: 字符串 元组 整型 浮点型 布尔类型

#15. 什么是深浅拷贝

#16 请合并下面两个字典 a = {“A”: 1, “B”: 2},b = {“C”: 3, “D”: 4}
a = {"A": 1, "B": 2}
b = {"C": 3, "D": 4}
a.update(b)
print(a)

#17 python的三元运算表达
a = 11
b = 20
ret = a if a > b else b
print(ret)
print("a是偶数" if a % 2 == 0 else "a是奇数")

#18. 统计一段字符串中每个字符出现的次数，比如abcaabccab
a = "abcaabccab"
print(a.count("a"))

dic = {}
for i in a:
		dic[i] = dic.get(i,0)+1
print(dic)

s = "abcaabccab"
result = {x: s.count(x) for x in s}
print(result)

#19. 字典和列表的查找速度哪个更快?
#列表查询是遍历方式，时间复杂度是O(n), 字典查询是hash映射 时间复杂度是O(1);当数据量小的时候切片查询比map快，但是数据量大的时候字典的优势就体现出来了

#20. 如何实现[‘1’, ‘2’, ‘3’]变成[1, 2, 3]
l = ['1','2','3']
l2 = [ int(i) for i in l]
print(l,l2)

#21 获取1-100中所有偶数平方列表
print([ q*q for q in range(1,101) if q % 2 == 0])

#22 1,2,3,4,5 能组成多少个互不相同切无重复的元素
li = [1,2,3,4,5]
lq = [int(str(q)+str(w)+str(e)) for q in li for w in li for e in li if q != w and q != e and e != w]
print(len(lq))

# 23 如何交换字典{"A":1,"B":2}的键和值
dict_1 = {"A":1,"B":2}
dict_2 = {v:k for k,v in dict_1.items()}
print(dict_2)

# 24 将所有的key值变为大写
dict_1 = {"a":1, "b":2, "c":3, "d":4}
dict_2 = { k.upper():v for k,v in dict_1.items()}
print(dict_2)

# 25 pass语句的作用是什么
# 占位符,不执行任何操作

# 26 如何在一个函数内部修改全局变量
i = 100
def num(q):
		global i
		i += q
		return i
print(num(145),i)

# 27. 如何修改一个非局部非全局变量
def foo():
		x = 200
		def bar():
				nonlocal x
				x = x+1
		bar()
		print(x)

foo()

# 28. 