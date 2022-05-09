from django.test import TestCase

# Create your tests here.

import requests

data = requests.get("https://2019ncov.chinacdc.cn/JKZX/yq_20220401.json")
print(data.json())