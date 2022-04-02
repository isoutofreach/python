# 这是单行注释
'''

这是多行注释
用三个单引号或者三个双引号
'''

# 作业1： 计算 1 - 2 + 3 - 4 + ... + 99 中除了88以外所有数的总和？
# 作业2：
'''
程序随机内置一个位于一定范围内的数字作为猜测的结果，由用户猜测此数字。用户每猜测一次，由系统提示猜测结果：太大了、太小了或者猜对了，直到用户猜对结果或者猜测次数用完导致失败。
设定一个理想数字比如：66，
让用户三次机会猜数字，如果比66大，则显示猜测的结果大了；
如果比66小，则显示猜测的结果小了;
只有等于66，显示猜测结果正确，退出循环。
最多三次都没有猜测正确，退出循环，并显示‘都没猜对,继续努力’。
'''

"""num = 0
num1 = 0
while num < 100:
    num += 1
    if num % 2 == 0:
        num1 -= num
    elif num == 88:
        continue
    else:
        num1 += num
print(num1)"""


change = 0
while change < 3:
    num = input("请输入你想猜测的数字: ")
    if num.isdigit():
        num = int(num)
        if num > 66:
            print("太大了")
        elif num < 66:
            print("太小了")
        else:
            print("猜对了")
            break
    else:
        print("输入错误浪费一次机会，请重新输入")
        change += 1
        continue
    change += 1
    if change == 3:
        print("三次机会结束")

