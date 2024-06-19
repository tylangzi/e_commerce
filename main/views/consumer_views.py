from django.urls import reverse

from main.models import Consumer
from utils.jsonresponse import JR


class ConsumerView:
    def register(self, request):
        if request.method == 'POST':
            avatar = request.FILES.get('avatar')
            print(avatar)
            nickname = request.POST.get('nickname')
            username = request.POST.get('username')
            password = request.POST.get('password')
            mobile = request.POST.get('mobile')
            gender = request.POST.get('gender')
            data = {'avatar': avatar,
                    'nickname': nickname,
                    'username': username,
                    'password':  password,
                    'mobile': mobile,
                    'gender': gender}
            consumer = Consumer()
            response = consumer.create_consumer(**data)
            return JR(response)
        else:
            return JR({'message': '请使用POST方法', 'status': 400})
