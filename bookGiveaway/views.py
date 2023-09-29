from django.db.models import Q
from book.models import Book
from django.shortcuts import render


def search_books(request):
    query = request.GET.get('q')
    if query:
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(genre__name__icontains=query) |
            Q(condition__name__icontains=query) |
            Q(description__icontains=query) |
            Q(pickup_location__icontains=query)
        )
    else:
        results = Book.objects.all()  # Show all books if no query is provided

    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'search_results.html', context)
