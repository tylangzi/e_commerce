from django.test import TestCase

# Create your tests here.


import requests

data = {
    'username': 'mldr',
    'password': 'mldr'
}

response = requests.post('http://127.0.0.1:8000/user_login/', data=data)
print(response.text)