from django.db import models

class Feed(models.Model):
    user = models.UUIDField()
    url = models.URLField(max_length=200)