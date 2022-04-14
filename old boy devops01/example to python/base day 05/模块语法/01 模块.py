'''
模块分类：
1. 解释器内建模块   2. 标准库模块    3. 第三方模块   4. 自定义模块
'''
# 导入模块方法一
import cal

print(cal.add(1, 5))
print(cal.mul(2, 5))

# 导入模块方法二
# 将模块中的某个变量导入
from cal import add, mul
# 当模块中有同名变量，以免发生冲突，可以给变量起别名
from cal import a as cal_a

a = 1
print(a, cal_a)
print(add(1, 2))
print(mul(2, 4))

# 导入模块方法三
# 将模块中所有变量导入,但是效率较低,慎用
from cal import *
print(a)

'''
导入模块的路径依赖: 
1. 内建模块
2. sys.path:[当前执行模块的目录,python环境]

'''


