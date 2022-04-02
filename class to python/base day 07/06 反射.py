class Person(object):
    def __init__(self, name, age, gander):
        self.name = name
        self.age = age
        self.gander = gander


yuan = Person("yuan", 23, "男")


def check_attr():
    attr = input("yuan的属性 >>>")
    isExist = hasattr(yuan, attr)
    # 判断attr是否是yuan实例对象中的类属性，返回ture和false
    if isExist:
        print(getattr(yuan, attr))
        # 获取yuan对象类中attr的值，等同于 yuan.attr ,attr是引导用户输入的值，可以是name age gander
    else:
        print("yuan不存在属性", attr)
        choice = input("是否设置该属性?Y/N")
        if choice.upper() == "Y":
            value = input(f"请输入属性{attr}")
            print(value)
            setattr(yuan, attr, value)
            # 对yuan实例对象增加参数，attr作为变量名，value作为参数


while 1:
    check_attr()
