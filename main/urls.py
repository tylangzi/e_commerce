from django.urls import path
from django.contrib import admin

from main.views import UserHandler

app_name = 'main'
urlpatterns = [
    path('user_login/', UserHandler().user_login, name='user_login'),
]