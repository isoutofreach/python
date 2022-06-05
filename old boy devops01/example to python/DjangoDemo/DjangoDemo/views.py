from django.shortcuts import render, HttpResponse, redirect


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "yuan" and pwd == "123":
            # return HttpResponse("验证成功")
            return redirect("/timer")
        else:
            return HttpResponse("用户名或者密码错误")