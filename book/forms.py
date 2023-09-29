from django import forms
from .models import Book, Genre, Condition


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'condition',
                  'pages', 'description', 'pickup_location', 'image']


class BookFilterForm(forms.Form):
    author = forms.CharField(max_length=255, required=False)
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(), required=False)
    condition = forms.ModelChoiceField(
        queryset=Condition.objects.all(), required=False)
