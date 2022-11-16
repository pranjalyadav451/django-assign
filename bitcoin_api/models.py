from django.contrib.auth.models import AbstractUser
from django.db import models

class Bitcoin(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    coin_name = models.CharField(max_length=50)
    current_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.coin_name


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50,unique=True,blank=False,null=False)
    email = models.EmailField(max_length=50,unique=True,blank=False,null=False)
    password = models.CharField(max_length=50,null=False,blank=False)
