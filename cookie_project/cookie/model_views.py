from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from PIL import Image
from io import BytesIO
import numpy as np
import os
import json
from .dncskin_segmentation import common_conf, function, run_segmentation

@api_view(['POST'])
def predict_view(request):
    if 'temp_image' in request.FILES:            
        image_file = request.FILES['temp_image']
        image = Image.open(image_file)

        image_stream = BytesIO()
        image.save(image_stream, format='JPEG')
        image_stream.seek(0)

        img_overlays, pred_clses = run_segmentation.predict(image_stream)

        combined_image = Image.new('RGB', img_overlays[0].size)
        for idx, overlay in enumerate(img_overlays):
            if pred_clses[idx]:
                combined_image.paste(overlay, (0, 0), overlay)

        image_dir = os.path.join(os.path.dirname(__file__), 'dncskin_segmentation', 'return')
        combined_image_path = os.path.join(image_dir, 'combined_image.jpg')
        combined_image.save(combined_image_path, format='JPEG')

        pred_clses_path = os.path.join(image_dir, 'pred_clses.txt')
        with open(pred_clses_path, 'w') as f:
            f.write('\n'.join(map(str, pred_clses)))

        json_data = {
            'success': True,
            'message': 'Prediction and image synthesis complete',
            'combined_image_path': combined_image_path,
            'pred_clses_count': len(pred_clses),
        }

        return JsonResponse(json_data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)