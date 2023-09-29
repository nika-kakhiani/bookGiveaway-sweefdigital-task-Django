from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pages = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    pickup_location = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/", default="default-image.jpg")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book", args=[self.slug])
