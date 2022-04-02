class Animal(object):
    def eat(self):
        print("吃")

    def sleep(self):
        print("睡着了....")


class Fly(object):

    def fly(self):
        print("飞")


class Bat(Animal, Fly):  # 设置为2个父类
    pass
    def __init__(self,name,age):
        self.name = name
        self.age = age

class LittleBird(Animal, Fly):
    pass


b = Bat("xxx",23)
b.fly()  # 从左到右的方式进行查找，Animal父类中找不到fly就去Fly类中去查找方法
l = LittleBird()
l.fly()

print(type(b))  # 可以直接拿到对应类和类的名字
print(isinstance(b, Bat))  # 判断b是否是Bat的实例对象，返回true和false
print(isinstance(b, Animal))  # 判断实例化的类的父类是否是Animal，返回true和false

print(dir(Bat), dir(b))  # 可以查看实例化对象或者类的方法
print(b.__dir__())   # 等同于dir，顺序不同
print(b.__dict__)  # 相比于上面不同的是__dict__会打印实例属性
