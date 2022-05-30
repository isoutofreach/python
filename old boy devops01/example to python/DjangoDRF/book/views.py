from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework.views import APIview


# Create your views here.

class BookView(APIview):


    def get(self, request):
        return HttpResponse("APIview GET请求")

    def post(self, request):
        return HttpResponse("APIview POST请求")

    def delete(self, request):
        return HttpResponse("APIview delete请求")
