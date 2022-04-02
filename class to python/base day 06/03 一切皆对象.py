# 一切皆对象
# 数据类型: 数字类型  布尔类型  字符串类型 列表 字典 集合 元祖
s = "hello yuan"  # 简易表达
s2 = str("hello yuan")  # 创建字符串的根本方式
print(s2, type(s2))

class Weapon(object):
    def __init__(self, name, color,attack):
        self.name = name
        self.color = color
        self.attack = attack

class Hero(object):
    def __init__(self, name, hp, weapon, level=2, exp=2000, money=10000):
        self.name = name  # 英雄的名字
        self.hp = hp  # 英雄生命值
        self.level = level  # 英雄的等级
        self.exp = exp  # 英雄的经验值
        self.money = money  # 英雄的金币
        self.weapon = weapon  # 英雄的武器

w1 = Weapon("弓箭", "黄色", 180)

yuan = Hero("yuan", 100, w1)
print(yuan.weapon)
print(yuan.weapon.color)