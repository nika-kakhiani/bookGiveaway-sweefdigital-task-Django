from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("create_book", views.create_book, name="create_book"),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),

]
