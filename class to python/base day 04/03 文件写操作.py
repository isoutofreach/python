# 写字符
# 在文件写的时候，encoding就是写入的时候编码方式
# W 为覆盖模式，先将之前的清空，在写进去
f = open("自嘲诗1.txt", "w", encoding="utf8")
f.write("本是后山人")  # write写字符
f.close()  # 打开之后需要关闭

# 写入多行字符
f = open("自嘲诗1.txt", "w", encoding="utf8")
f.writelines(["xxx\n", "---\n", "xxxx\n"])  # 将字符串列表插入到文件中
f.flush()  # 之前是保存在内存之中,flush会写进硬盘里
f.close()  # 在使用close的方法会自动加载一下flush

# 写入追加模式
f = open("自嘲诗1.txt", "a", encoding="utf8")
f.writelines(["qqqq\n", "www\n", "eee\n"])  # 将字符串列表插入到文件中



