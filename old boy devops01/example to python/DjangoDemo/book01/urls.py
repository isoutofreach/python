from django.urls import path, re_path, include
from book01.views import multi, book, add_book, edit_book, search_book, auth_title, cal

urlpatterns = [
    path('multi/', multi),
    path('book/', book),
    path('add/', add_book),
    re_path('edit/(\d+)', edit_book),
    re_path('book/s', search_book),
    path('auth_title/', auth_title),
    path('cal/', cal)
]
