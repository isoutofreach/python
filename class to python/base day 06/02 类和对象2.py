# # 声明一个类
# # 类是一种比函数更高级的代码组织形式
# class Student(object):
#     # 类属性
#     class_name = "s32"
#     teachar = "yuan"
#     num = 30
#
#     # 方法
#     def __init__(self, name, age, sex):
#         # 初始化方法 作用: 实例化的时候最先触发
#         # self: 实例对象的空间地址
#         self.name = name
#         self.age = age
#         self.sex = sex
#         print(name, age, sex)
#
#     def listen(self):
#         print("听课")
#
#     def homework(self):
#         print("写作业")
#
#
# # 方式一: 实例化和属性赋值
# # s2 = Student()
# # s2.name = "潘磊"
# # s2.age = 39
# # s2.gander = "男"
#
# # 方式二:
# s1 = Student("潘磊", 39, "男")  # 将数值传给初始化方法
# s2 = Student("zhubiao", 21, "男")

# 声明一个类
# 类是一种比函数更高级的代码组织形式
class Student(object):
    # 类属性
    class_name = "s32"
    teachar = "yuan"
    num = 30

    # 方法
    def __init__(self, name, age, sex):
        # 初始化方法 作用: 实例化的时候最先触发
        # self: 实例对象的空间地址
        self.name = name
        self.age = age
        self.sex = sex
        print(name, age, sex)

    def listen(self,sourse="python"):   # 实例方法
        print("%s听%s课"%(self.name,sourse))

    def homework(self):
        print("%s写作业"%self.name)

# 实例方法
# 当调用实例方法的时候，会将调用的对象作为一个实参传回给形参
s1 = Student("潘磊", 39, "男")
s2 = Student("zhubiao", 21, "男")
s1.listen()
s1.homework()
