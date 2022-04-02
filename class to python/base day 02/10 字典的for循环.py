stu = {'name': 'yuan', 'age': 32, 'gander': 'male'}
for i in stu:
    print(i, stu.get(i))  # 只会遍历字典的键值

a, *b = [1, 2, 3]
print(a, b) # 将1赋值给a，将剩下的所有值赋值给b

for k,v in stu.items():  # [["name","yuan"],["age","32"],["gamder","male"]]
    print(k,v)
