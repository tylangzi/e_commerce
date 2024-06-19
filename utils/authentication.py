from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password

from main.models import *

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 先尝试在商家表中认证
        merchant = Merchant.objects.filter(username=username).first()
        if merchant and check_password(password, merchant.password):
            return merchant

        # 尝试在消费者表中认证
        consumer = Consumer.objects.filter(username=username).first()
        if consumer and check_password(password, consumer.password):
            return consumer

        return None