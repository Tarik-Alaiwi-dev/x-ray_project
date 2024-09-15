from django.urls import path
from .views import PredictionListAPIView, ImageClassificationView

urlpatterns = [
    path('get-form/', PredictionListAPIView.as_view(), name='get-form'),
    path('predict/', ImageClassificationView.as_view(), name='predict'),
]
