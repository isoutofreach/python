from django.urls import path, re_path, include
from book.views import add_book, select_book, delete_book, edit_book

urlpatterns = [

    path("add_book", add_book, name="add_book"),
    path("", select_book, name="book_select"),
    # path("update_book", update_book),
    re_path("delete_book/(\d+)", delete_book),
    re_path("edit/(\d+)", edit_book, name= "edit_book"),
]
