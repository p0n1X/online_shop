from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=False, null=True, unique=True)
    first_name = models.CharField(max_length=50, blank=False, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=True)
    address = models.CharField(max_length=50, blank=False, null=True)
    email = models.CharField(max_length=50, blank=False, null=True)
    password = models.CharField(max_length=100, blank=False, null=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def token(self):
        tokens = Token.objects.filter(user=self).first()
        if tokens:
            return tokens.key
