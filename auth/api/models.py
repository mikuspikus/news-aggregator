from django.db import models
from django.contrib.auth.models import AbstractUser

from uuid import uuid4

from .tokenauthentication.models import Token

class AuthUser(AbstractUser):
    uuid = models.UUIDField(unique = True, default = uuid4, editable = False)

class UserAuthToken(Token):
    user = models.OneToOneField(to = AuthUser, on_delete = models.CASCADE)

class ServicesToken(Token):
    pass