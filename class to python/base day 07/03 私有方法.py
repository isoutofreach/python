class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        self._score = 100

    def get_name(self):
        print(self.__name)


    def __foo(self):
        print("foo")


class Teacher(Person):
    def bar(self):
        self.__foo()


t1 = Teacher("yuan", 23)

#t1.bar()   调用不成功，子类调用不了父类的方法 __类方法  只能在本类中调用

