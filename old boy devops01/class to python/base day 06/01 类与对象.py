# 声明一个类
# 类是一种比函数更高级的代码组织形式
class Student(object):
    # 类属性
    class_name = "s32"
    teachar = "yuan"
    num = 30

    # 方法
    def listen(self):
        print("听课")

    def homework(self):
        print("写作业")


# 实例化对象: 类名()   实例化的对象各自开辟一个内存空间地址
s1 = Student()
print(id(s1))  # 打印结果: 3067115859416
s2 = Student()
print(id(s2))  # 打印结果: 3067115859472

# 对象通过句点符号调用属性和方法的过程
print(s1.class_name)  # 调用属性  # 打印结果: s32
print(s1.num)  # 调用属性     # 打印结果: 30
s1.listen()  # 调用方法    # 打印结果: 听课

# 设置实例属性  会将设置的属性存储到各自单独的空间
s1.name = "zhubiao"
s1.age = 31

# 实例对象.变量的查询顺序    首先查询自己内存空间的变量，如果没有就查询到类中的属性
print(s1.name)    # 打印结果: zhubiao
print(s1.class_name)   # 打印结果: s32
# 类属性的修改
Student.class_name = "s188"
print(s1.class_name, s2.class_name)    # 打印结果: s188 s188


































