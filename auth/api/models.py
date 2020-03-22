from django.db import models
from django.contrib.auth.models import AbstractUser

from uuid import uuid4

from .tokenauthentication.models import Token

class AuthUser(AbstractUser):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)

class AuthToken(Token):
    user = models.OneToOneField(to = AuthUser, on_delete = models.CASCADE)

class AuthServiceToken(Token):
    pass

class CommentsServiceToken(Token):
    pass

class NewsServiceToken(Token):
    pass

class RSSParserServiceToken(Token):
    pass

class StatsServiceToken(Token):
    pass

class UsersServiceToken(Token):
    pass