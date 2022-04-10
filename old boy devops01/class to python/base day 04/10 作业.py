# 将学生管理系统改成可以存储在本地的形式
import os
import json
import sys


def choses_1():
    print("*" * 100)
    for stu_id in stu_dicry.keys():
        stu_name = stu_dicry.get(stu_id).get("name")
        stu_chinese = stu_dicry.get(stu_id).get("score").get("chinese")
        stu_english = stu_dicry.get(stu_id).get("score").get("english")
        stu_math = stu_dicry.get(stu_id).get("score").get("math")
        print("学号: %s, 姓名: %4s, 语文成绩: %-4s, 数学成绩: %-4s, 英文成绩: %-4s" % (
            stu_id, stu_name, stu_chinese, stu_math, stu_english))
    print("*" * 100)


def choses_2():
    stu_id = input("请输入学号>>>")
    if int(stu_id) not in stu_dicry.keys():
        stu_name = input("请输入姓名>>>")
        stu_chinese = input("请输入语文成绩>>>")
        stu_english = input("请输入英语成绩>>>")
        stu_math = input("请输入数学成绩>>>")
        stu_dicry.update({int(stu_id): {"name": stu_name,
                                        "score": {"chinese": int(stu_chinese), "english": int(stu_english),
                                                  "math": int(stu_math)}}})
    else:
        print("输入的学生学号重复")


def choses_3():
    stu_id = input("请输入修改学生学号>>>")
    if int(stu_id) in stu_dicry.keys():
        stu_chinese = input("请修改语文成绩>>>")
        stu_english = input("请修改英语成绩>>>")
        stu_math = input("请修改数学成绩>>>")
        stu_dicry.update(
            {int(stu_id): {"score": {"chinese": int(stu_chinese), "english": int(stu_english), "math": int(stu_math)}}})
    else:
        print("没有该学号，重新输入")


def choses_4():
    stu_id = input("请输入修改学生学号>>>")
    if int(stu_id) in stu_dicry.keys():
        stu_dicry.pop(int(stu_id))
    else:
        print("没有该学号，重新输入")


stu_dicry = {
    1001: {"name": "yuan", "score": {
        "chinese": 80,
        "english": 90,
        "math": 100
    }
           },
    1002: {"name": "yinz", "score": {
        "chinese": 100,
        "english": 100,
        "math": 100
    }
           }
}

a = os.path.abspath(__file__)
path = os.path.join(os.path.dirname(a), "学生管理.json")
f = open(path, "w")
f.write(json.dumps(stu_dicry))
f.close()

with open(path) as f:
    stu_dicry = json.loads(f.read())
while True:
    print("""
    1. 查看所有学生成绩
    2. 添加一个学生成绩
    3. 修改一个学生成绩
    4. 删除一个学生成绩
    5. 保存并退出程序
    """)
    choses = input("请输入您的选择: ")
    if choses.isdigit():
        choses = int(choses)
        if choses == 1:
            choses_1()
        elif choses == 2:
            choses_2()
        elif choses == 3:
            choses_3()
        elif choses == 4:
            choses_4()
        elif choses == 5:
            print("退出程序")
            f.close()
            with open(path) as f:
                stu_dicry = json.loads(f.read())
            sys.exit()
        else:
            print("输入错误，请重新输入")
    else:
        print("输入错误，请重新输入")
