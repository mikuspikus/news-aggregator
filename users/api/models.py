from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

class User(AbstractUser):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)