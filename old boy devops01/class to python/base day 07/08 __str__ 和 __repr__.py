class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # 控制打印对象返回值，必须返回的是字符串类型
        return f"姓名: {self.name}, 年龄: {self.age}"

    def __repr__(self):
        # 控制打印对象返回值, 优先去找str, 如果str没有就去找repr, 如果没有就返回默认值
        # repr和str区别是, repr返回的比str要详细, 可以返回很多其他信息, 比如调用模块, 数据类型等
        # 通俗点 str 是给人看的  repr 是给程序员看的
        return self.name


p1 = Person("yuan", 22)
p2 = Person("rain", 32)
print(p1)
print(p2)
