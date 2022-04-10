# 同步主进程和子进程

import time, os
from multiprocessing import Process


# (1) join 基本使用
# def func():
#     print("发送第一封邮件: 领导在不")
#
#
# if __name__ == "__main__":
#     p = Process(target=func)
#     p.start()
#     # time.sleep(1)
#     p.join()   # join： 必须等待当前子进程结束之后，再执行下面的代码，用来同步子父进程
#     print("发送第二封邮件: 工资一个月涨到6W")

# (2) 多个进程中的join
# def func(i):
#     time.sleep(1)
#     print("发送第一封邮件{}: 领导在不".format(i))
#
#
# if __name__ == "__main__":
#     lst = []
#     for i in range(1, 11):
#         p = Process(target=func, args=(i,))
#         p.start()
#         # join写在里面会导致程序变成同步
#         lst.append(p)
#
#     # 把所有进程对象都放在列表中统一使用.join进行管理
#     for i in lst:
#         i.join()
#
#     print("发送第二封邮件: 工资一个月涨到6W")

# 使用自定义进程类, 来创建进程

## 基本语法
# class MyProcess(Process):
#     def run(self):
#         print("1子进程id:{},2父进程id:{}".format(os.getpid(), os.getppid()))
#
# if __name__ == "__main__":
#     p = MyProcess()
#     p.start()


## 带有参数的自定义进程类
class MyProcess(Process):

    def __init__(self, name):
        # 手动调用一下父类的构造方法, 完成系统成员的初始化
        super().__init__()
        self.name = name

    def run(self):
        print("1子进程id:{},2父进程id:{}".format(os.getpid(), os.getppid()))
        print(self.name)


if __name__ == "__main__":
    p = MyProcess("我是参数")
    p.start()
