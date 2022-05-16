from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, render, redirect
import datetime


def get_timer(request):
    now = datetime.datetime.now()
    print(request.method)
    print(request.path)
    print(request.get_full_path())
    print(request.META)
    print(request.GET)
    print(request.POST)
    user = request.POST.get("user")
    print(user)
    hobby = request.POST.getlist("hobby")
    print(hobby)
    return render(request, "timer.html", {"showtime": now})


def index(request):
    return HttpResponse("hello index")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "yuan" and pwd == "123":
            # return HttpResponse("验证成功")
            return redirect("/timer")
        else:
            return HttpResponse("用户名或者密码错误")


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def muban(request):
    name = "yin"
    books = ["西游记", "三国演义", "水浒传", "红楼梦"]
    info = {"name": "rain", "age": 23}
    s1 = Student("yuan", 22)
    s2 = Student("rain", 22)
    s3 = Student("alvin", 22)
    stus = [s1, s2, s3]

    import datetime
    now = datetime.datetime.now()
    fileSize = 123123123123

    import requests
    data = requests.get("https://2019ncov.chinacdc.cn/JKZX/yq_20220401.json")
    # print(data.json()['features'][0]['properties'])
    yiqing = data.json()["features"]
    # print(yiqing)

    return render(request, "muban.html",
                  {"name": name, "books": books, "info": info, "stus": stus, "now": now, "filesize": fileSize,
                   "yiqinglist": yiqing})


def books(request):
    age = 188
    books = ["AA", "BB", "CC", "DD"]
    return render(request, "books.html", {"books": books, "age": age})


def get_ncov(request):
    import requests
    res = requests.get("https://2019ncov.chinacdc.cn/JKZX/yq_20220401.json")
    data = res.json()["features"]

    return render(request, "ncov.html", {"data": data})


def articleByYear(request, year):
    return HttpResponse(year + "aticale文章列表")


def articleByMonth(request, year, month):
    return HttpResponse(f"{year}年{month}月的文章")