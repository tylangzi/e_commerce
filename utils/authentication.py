from django.contrib.auth.backends import ModelBackend
from main.models import *

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 先尝试在商家表中认证
        merchant = Merchant.objects.filter(username=username, password=password).first()
        if merchant:
            return merchant

        # 尝试在消费者表中认证
        consumer = Consumer.objects.filter(username=username, password=password).first()
        if consumer:
            return consumer

        return None