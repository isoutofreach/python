class Base:
    def foo(self):
        print("foo from Base")

    def test(self):
        self.foo()

class Son(Base):
    def foo(self):
        print("foo from Son")

s=Son()
s.test()


class Base:
    def __foo(self):
        print("foo from Base")

    def test(self):
        self.__foo()

class Son(Base):
    def __foo(self):
        print("foo from Son")

s=Son()
s.test()