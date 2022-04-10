"""l1 = [1, 2, 3, 4, 5]"""
# （1）在l1的元素3后面插入300
"""l1.insert(2, 300)
print(l1)"""
# （2）删除元素2
"""l1.remove(2)
print(l1)"""
# （3）将5更改为500
"""l1[4] = 500
print(l1)"""
# （4）将2，3，4切片出来
"""print(l1[1:4])"""
# （5）l1[-3:-5]的结果
"""空值"""
# （6）l1[-3:]的结果
"""3,4,5"""

# 2. 通过input引导用户输入一个姓名，判断该姓名是否存在于列表names中
"""names = ["yuan","eric","alvin","george"]
user_name = input("输入姓名: ")
print(user_name.strip() in user_name)"""

"""l = [1,2,3,[4,5]]"""
# （1）将4修改为400
"""l[3][0] = 400
print(l)"""
# （2）在l的[4，5]列表中追加一个6，即使l变为[1,2,3,[4,5,6]]
"""l[3].append(6)
print(l)
"""
# 4. 数一下字符串"天津 北京 上海 深圳 大连"中的城市个数
"""citys = "天津 北京 上海 深圳"
print(len(citys.split()))"""

# 5. 将字符串"56,45,6,7,2,88,12,100"转换为按顺序显示的"2 6 7 12 45 56 88 100"
num = "56,45,6,7,2,88,12,100"
num1 = []
num2 = []
num1 = [int(i) for i in num.split(",")]
num1.sort()
num2 = [str(i) for i in num1]
num = " ".join(num2)
print(num)


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

while True:
    print("""
    1. 查看所有学生成绩
    2. 添加一个学生成绩
    3. 修改一个学生成绩
    4. 删除一个学生成绩
    5. 退出程序
    """)
    choses = input("请输入您的选择: ")
    if choses.isdigit():
        choses = int(choses)
        if choses == 1:
            print("*" * 100)
            for stu_id in stu_dicry.keys():
                stu_name = stu_dicry.get(stu_id).get("name")
                stu_chinese = stu_dicry.get(stu_id).get("score").get("chinese")
                stu_english = stu_dicry.get(stu_id).get("score").get("english")
                stu_math = stu_dicry.get(stu_id).get("score").get("math")
                print("学号: %d, 姓名: %4s, 语文成绩: %-4d, 数学成绩: %-4d, 英文成绩: %-4d" % (stu_id, stu_name, stu_chinese, stu_math, stu_english))
            print("*" * 100)
        elif choses == 2:
            stu_id = input("请输入学号>>>")
            if int(stu_id) not in stu_dicry.keys():
                stu_name = input("请输入姓名>>>")
                stu_chinese = input("请输入语文成绩>>>")
                stu_english = input("请输入英语成绩>>>")
                stu_math = input("请输入数学成绩>>>")
                stu_dicry.update({int(stu_id): {"name": stu_name, "score": {"chinese": int(stu_chinese), "english": int(stu_english), "math": int(stu_math)}}})
            else:
                print("输入的学生学号重复")
        elif choses == 3:
            stu_id = input("请输入修改学生学号>>>")
            if int(stu_id) in stu_dicry.keys():
                stu_chinese = input("请修改语文成绩>>>")
                stu_english = input("请修改英语成绩>>>")
                stu_math = input("请修改数学成绩>>>")
                stu_dicry.update({int(stu_id): {"score": {"chinese": int(stu_chinese), "english": int(stu_english), "math": int(stu_math)}}})
            else:
                print("没有该学号，重新输入")
        elif choses == 4:
            stu_id = input("请输入修改学生学号>>>")
            if int(stu_id) in stu_dicry.keys():
                stu_dicry.pop(int(stu_id))
            else:
                print("没有该学号，重新输入")
        elif choses == 5:
            print("退出程序")
            break
        else:
            print("输入错误，请重新输入")
    else:
        print("输入错误，请重新输入")