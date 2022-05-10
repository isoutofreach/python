from django.test import TestCase

# Create your tests here.

import requests

data = requests.get("https://2019ncov.chinacdc.cn/JKZX/yq_20220401.json")
# print(data.json()['features'][0]['properties'])
data1 = data.json()["features"]
print()

for item in data1:
    # print(item.get("properties"))
    name = item.get("properties").get("name")
    a = item.get("properties").get("新增疑似")
    b = item.get("properties").get("累计确诊")
    c = item.get("properties").get("新增确诊")
    print(name, a, b, c)


