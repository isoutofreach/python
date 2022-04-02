class Animal(object):
    def eat(self):
        print("吃")

    def sleep(self):
        print("睡着了....")

class Dog(Animal):      # 定义一个狗类，会叫，会吃，会睡觉, 继承Animal类会吃会睡觉
    def sleep(self):
        # 引用父类的方法
        # super关键词：当前父类的超类
        super().sleep()       # 对父类进行一个实例化
        print("仰天大睡")

    def bark(self):
        print("狂吠")


class Cat(Animal):    # 定义一个猫类，会上树，会吃，会睡, 继承Animal类会吃会睡觉

    def climetree(self):
        print("爬树")

d1 = Dog()
d1.eat()  # 如果调用的实例中没有，就会向上找，同时找到父类
d1.sleep()  # 首先调用父类的方法sleep，然后再调用自己的sleep方法

