from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Accounts

@api_view(['POST'])
def insert_sign_info(request):
    if request.method == 'POST':
        user_id = request.data.get('USER_ID')
        password = request.data.get('PASSWORD')

        Accounts.objects.create(USER_ID=user_id, PASSWORD=password)

        return JsonResponse({'message': '회원가입 성공'}, status=201)