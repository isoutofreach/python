from django.shortcuts import render, HttpResponse, redirect
from book01.models import *


# Create your views here.

def multi(request):
    # 方法一:
    # pub = Publish.objects.get(name="苹果出版社")
    # publish_id = pub  会自动默认的把查询对应的id赋值
    # book = Book.objects.create(title="西游记", price=199, pub_date="2012-12-12", publish=pub)

    # 方法二:

    # book = Book.objects.create(title="红楼梦", price=299, pub_date="2012-12-12", publish_id=2)

    return HttpResponse("OK")


def book(request):
    book = Book.objects.all()
    return render(request, "book01_book.html", {"book_list": book})


def add_book(request):
    if request.method == "GET":
        publish_list = Publish.objects.all()
        authors_list = Author.objects.all()
        return render(request, "book01_add_book.html", {"publish_list": publish_list, "authors_list": authors_list})
    else:
        data = request.POST.dict()
        authors_id_list = request.POST.getlist("authors_id_list")
        data.pop("authors_id_list")
        new_book = Book.objects.create(**data)

        # 绑定多对多关系
        new_book.authors.add(*authors_id_list)

        return redirect("/book01/book")
