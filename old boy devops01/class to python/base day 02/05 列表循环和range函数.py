# for循环: 便利循环，循环次数取决于遍历对象的元素个数
'''
for 循环的格式:

for 变量 in 可迭代的对象(字符串|列表|字典|元祖|集合):
    循环体

'''
"""for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

# range(start=0,end,step=1) start：开始参数,默认为0  end：结束参数  step:步长
for i in range(5):
    print(i)"""

s = "20,15,34,188,26,yinzijian"
num1 = s.split(",")
num2 = []
for i in num1:
    if i.isdigit():
        num2.append(int(i))
    else:
        print("该字符串 %s 不是数字，忽略"%(i))
num2.sort()
print(num2)

