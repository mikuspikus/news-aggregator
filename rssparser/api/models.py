from django.db import models

class Feed(models.Model):
    user = models.UUIDField()
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=200)