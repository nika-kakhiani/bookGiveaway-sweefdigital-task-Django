from django import forms
from .models import Book, Genre, Condition


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'condition',
                  'pages', 'description', 'pickup_location', 'image']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["name",]


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'condition',
                  'pages', 'description', 'pickup_location', 'image']
