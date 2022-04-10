# 案例1
stu01 = {"name": "rain"}
stus = {1001: stu01}
print(stus)
stu01["name"] = "alvin"
print(stus)
print(id(stus[1001]))
stus[1001] = {"name": "eric"}
print(stu01)
print(id(stus[1001]))
 