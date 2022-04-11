# import time
#
# time.sleep(10)  # 阻塞程序10秒钟
#
# '''
# 时间戳
# "1970-1-1 0:0:0" 为标志，是0
# "1970-1-1 0:0:1" 是1
# time.time() 是表示从1970-1-1 0:0:0 到现在过了多长时间
# '''
# print(time.time())    # 打印当前时间戳
# # 用来打印时间差
# c1 = time.time()
# print(c1)
# print("hello world")
# time.sleep(3)
# c2 = time.time()
# print(c2)
# print(c2 - c1)


# import datetime  # 导入包
# # 构建一个日期对象
# # data类
# dt = datetime.date(2012, 12, 12)
# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt)  # 默认格式
# ret = dt.strftime("%Y/%m/%d")
# print(ret)
# # 构建当前日期对象
# td = datetime.date.today()
# print(td)


# import datetime
# # datetime类
# # 构建日期对象
# dt = datetime.datetime(2012, 11, 10, 9, 8, 7)
# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.hour)
# print(dt)
# print(dt.strftime("%Y/%m/%d %H-%M-%S"))
# print(dt.strftime("%Y/%m/%d %X"))

# import datetime
#
# # datedelta 打印时间差
# dt = datetime.datetime(2012, 11, 10, 9, 8, 7)
# print(datetime.datetime.now())  # 获取此刻的时间，代码运行到此刻
# # 关于日期比较
# print(datetime.datetime.now() > dt)
# # 关于时间差
# td = datetime.timedelta(days=3)
# print(datetime.datetime.now() - td)
# print(datetime.datetime.now() + td)

import locale
import datetime

locale.setlocale(locale.LC_CTYPE, 'chinese')
# 通过当前时间按照格式"1998年12月10日 星期五 13时45分"显示当前时刻三天后时间
now = datetime.datetime.today()
data = datetime.timedelta(days=3)
threedata = now + data
print(threedata.strftime(f'%Y{"年"}%m{"月"}%d{"日"} %H{"时"}%M{"分"}'))
