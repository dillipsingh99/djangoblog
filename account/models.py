from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomAccount(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    contact_number = models.PositiveIntegerField(null=True, blank=True)
    img = models.ImageField(default='default.jpg', upload_to='uploaded')
    address = models.CharField(max_length=200)
    education = models.CharField(max_length=200)

    def __str__(self):
        return self.username

