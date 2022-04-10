# d = {"name": "yuan"}
# # print(d["names"])  #没有对应键,会报错
#
# try:
#     print("OK1")
#     f = open("xxx")  # 没有xxx的文件，会报错
#     print("OK2")
#     # 当程序报错的时候, 会立即跳到except, 不会执行下面的代码, 所以只会打印OK1
# except FileNotFoundError:  # 只会捕获相应的报错
#     print("文件不存在")
#
# try:
#     print(d["names"])
# except Exception as e:  # Exception 为万能报错, 什么报错都可以接收, 后面的as是将报错的信息赋值到e, 后面可以打印信息
#     print("报错了", e)
#
# try:
#     f = open("xxx")
#     print(d["names"])  # 因为上面报错, 下面不执行了, 所以不会跳到KeyError异常处理
# except KeyError as e:
#     print("找不到键值")
# except FileNotFoundError as e:  # 可以设置多种报错异常处理
#     print("找不到文件")
#
# try:
#     f = open("xxx")
#     print(d["names"])
# except (KeyError, FileNotFoundError) as e:  # 多种报错异常处理
#     print("报错")
# finally:       # 无论报错还是不报错, 都会执行的语句, 使用例子: 关闭文件, 关闭数据库连接等
#     print("无论如何都会执行的语句")


# 自定义异常类型
class TooLongExceptin(Exception):   # 自定义错误类型, 一定要声明一个类, 一定要继承父类Exception
    "this is user's Exception for check the length of name "

    def __init__(self, len):
        self.len = len

    def __str__(self):
        return "输入姓名长度是" + str(self.len) + "，超过长度了"


try:
    name = input("enter your name:")
    if len(name) > 5:
        raise TooLongExceptin(len(name))  # 如果长度超过5, 就会报错TooLongExceptin
    else:
        print(name)
except TooLongExceptin as error:  # 通过之前自定义的报错TooLongExceptin来返回信息
    print("打印异常信息：", error)


