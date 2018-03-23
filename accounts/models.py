from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.CharField(max_length=200, null=True)
    is_blogger = models.BooleanField(default = False)

