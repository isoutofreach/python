stu = {"name": "yuan", "age": "22"}

# 通过键查询值  字典对象[键]
print(stu["name"])
print(stu["age"])

# 添加或修改是一个操作
stu["gender"] = "male"  # 当键不存在的时候，就是添加
print(stu)
stu["age"] = "25"   # 当键存在的时候，就是修改
print(stu)

# 删除键值对  del
del stu["name"]
print(stu)