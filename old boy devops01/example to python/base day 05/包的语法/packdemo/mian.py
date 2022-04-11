# 导入包的方式一:
# import 包名.模块名
import db.cal

print(db.cal.add(1, 4))

# 导入包方式二:
# from 包名 import 模块名
from db import cal

print(cal.mul(1, 10))

# 导入包方式三:
# from 包名.模块名 import 成员变量
from db.cal import mul, add

print(mul(1, 10))
print(add(10, 20))
