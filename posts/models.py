from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Book(models.Model):
    title = models.CharField(max_length=25, help_text='Enter the book name')

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['-last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

    def get_absolute_url(self):
        return f'/person/{self.pk}'


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.CharField(max_length=255, unique=True, verbose_name='URL имя')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title