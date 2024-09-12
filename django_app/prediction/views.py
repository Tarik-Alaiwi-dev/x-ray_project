from django.shortcuts import render

from rest_framework import generics
from .models import Prediction
from .serializers import PredictionSerializer

class PredictionView(generics.CreateAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
