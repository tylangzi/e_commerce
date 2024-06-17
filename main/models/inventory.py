from django.db import models

class Inventory(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    last_update_time = models.DateTimeField(auto_now=True)