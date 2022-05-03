"""
函数语法格式:
def 函数名():
    代码块
"""
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


print_ling(4)
