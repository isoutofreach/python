class Utils(object):
    class_num = 30

    @staticmethod
    # 如果不加静态方法，将会把x 当成self赋值
    def add(x, y):
        return x + y

    # 类方法
    @classmethod
    def add_class_num(cls):  # 当前类对象
        print(id(cls), id(Utils))  # 声明cls参数和声明的类为一个内存空间
        cls.class_num += 1
        print(cls.class_num)


# 通过实例对象调用静态方法
u = Utils
print(u.add(1, 2))

# 类对象调用对象方法
print(Utils.add(6, 7))

Utils.add_class_num()
print(Utils.class_num)        # 打印class_num



