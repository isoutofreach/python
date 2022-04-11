class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def foo(self):
        print(self.__name, self.age)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


p1 = Person("yuan", 22)
print(p1.name)   # 使用了属性装饰器之后, 后面调用的时候，不用加(),使用起来更加简洁

p1.name = "xxx"    # 使用了属性装饰器之后，后面调用的时候，可以直接用赋值的方式

print(p1.name)
# 如果是查询就会走@property装饰器，如果是设置，就会走 xx.setter装饰器
# 只会对装饰器下的方法有用

