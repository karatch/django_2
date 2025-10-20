from django.contrib import admin

from posts.models import Post, Book, Person, Group

admin.site.register(Post)
admin.site.register(Book)
admin.site.register(Person)
admin.site.register(Group)
