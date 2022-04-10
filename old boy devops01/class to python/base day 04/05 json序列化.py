stu_dicry = {
    1001: {"name": "yuan", "score": {"chinese": 80, "english": 90, "math": 100}
           },
    1002: {"name": "yinz", "score": {"chinese": 100, "english": 100, "math": 100}
           }
}

# 存文本的方式
# f = open("data.txt", "w")
# data = str(stu_dicry)
# f.write(data)
# f.close()

# ##### json 序列化 ######
# # 数据交换的基本格式: 1.语言和语言的交换
import json  # 导入json包
#
# # 序列化
# data1 = (True, None, 123, 'yaun')
# json1 = json.dumps(data1)
# print(json1, type(json1))  # json 序列化结构
#
data2 = {"name": 'yuan', "age": "22", "isMarried": False}
ret2 = json.dumps(data2)
print(repr(ret2))
#
# 存储文件
f = open("data.json", "w")
f.write(ret2)
f.close()

# # 反序列化
# f = open("data.json")
# data = f.read()
# print(data, type(data))
# data_dict = json.loads('{"name": "yuan", "age": "22", "isMarried": false}')
# print(data_dict.get("name"))
#
# # 补充
# data_str = '{"name":"yuan","is_married":false,"sorc":[100,43,67]}'
# js_data = json.loads(data_str)
# print(js_data,type(js_data))
#
# res = {"state": True, "err": None}
# res_json = json.dumps(res)
# print(res_json)