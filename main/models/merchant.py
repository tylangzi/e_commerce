

from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Merchant(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='merchant_logos/', blank=True, null=True)
    description = RichTextField()
    address = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    establishment_date = models.DateTimeField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    is_active = models.BooleanField(default=True)
    license_number = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    bank_account_info = models.TextField(blank=True)
    last_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
