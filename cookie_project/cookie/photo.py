import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

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
        return Response({'message': '사진 업로드 성공', 'file_url': file_url}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': '파일이 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    

# @api_view(['DELETE'])
# def delete_photo(request, file_path):
#     try:
#         # 이미지 파일의 경로에서 파일을 삭제
#         if os.path.exists(file_path):
#             os.remove(file_path)
#             return Response({'message': '이미지 삭제 성공'}, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({'message': '이미지가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'message': '이미지 삭제 실패', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)