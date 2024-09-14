from django.urls import path
from .views import PredictionCreateView, PredictionListAPIView, ImageClassificationView

urlpatterns = [
    path('submit-form/', PredictionCreateView.as_view(), name='submit-form'),
    path('get-form/', PredictionListAPIView.as_view(), name='get-form'),
    path('predict/', ImageClassificationView.as_view(), name='predict'),
]
