# 列表内置方法：  列表对象.方法()
# 列表的内置方法是用来管理列表中的数据：增删改查

"""# 一、 增：append insert extend
l = [10, 20, 30, 40]

ret = l.append(50)  # 添加一个到最后
print(l)

l.insert(0, 100)  # 插入到指定位置， 列表.insert(指定, 添加内容)
# 效率低
print(l)

l2 = [1, 2, 3]
l3 = [4, 5, 6]
l2.extend(l3)  # 将一个列表中的内容添加到另外一个列表中
print(l2)"""

"""# 二、 删： pop  remove clear

names = ["张三", "李四", "王五"]
print(names.pop(0)) # 按照索引删，返回删除的元素值
print(names)

# 元素值删除
names.remove("李四")  # 按照指定的元素值删除，返回NONE
print(names)

# 清空列表
names.clear()   # 清空列表
print(names)

#删除变量
del names
print(names)"""

"""# 三、改： 没有内置方法，只能通过索引完成
l = [1, 2, 3]
l[0] = 100
print(l)"""

# 四 查   index count sort reverse
names = ["张三", "李四", "王五", "张三"]
print(names.index("李四"))  # 查找值所在的索引，默认是从左到右第一次

print(names.count("张三"))  # 查找值出现过几次

age = [20, 22, 18, 45, 32]
age.sort()  # 从小到大，进行排序
print(age)
age.sort(reverse=True)   # 从大到小，进行排序
print(age)
age1 = ["100", "10", "32"]
age1.sort()      #  如果是字符串的话，就是通过ASCII值进行比较
print(age1)

age = [20, 22, 18, 45, 32]
age.reverse()        # 将列表翻转
print(age)