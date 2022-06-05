import json

from django.shortcuts import render, HttpResponse, redirect
from book01.models import *
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage


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
    keyword = request.GET.get("keyword")

    book = Book.objects.all()

    if keyword:
        book = Book.objects.filter(title__contains=keyword)
        book_kw = keyword

    book_kw = None
    paginator = Paginator(book, 3)  # 3条数据一页
    current_page = int(request.GET.get("page", 1))  # 如果page取不到值就拿1当默认值
    try:
        book = paginator.page(current_page)  # 取page页数
    except EmptyPage:
        book = paginator.page(1)
    has_previous = book.has_previous()
    has_next = book.has_next()
    # print("count:", paginator.count)  # 数据总数
    # print("num_pages", paginator.num_pages)  # 总页数
    # print("page_range", paginator.page_range)  # 页码的列表

    # page2 = paginator.page(2)
    # print(page2.has_next())  # 是否有下一页
    # print(page2.next_page_number())  # 下一页的页码
    # print(page2.has_previous())  # 是否有上一页
    # print(page2.previous_page_number())  # 上一页的页码

    return render(request, "book01_book.html",
                  {"book_list": book, "book_kw": book_kw, "paginator": paginator, "current_page": current_page,
                   "has_next": has_next, "has_previous": has_previous})


def add_book(request):
    if request.method == "GET":
        publish_list = Publish.objects.all()
        authors_list = Author.objects.all()
        return render(request, "book01_add_book.html", {"publish_list": publish_list, "authors_list": authors_list})
    else:

        authors_id_list = request.POST.getlist("authors_id_list")
        data = request.POST.dict()
        data.pop("authors_id_list")
        new_book = Book.objects.create(**data)

        # 绑定多对多关系
        new_book.authors.add(*authors_id_list)

        return redirect("/book01/book")


def edit_book(request, edit_id):
    if request.method == "GET":
        # 获取正在编辑的数据对象
        edit_book = Book.objects.get(pk=edit_id)
        publish_list = Publish.objects.all()
        authors_list = Author.objects.all()
        return render(request, "book01_edit_book.html",
                      {"edit_book": edit_book, "publish_list": publish_list, "authors_list": authors_list})
    else:
        # 编辑提交的数据
        authors_id_list = request.POST.getlist("authors_id_list")
        print(authors_id_list)
        data = request.POST.dict()
        data.pop("authors_id_list")
        Book.objects.filter(pk=edit_id).update(**data)
        edit_book = Book.objects.get(pk=edit_id)
        edit_book.authors.set(authors_id_list)
        return redirect("/book01/book")


def search_book(request):
    keyword = request.GET.get("keyword")
    print(keyword)
    book_list = Book.objects.filter(title__contains=keyword)

    return render(request, "book01_book.html", {"book_list": book_list})


def auth_title(reques):
    print(reques.GET)
    title = reques.GET.get("title")
    ret = Book.objects.filter(title=title)
    res = {"is_exist":False,"msg":""}

    if ret:
        res["is_exist"] = True
        res["msg"] = "该书籍已存在"

    return HttpResponse(json.dumps(res,ensure_ascii=False))

from django.http import JsonResponse

def cal(request):

    n1 = request.GET.get("num1")
    n2 = request.GET.get("num2")
    ret = int(n1) + int(n2)
    res = {
        "ret": ret
    }
    return JsonResponse(res)