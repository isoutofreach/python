import random

print(random.random())  # 0-1随机浮点数
print(random.randint(1, 9))  # 取 0-9范围整形
print(random.randrange(1, 3))  # 取1-3的范围，但是顾头不顾尾，取不到3
print(random.choice(["a", "b", "c"]))  # 多个元素选一个
print(random.sample(["a", "b", "c"], 2))  # 多个元素选多个

l = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(l)  # 将有序的序列打乱成无序显示
print(l)

# 构建五位验证码
print(ord("a"))  # 将字符转换成ASCII
print(chr(97))  # 将ASCII转换成字符

def get_rendom_str():
    ret = []
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_lower = chr(random.randint(97, 122))
        # 因为小写的a-z ASCII 是97到122
        random_upper = random_lower.upper()
        # 因为大写的A-Z ASCII 是65到190
        random_char = random.choice([random_upper, random_num, random_lower])
        ret.append(random_char)
    return "".join(ret)

print(get_rendom_str())