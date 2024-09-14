from django.shortcuts import render

from rest_framework import generics, status
from .models import Prediction
from .serializers import PredictionSerializer

from django.http import JsonResponse

from .model import load_model, preprocess_image
import torch

import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from .model import load_model, predict
from .models import Prediction
from PIL import Image

# Load the pre-trained model (assuming it is saved as 'model.pth')
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'chest_xray_model.pth')
model = load_model(MODEL_PATH)

class PredictionCreateView(generics.CreateAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer

class PredictionListAPIView(generics.GenericAPIView):
    serializer_class = PredictionSerializer

    def get(self, request, *args, **kwargs):
        # Get the latest record by 'date' field
        latest_object = Prediction.objects.latest()
        serializer = self.get_serializer(latest_object)
        return JsonResponse(serializer.data, safe=False)
    

class ImageClassificationView(generics.CreateAPIView):
    serializer_class = PredictionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Retrieve the uploaded image
        image = serializer.validated_data['image']

        # Preprocess the image
        processed_image = preprocess_image(image)

        # Make the prediction using the loaded model
        with torch.no_grad():
            output = model(processed_image)
            prediction = torch.sigmoid(output).item()

        # Convert the prediction to a binary class (0 or 1)
        predicted_class = 1 if prediction > 0.5 else 0

        # Return the result
        return Response({
            'prediction': predicted_class,
            'confidence': prediction
        }, status=status.HTTP_200_OK)

