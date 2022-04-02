# 声明函数
'''
def 函数名(传参,...):
    函数体
    return # 函数返回值
    # 如果没有写，默认None

ret = 函数名(实参)   # 用ret来接收函数的返回值
'''
def foo():
    print("ok")
# 默认返回Nnone
ret = foo()
print("ret", ret) #None

# 将多个值变成元祖返回
def bar():

    return True, "yuan" # 会将多个值,变成元祖返回
state, username = bar()



