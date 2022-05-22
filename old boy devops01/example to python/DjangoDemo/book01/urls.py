from django.urls import path, re_path, include
from book01.views import add

urlpatterns = [
    path('add/', add)

]