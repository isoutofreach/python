import sys

print(sys.platform)  # 打印所在平台环境

# sys.path : 导入包的路径列表

print("ys.argv", sys.argv)  # 在执行的时候就导入参数
user_index = sys.argv.index("-u") + 1
pwd_index = sys.argv.index("-p") + 1
user = sys.argv[user_index]
pwd = sys.argv[pwd_index]
if user == "yuan" and pwd == "123":
    print("OK")


sys.exit()  # 强制程序退出
