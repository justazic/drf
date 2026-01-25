from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=13, unique=True, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username