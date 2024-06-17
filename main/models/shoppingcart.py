from django.db import models


class ShoppingCart(models.Model):
    consumer = models.ForeignKey('Consumer', on_delete=models.CASCADE)

    def __str__(self):
        return f"购物车:{self.consumer}"


class ShoppingCartItem(models.Model):
    shoppingcart = models.ForeignKey('ShoppingCart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)