from django.contrib.auth.models import AbstractUser
from django.db import models


class Bitcoin(models.Model):
    created_by = models.ForeignKey(
        'CustomUser', max_length=500, on_delete=models.CASCADE)
    coin_name = models.CharField(max_length=500)
    current_price = models.FloatField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, max_length=100)

    class Meta:
        ordering = ['-created_at']


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=100, unique=True, blank=False, null=False)
    email = models.EmailField(
        max_length=100, unique=True, blank=False, null=False)
    password = models.CharField(max_length=100, null=False, blank=False)
