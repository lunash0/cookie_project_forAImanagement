from django.urls import path, include, re_path
from .models import Accounts
from . import signup

app_name = 'cookie'

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework_category')),
    path('signup/', signup.insert_sign_info, name='insert_sign_info'),
]