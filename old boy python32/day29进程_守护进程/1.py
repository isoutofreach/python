# 进程
import os, time

'''
# 获取进程号
res = os.getpid()
print(res)

# 获取当前进程的父进程
res = os.getppid()
print(res)
'''

# 引入进程一个类
from multiprocessing import Process

'''
def func():
    print("1子进程id:{},2父进程id:{}".format(os.getpid(), os.getppid()))


if __name__ == "__main__":
    # 创建子进程, 返回进程对象
    p = Process(target=func)
    # 调用子进程
    p.start()
    print("3子进程id:{},4父进程id:{}".format(os.getpid(), os.getppid()))
    '''


# (2) 创建带有参数的进程

# def func(n):
#     time.sleep(1)
#     for i in range(1, n + 1):  # 0 ~ n-1
#         print(i)
#         print("1.子进程id:{},2.父进程id:{}".format(os.getpid(), os.getppid()))
#
#
# if __name__ == "__main__":
#     n = 6
#     # target=指定任务  args = 参数元组
#     p = Process(target=func, args=(n,))
#     p.start()
#
#     for i in range(1, n + 1):
#         print("*" * i)

# (3) 进程之间的数据彼此隔离
# total = 100
#
#
# def func():
#     global total
#     total += 1
#     print(total)
#
#
# if __name__ == "__main__":
#     p = Process(target=func)
#     p.start()
#     time.sleep(1)
#     print(total)

# (4) 进程之间的异步性
def func(n):
    print("1子进程id:{},2父进程id:{}".format(os.getpid(), os.getppid()), n)


if __name__ == "__main__":
    for i in range(1, 11):
        if i == 2:
            time.sleep(1)
        p = Process(target=func, args=(i,))
        p.start()

    print("主进程执行结束", os.getpid())