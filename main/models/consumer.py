from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.

class Consumer(models.Model):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    nickname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10, choices=(('0', '男'), ('1', '女')), blank=True)
    last_login = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nickname

    @classmethod
    def create_consumer(cls, *args, **kwargs):
        avatar = kwargs.get('avatar')
        nickname = kwargs.get('nickname')
        username = kwargs.get('username')
        password = kwargs.get('password')
        mobile = kwargs.get('mobile')
        gender = kwargs.get('gender')

        required_fields = ['nickname', 'username', 'password']
        for field in required_fields:
            if not locals()[field]:
                return {'status':'400', 'message':f'{field}不能为空'}

        hashed_password = make_password(password)
        consumer = Consumer(
            avatar = avatar,
            nickname = nickname,
            username = username,
            password = hashed_password,
            mobile = mobile,
            gender = gender,
        )

        try:
            consumer.save()
            return {'status':200, 'message':'消费者创建成功'}
        except Exception as e:
            return {'status':400, 'message': f'创建消费者时出错：{str(e)}'}



