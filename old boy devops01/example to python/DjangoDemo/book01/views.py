from django.shortcuts import render, HttpResponse
from book01.models import *


# Create your views here.

def add(request):
    # 方法一:
    #pub = Publish.objects.get(name="苹果出版社")
    # publish_id = pub  会自动默认的把查询对应的id赋值
    #book = Book.objects.create(title="西游记", price=199, pub_date="2012-12-12", publish=pub)

    # 方法二:

    #book = Book.objects.create(title="红楼梦", price=299, pub_date="2012-12-12", publish_id=2)

    return HttpResponse("OK")
