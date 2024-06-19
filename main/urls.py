from django.urls import path
from django.contrib import admin

from main.views import *

app_name = 'main'
urlpatterns = [
    path('user_login/', AuthenticationView().user_login, name='user_login'),
    path('consumer/register/', ConsumerView().register, name='consumer_register'),
]