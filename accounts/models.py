from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    telefon = models.CharField(max_length=13)

    def __str__(self):
        return self.username
    