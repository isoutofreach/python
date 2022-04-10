# 类和对象的概念
# 声明一个类
'''
class  类名（object）:
    类属性
    实例方法


类名()



'''


class Person(object):
    # 类属性、类变量、类的成员变量
    legs_num = 2

    def __init__(self, name, age):
        # 实例属性、实例对象
        self.name = name
        self.age = age

    def dream(self):
        pass


p1 = Person("yuan", 22)
p2 = Person("yuan", 22)


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def Print(self):
        print(self.name, self.age, self.score)


s = Student("yuan", 23, 100)
s.Print()