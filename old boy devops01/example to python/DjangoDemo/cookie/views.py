from django.shortcuts import render, HttpResponse, redirect
from cookie.models import *


# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        try:
            user = UserInfo.objects.get(user=user, pwd=pwd)
            # 对响应体设置cookie
            res = redirect("/timer")
            res.set_cookie("isLogin", "True")
            # max_age: 有效时间为10秒,10秒后会自动删除cookie
            # expires: 设置有效时间, 接收日期类型
            # path: 设置路径, 只对某些路径有效
            res.set_cookie("username", user.user, max_age=10,expires=None,path='/')
            # return redirect("/timer")
            return res
        except Exception as e:
            print(e)
            return redirect("/login")
