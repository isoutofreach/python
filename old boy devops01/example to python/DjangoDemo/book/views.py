from django.shortcuts import render, HttpResponse, redirect
from book.models import Book

# Create your views here.
'''
python     sql
模型类      table

'''


def add_book(request):
    if request.method == "GET":
        return render(request, "add_book.html")
    else:
        Book.objects.create(**request.POST.dict())
        return redirect("/book/select_book")


def select_book(request):
    book_list = Book.objects.all()

    return render(request, "books.html", {"book_list": book_list})


def update_book(request):
    Book.objects.filter(price=455).update(price="500")

    return HttpResponse("OK")


def delete_book(request, delete_id):
    if request.method == "GET":
        book = Book.objects.get(pk=delete_id)
        return render(request, "delete_book.html", {"book": book})
    else:
        Book.objects.filter(pk=delete_id).delete()
        return redirect("/book/select_book")
