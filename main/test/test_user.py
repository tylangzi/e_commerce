import requests
import pytest
from django.urls import reverse
import django
from django.conf import settings

# Create your tests here.


class TestUser:
    USER_LOGIN_URL = 'http://127.0.0.1:8000/user_login/'
    @pytest.mark.django_db
    def test_user_login(self):
        data = {
            'username': 'mldr',
            'password': 'mldr'
        }

        response = requests.post(self.USER_LOGIN_URL, data=data)
        print(response.text)