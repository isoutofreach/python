from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse


def get_timer(requset):
    import datetime
    now = datetime.datetime.now().strftime("%Y-%m-%d %X")
    return HttpResponse(now)


def index(request):
    return HttpResponse("hello index")

def login(request):
    return HttpResponse("hello login")