class Person(object):
    instance = None

    def __new__(cls, *args, **kwargs):  # __new__ 开辟命名空间 cls 代表着 Person 这个类对象
        if not cls.instance:   # cls.instance 第一次为None, None的零值为false,
            cls.instance = super().__new__(cls)  # cls.instance为__new__开辟命名空间的地址
        return cls.instance  # 如果没有返回值，则返回空给init, init不会执行
        # 用来创建单例, 无论实例化多少次, 都指向一个内存空间地址, 比如配置文件, 在一个项目中都指向一个内存空间读配置信息

    def __init__(self, name, age):
        print("__init__方法执行")
        self.name = name
        self.age = age




yuan = Person("yuan", 23)
