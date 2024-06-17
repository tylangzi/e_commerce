

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.

class Consumer(models.Model):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    nickname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10, choices=(('0', '男'), ('1', '女')), blank=True)
    last_login = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nickname