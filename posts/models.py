from django.db import models

class Post(models.Model):
    # some changes for commit - from X200
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Введите жанр книги')


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['last_name',]


class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=255, help_text='Введите описание книги')
    isbn = models.CharField(max_length=13, help_text='Введите код ISBN')
    genre = models.ManyToManyField(Genre, help_text='Введите жанр книги')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)