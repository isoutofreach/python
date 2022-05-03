from django.shortcuts import HttpResponse, render


def get_timer(request):
    import datetime
    now = datetime.datetime.now().strftime("%Y-%m-%d %X")

    return render(request, "timer.html", {"show_time": now})


def login(request):
    return render(request, "log-from.html")


def result(request):
    data = request.POST
    if request.POST.get("user") == "yinzijian" and request.POST.get("pwd") == "123":
        result = "ok"
    else:
        result = "user or passwd is false"
    return render(request, "result.html", {"result": result})


def get_ncov(request):
    return render(request, "ncov.html")
