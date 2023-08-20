from django.urls import path, include, re_path
from .models import Accounts
#from .views import CreatePetInfo
from . import login
from . import photo

app_name = 'cookie'

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework_category')),
    path('sign_up/', login.create_sign_info, name='create_sign_info'),
    path('log_in/', login.read_login_info, name='read_login_info'),
    path('photo_upload/', photo.upload_and_display_photo, name='upload_and_display_photo'),
    # path('pet_info/', CreatePetInfo.as_view(), name="create_pet_info"),
]