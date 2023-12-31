# Generated by Django 4.2.5 on 2023-09-29 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0006_condition_genre_alter_book_condition_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="condition",
            name="slug",
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="genre",
            name="slug",
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
