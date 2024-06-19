import pytest
import requests


class TestConsumer:
    CONSUMER_REGISTER_URL = 'http://127.0.0.1:8000/consumer/register/'

    def test_consumer_register(self):
        with open('image/zhaoming.png', 'rb') as f:
            avatar_data = f.read()

        files = {
            'avatar': ('zhaoming.png', avatar_data, 'image/png')
        }

        data = {
            'nickname': 'zhaoming',
            'username': 'zhaoming',
            'password': 'zhaoming',
            'mobile': '13333333333',
            'gender': '0',
        }

        response = requests.post(self.CONSUMER_REGISTER_URL, files=files, data=data)
        print(response.json())
