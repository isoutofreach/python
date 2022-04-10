# 测试题：

class Base:
    def __init__(self):
        self.func()

    def func(self):
        print('in base')

class Son(Base):
    def func(self):
        print('in son')

s = Son()
