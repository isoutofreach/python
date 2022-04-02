x = 10
b = True

"""# 创建一个字符串
s = 'hello world'  # 字符串是用双引号和单引号标识的
print(s)
"""

"""s2 = "i am yuan \ni am a teacher"
print(s2)"""

"""s2 = 'i\'m yuan!'
print(s2)"""

"""# 长字符串
s3 = '''
   杜甫 
 白日依山尽 
 黄河入海流'''
print(s3)"""

# 格式化输出
name = "rain"
age = 23
gender = "男"
# 所谓模板或者格式化字符串：将动态变化的值嵌入到字符串的某个位置中
# 占位符： %s：给字符串占位  %d：给十进制数字占位 %f: 给浮点型占位
s6 = "姓名: %s , 年龄: %d ， 性别： %s" % (name, age, gender)
print(s6)
