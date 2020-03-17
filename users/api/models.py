from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

class CustomUser(AbstractUser):
    uuid = models.UUIDField(unique = True, default = uuid4, editable = False)