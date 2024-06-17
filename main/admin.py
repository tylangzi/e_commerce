from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(consumer.Consumer)
admin.site.register(Merchant)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Address)
admin.site.register(ShoppingCart)
admin.site.register(OrderProduct)
admin.site.register(ShoppingCartItem)
admin.site.register(Inventory)
admin.site.register(Review)
admin.site.register(Transport)
