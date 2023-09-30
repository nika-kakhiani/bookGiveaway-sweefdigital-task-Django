from django.shortcuts import get_object_or_404
from .forms import BookForm, GenreForm, EditBookForm
from django.shortcuts import render, redirect
from .models import Book, Genre, Condition, BookInterest
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse

from rest_framework import generics
from .serializers import GenreSerializer, ConditionSerializer, BookSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.


def home(request):
    all_books = Book.objects.all()

    books_per_page = 10

    paginator = Paginator(all_books, books_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        "page": page,
        "all_books": all_books,
    }
    return render(request, "home.html", context)


def genres(request):
    all_genres = Genre.objects.all()

    return {"all_genres": all_genres}


def list_genres(request, slug=None):
    genre = get_object_or_404(Genre, slug=slug)

    books = Book.objects.filter(genre=genre)

    context = {
        "genre": genre,
        "books": books,
    }

    return render(request, "book/list_genres.html", context)


@login_required(login_url="login")
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.slug = slugify(book.title)
            book.save()
            messages.success(request, 'Book added successfully.')
            return redirect('book_detail', slug=book.slug)
        else:
            messages.error(
                request, 'Error adding the book. Please correct the errors below.')
    else:
        form = BookForm()

    context = {
        'form': form,
    }
    return render(request, 'book/create_book.html', context)


def edit_book(request, slug):
    book = get_object_or_404(Book, slug=slug)

    if request.method == 'POST':
        form = EditBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully.')
            return redirect('book_detail', slug=book.slug)
    else:
        form = EditBookForm(instance=book)

    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'book/edit_book.html', context)


def delete_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        book.delete()
        return redirect('home')

    context = {
        'book': book,
    }
    return render(request, 'book/delete_book.html', context)


def add_genre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save(commit=False)
            genre.slug = slugify(genre.name)
            genre.save()
            return redirect("home")
    else:
        form = GenreForm()

    context = {
        "form": form,
    }
    return render(request, "book/add_genre.html", context)


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    context = {
        'book': book,
        "book_owner": book.owner,
        "user": request.user
    }
    return render(request, 'book/book_detail.html', context)


def get_pickup_location(request, slug):
    book = get_object_or_404(Book, slug=slug)

    context = {
        'pickup_location': book.pickup_location,
    }
    return JsonResponse(context)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def express_interest(request, slug):
    book = get_object_or_404(Book, slug=slug)

    existing_interest = BookInterest.objects.filter(
        user=request.user, book=book).exists()
    if existing_interest:
        return Response({"error": "You have already expressed interest in this book."}, status=400)

    BookInterest.objects.create(user=request.user, book=book)

    return Response({"message": "Interest expressed successfully."}, status=200)


class GenreListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ConditionListView(generics.ListCreateAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
