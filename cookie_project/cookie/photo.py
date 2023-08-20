from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
import os

@api_view(['POST'])
def upload_and_display_photo(request):
    if 'file' in request.FILES:
        photo = request.FILES['file']

        # 파일을 저장할 디렉터리 설정
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(photo.name, photo)

        # 파일 URL 생성
        file_url = fs.url(filename)

        # index.html 템플릿 렌더링
        return Response({'message': '사진 업로드 및 표시 성공', 'file_url': file_url}, status=status.HTTP_201_CREATED)
        return Response({'message': '파일이 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)