from django.shortcuts import HttpResponse, render, redirect
import datetime
import requests


def books(request):
    books = ["AAA", "BBB", "CCC", "DDD"]

    age = 15
    return render(request, "books.html", {"books": books, "age": age})


def test(request):
    return redirect("/timer/")


def get_timer(request):
    now = datetime.datetime.now()

    return render(request, "timer.html", {"now": now})


def get_ncov(request):
    res = requests.get("https://2019ncov.chinacdc.cn/JKZX/yq_20220401.json")
    data = res.json()["features"]

    return render(request, "ncov.html", {"data": data})


def artical(request, year):
    return HttpResponse(year + " artical文章列表")
