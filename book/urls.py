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


    path('api/genres/', views.GenreListView.as_view(), name='genre-list'),
    path('api/conditions/', views.ConditionListView.as_view(), name='condition-list'),
    path('api/books/', views.BookListView.as_view(), name='book-list'),
    path('api/books/<slug:slug>/',
         views.BookDetailView.as_view(), name='book-detail'),

    path('api/books/<slug:slug>/pickup-location/',
         views.get_pickup_location, name='get_pickup_location'),

    path("book/<slug:slug>/express_interest/",
         views.express_interest, name="express_interest"),

    path('book/<slug:slug>/choose_recipient/',
         views.choose_recipient, name='choose_recipient'),

    path('book/<slug:slug>/interested_users/',
         views.interested_users_list, name='interested_users_list'),


]
