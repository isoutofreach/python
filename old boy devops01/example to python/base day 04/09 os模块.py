import os

print(os.getcwd())  # 获取当前目录,python基本的存放目录
os.chdir("E:\代码保存\py\\base base day 16 04")  # 调整工作目录
print(os.listdir())  # 打印当前工作目录所有文件
# os.pardir 显示父目录
os.makedirs("wk01/xx", exist_ok=True)  # 当前工作目录下,创建多层文件夹
# exist_ok=True 如果文件夹存在不执行也不报错
os.removedirs("wk01/xx")  # 当前工作目录下,删除多层文件夹
os.mkdir("xx")  # 当前工作目录下,创建一层文件夹
os.rmdir("xx")  # 当前工作目录下, 删除一层文件夹
# os.rename("自嘲诗.txt", "自嘲诗3.txt")  # 重命名文件夹，前面是oldname后面是newname
print(os.stat('data.txt').st_size)  # 获取一个文件的属性,用.st_size 等可以获取对应信息
print(os.sep)  # 输出操作系统的路径分隔符,linux为/ windows为\ ,跨平台使用
os.system("ipconfig")  # 执行系统命令
print(os.path.abspath((__file__)))  # 显示文件的绝对路径

a = os.path.abspath((__file__))
ret = os.path.split(a)  # 将路径分割成目录和文件名
print(ret)
print(os.path.basename(a))  # 取path中的文件名
print(os.path.dirname(a))  # 取path中的目录名
print(os.path.exists(a))  # 判断路径是否存在，返回ture和false
print(os.path.isabs(a))  # 判断是否是绝对路径，返回ture和false
print(os.path.isfile(a))  # 判断是否为文件，返回ture和false
print(os.path.isdir(a))  # 判断是否为目录，返回ture和false

a = os.path.abspath(__file__)
path = os.path.join(os.path.dirname(a), "data.txt")  # 将多个路径拼接到一起
with open(path) as f:  # 将对文件的操作都放到文件句柄之中
    print(f.read())

os.path.getatime(a)  # 获取文件或者目录最后访问时间
os.path.getmtime(a)  # 获取文件或目录最后修改时间
os.path.getsize(path)  # 获取文件大小
