from django.urls import path, re_path, include
from book01.views import multi, book, add_book

urlpatterns = [
    path('multi/', multi),
    path('book/', book),
    path('add/', add_book)
]