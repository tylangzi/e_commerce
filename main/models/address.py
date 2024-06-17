from django.db import models


class Address(models.Model):
    destination = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.destination}"