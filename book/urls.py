from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("create_book", views.create_book, name="create_book"),
    path("book/<slug:slug>/edit/", views.edit_book, name="edit_book"),
    path("book/<slug:slug>/delete/", views.delete_book, name="delete_book"),
    path("book/<slug:slug>/",
         views.book_detail, name='book_detail'),
    path("genre/<slug:slug>", views.list_genres, name="list_genres"),
    path("add_genre", views.add_genre, name="add_genre"),

]
