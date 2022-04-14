class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # __age即私有属性
        # python在设置私有属性的时候，真正设置的是 _类名__实例对象 = 传值

    def foo(self):
        print(self.name, self.__age)  # 调用内部私有属性
        # 自己内部调用的时候，使用的是self._类名__实例对象

    def get_age(self):
        return self.__age  # 对外封装接口，让外部调用

    def set_age(self, new_age):
        if new_age < 100:
            self.__age = new_age    # 对外封装接口，可以对外设置
        raise Exception("年龄不能超过100岁")

p1 = Person("yuan", 22)
print(p1.name)  # 共有属性使用：设置完之后，在当前类的外部可以使用类的属性和方法
p1.name = "rain"  # 共有属性：外部可以使用，可以修改
# p1.age  在外部会调用不到这个参数
p1.foo()

print(dir(p1))  # 使用dir，可以查询到隐藏属性  '_Person__age'
# 调用私有化
print(p1._Person__age)  # 强制调用私有化参数

print(p1.get_age())  # 外部调用接口

p1.set_age(20)  # 外部设置内部参数
p1.foo()
p1.set_age(101)
