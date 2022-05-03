import requests

data = requests.get("https://2019ncov.chinacdc.cn/JKZX/yq_20220401.json")
res = data.json()['features']['properties']
print(res)