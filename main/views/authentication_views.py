from django.contrib.auth import login
from utils.authentication import CustomAuthBackend
from utils.jsonresponse import JR


class AuthenticationView:
    def user_login(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = CustomAuthBackend().authenticate(request, username=username, password=password)
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return JR({'message': '登录成功', 'status': 200,'who': user.username})
            else:
                return JR({'message': '登录失败，用户名或者密码错误', 'status': 401})
        else:
            return JR({'message': '请使用POST方法', 'status': 400})



