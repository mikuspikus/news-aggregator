from django.db import models
from uuid import uuid4


class User(models.Model):
    uuid = models.UUIDField(unique=True)

    def __str__(self) -> str:
        return self.uuid


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    author = models.UUIDField()
    url = models.URLField()
    title = models.CharField(max_length=128)
    score = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    votes = models.ManyToManyField(to=User, through='Vote')

    class Meta:
        verbose_name_plural = "News"

    def __str__(self) -> str:
        return f'"{self.title}" [{self.url}] by ({self.author})'


class Vote(models.Model):

    IS_UP_CHOICES = (
        (True, 'up'),
        (False, 'down')
    )

    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE)
    news = models.ForeignKey(
        to=News, on_delete=models.CASCADE)
    is_up = models.BooleanField(choices = IS_UP_CHOICES, default=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        vote = 'upvoted' if self.is_upvote() else 'downvoted'

        return f'{self.news} {vote} by {self.user}'