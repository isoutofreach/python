"""'''
def 函数名(形式参数):
    函数体
函数调用:
函数名（实际参数）
'''


def print_ling(rows):
    i = j = k = 1
    # 菱形的上半部分
    for i in range(rows):
        for j in range(rows - i):
            print(" ", end=" ")
            j += 1
        for k in range(2 * i - 1):
            print("*", end=" ")
            k += 1
        print("\n")
    # 菱形的下半部分
    for i in range(rows):
        for j in range(i):
            print(" ", end=" ")
            j += 1
        for k in range(2 * (rows - i) - 1):
            print("*", end=" ")
            k += 1
        print("\n")


print_ling(3)


# 计算1-100的和
def cal_add(n, m):
    ret = 0
    for i in range(n, m + 1):
        ret += i
    print(ret)


cal_add(1, 100)"""

"""# 二、默认参数
# 默认参数：如果没有传参，就使用默认参数，类似于给一个默认值
# 默认参数一定要放到位置参数的后面
def print_info(name,age,gender="男"):

    #   name = "yuan"
    #    age = 22
    #    gender = "男"
    print("姓名: %s  年龄:  %s  性别:   %s" % (name, age, gender))

print_info("rain",22)"""

"""# 三、关键字参数
# 直接用关键词赋值，不需要在意顺序
def print_info(name, age, height):
    #    name = "yuan"
    #    age = 22
    #    gender = "男"

    print("姓名: %s  年龄:  %s  性别:   %scm" % (name, age, height))

print_info(name="rain", height=180, age=20)
# 关键字参数一定要放到位置参数后面
print_info("yuan", height=180, age=20)"""

"""# 四、不定长参数

def add3(*args):
    print(args, type(args))
    ret = 0
    for i in args:
        ret += i
    print(ret)


# 返回的类型为元祖类型
add3(1, 2)
add3(1, 2, 3, 4)
add3(4, 5, 6, 7)


def add4(name, *a):
    print("%s在调用add函数" % (name))
    print("a: ", a)


add4("yuan", 2, 3, 4, 51, 1)"""


# *args: 用来传递位置参数， **kwargs: 用来接收关键字参数
def print_info(name, age, *args, **kwargs):
    print("姓名: %s, 年龄:  %s, 身高: %s" % (name, age, kwargs.get("height")))


# 将args 打包成元祖, 将kwargs打包成字典
print_info("yuan", 22, height=180)
