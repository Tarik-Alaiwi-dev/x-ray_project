from django.urls import path
from .views import PredictionListAPIView
from .views import ImagePredictionView

urlpatterns = [
    path('get-form/', PredictionListAPIView.as_view(), name='get-form'),
    # path('predict/', ImageClassificationView.as_view(), name='predict'),
    path('classify/', ImagePredictionView.as_view(), name='classify_image'),
]

