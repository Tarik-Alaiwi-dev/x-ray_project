from django.shortcuts import render

from rest_framework import generics
from .models import Prediction
from .serializers import PredictionSerializer

from django.http import JsonResponse

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
