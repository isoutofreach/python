from django.urls  import path
from app01.views import login, muban, books, get_ncov, get_timer


urlpatterns = [
    path('login/', login),
    path("muban/", muban),
    path("books/", books, name="app01_book"),
    path("2019ncov", get_ncov, name="app01_get_ncov"),
    path('timer', get_timer, name="app01_get_timer"),
]