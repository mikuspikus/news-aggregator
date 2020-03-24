from django.db import models
from django.contrib.auth.models import AbstractUser

from uuid import uuid4

from tokenauthentication.models import Token

class AuthUser(AbstractUser):
    uuid = models.UUIDField(unique = True)

    def __str__(self) -> str:
        return f'{self.username} [{self.uuid}]'

class UserAuthToken(Token):
    user = models.OneToOneField(to = AuthUser, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f'Token: <{self.token}:{self.created}> for {self.user}'

class ServicesToken(Token):
    pass