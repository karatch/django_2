from django.db import models

class Post(models.Model):
    # some changes for commit - from X200
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
