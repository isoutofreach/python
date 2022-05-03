from django.test import TestCase

# Create your tests here.
import requests

res = requests.get("https://2019ncov.chinacdc.cn/JKZX/yq_20220401.json")
data = res.json()["features"]

for item in data:
    name = print(item.get("properties").get("name"))
    yisi = print(item.get("properties").get("新增疑似"))
    total = print(item.get("properties").get("累计确诊"))
    recentDead = print(item.get("properties").get("新增死亡"))
    totalDead = print(item.get("properties").get("累计死亡"))


