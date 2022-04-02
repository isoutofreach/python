# 案例一
stu = {"name": "yuan", "score": [100, 90, 80]}
#  获取字典中列表的值
print(stu.get("score")[2])

# 案例二
stu = {"name": "yuan", "score": {"chinese": 100, "math": 90, "english": 80}}
# 获取字典中字典的值
print(stu.get("score").get("english"))

# 案例三
data = [
    {"name": "rain", "age": 22},
    {"name": "eric", "age": 32},
    {"name": "alvin", "age": 24},
]
for stu_dict in data:
    name = stu_dict.get("name")
    age = stu_dict.get("age")
    print("姓名 %s, 年龄 %d" % (name, age))

# 案例四
data2 = {
    1001:{"name": "rain", "age": 22},
    1002:{"name": "eric", "age": 32},
    1003:{"name": "alvin", "age": 24},
}
for k, v in data2.items():
    name = v.get("name")
    age = v.get("age")
    print("学号: %d, 姓名: %s,年龄: %d"%(k, name, age))