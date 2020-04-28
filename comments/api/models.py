from django.db import models
from uuid import uuid4


class Comment(models.Model):
    # id = models.UUIDField(primary_key = True, default = uuid4)
    author = models.UUIDField()
    news = models.UUIDField()
    body = models.TextField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
