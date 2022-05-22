"""DjangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from app01.views import get_timer, index, articleByYear, articleByMonth

urlpatterns = [
    # re_path('^article/\d{4}$', article),     # 正则匹配
    re_path('^article/(\d{4})$', articleByYear),  # 分组传递参数
    re_path('^article/(\d{4})/(\d{1,2})$', articleByMonth),  # 多分组传递参数
    re_path('^article/(?P<year>\d{4})/(?P<month>\d{1,2})$', articleByMonth),  # 有名分组传递参数,将位置传参改成了关键字传参
    path('admin/', admin.site.urls),
    # path('timer', get_timer),
    path('', index),
    path('app01/', include("app01.urls")),
    # path('login/', login),
    # path("muban/", muban),
    # path("books/", books),
    # path("2019ncov", get_ncov)
    path("book/", include("book.urls")),
    path("book01/", include("book01.urls")),
]
