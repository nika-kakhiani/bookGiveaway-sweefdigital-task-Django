from django.shortcuts import get_object_or_404
from .forms import BookForm, BookFilterForm
from django.shortcuts import render, redirect
from .models import Book
from django.contrib import messages

# Create your views here.


def home(request):
    all_books = Book.objects.all()

    context = {
        "all_books": all_books,
    }
    return render(request, "home.html", context)


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            messages.success(request, 'Book added successfully.')
            return redirect('book_detail', pk=book.pk)
        else:
            messages.error(
                request, 'Error adding the book. Please correct the errors below.')
    else:
        form = BookForm()

    context = {
        'form': form,
    }
    return render(request, 'book/create_book.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    context = {
        'book': book,
    }
    return render(request, 'book/book_detail.html')


def filter_books(request):
    if request.method == 'POST':
        form = BookFilterForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data.get('author')
            genre = form.cleaned_data.get('genre')
            condition = form.cleaned_data.get('condition')

            filtered_books = Book.objects.all()
            if author:
                filtered_books = filtered_books.filter(author=author)
            if genre:
                filtered_books = filtered_books.filter(genre=genre)
            if condition:
                filtered_books = filtered_books.filter(condition=condition)

            return render(request, 'filtered_books.html', {'filtered_books': filtered_books})
    else:
        form = BookFilterForm()

    context = {
        'form': form,
    }
    return render(request, 'filter_books.html', context)
