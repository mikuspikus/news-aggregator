from django.db import models

class Vote(models.Model):
    user = models.UUIDField(unique = True)

class News(models.Model):
    author = models.UUIDField()
    url = models.URLField()
    title = models.CharField(max_length=128)
    score = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    votes = models.ManyToManyField(to = Vote)

    def __str__(self) -> str:
        return f'"{self.title}" [{self.url}] by ({self.author})'