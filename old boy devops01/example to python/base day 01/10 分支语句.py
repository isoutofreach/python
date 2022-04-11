"""print("OK")
print("OK")
print("OK")"""

# 分支语句之if语句
'''
在python中用:+缩进表示语句体
if 表达式:
    语句1
'''
"""if 2 > 1:
    print(" OK ")"""
"""user = "yuan"
pwd = "123"
if user == "yuan" and pwd == "123":
    print("登录成功")"""

"""# 双分支语句
'''
if 表达式:
    语句1
else:
    语句2
'''
user = input("请输入用户名: ")
pwd = input("请输入密码: ")
if user == "yuan" and int(pwd) == 123:
    print("登录成功")
else:
    print("用户名或者密码错误")"""

# 多分支语句
"""
if 表达式:
    语句1
elif 表达式:
    语句2
else:
    语句3
    """

score = input("请输入成绩: ")
if score.isdigit() :
    score = int(score)
    if score > 100 or score < 0:
        print("非法输入")
    elif score >= 90:
        print("成绩优秀")
    elif score >= 80:
        print("成绩良好")
    elif score >= 60:
        print("成绩及格")
    else:
        print("成绩不及格")
else:
    print("请输入一个数字")

