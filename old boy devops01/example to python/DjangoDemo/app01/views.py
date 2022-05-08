from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
import datetime


def get_timer(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %X")
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
            return HttpResponse("验证成功")
        else:
            return HttpResponse("用户名或者密码错误")

