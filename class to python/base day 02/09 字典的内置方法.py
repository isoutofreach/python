# 字典的内置方法: 对字典对象的数据管理
stu = {"name": "yuan", "age": "24"}

# 一、查
stu.get("name", None)  # 如果查询不到不报错，返回NONE
print(stu.get("gander", "male"))
print(stu.keys())  # 返回所有键值
print(stu.values())  # 返回所有值
print(stu.items())  # 打印键值，用元祖的方式打印

# 二、添加或修改： update
stu.update({"age": 32})  # 如果有键值对，就修改
print(stu)
stu.update({"gander": "male"})  # 如果没有键值对，就添加
print(stu)
stu.setdefault("xx", "xxx") # 取值，如果取不到,就添加这个值
print(stu)

# 三、删除键值对
print(stu.pop("age"))  # 返回删除键值对应的值
print(stu)
stu.popitem()  # 删除最后一个键值对
print(stu)
stu.clear()  # 清空字典
print(stu)
