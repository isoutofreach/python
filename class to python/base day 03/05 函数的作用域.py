x = 100

print(id(x))

def foo():
    global  x  # 使用全局的X
    print(id(x)) # 打印内存地址，查看是否和全局一样
    x = 1000
    print("局部变量", x)


foo()
print("全局变量", x)
