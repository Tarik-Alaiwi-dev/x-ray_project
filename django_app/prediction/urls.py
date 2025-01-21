from django.urls import path
from .views import PredictionListAPIView, ImageClassificationView, PatientDetailView, PatientLoginView

urlpatterns = [
    # path('get-form/', PredictionListAPIView.as_view(), name='get-form'),
    path('predict/', ImageClassificationView.as_view(), name='predict'),
    path('predictions/<int:pk>/', PredictionListAPIView.as_view(), name='get-latest-prediction'),
    path('patient-info/', PatientDetailView.as_view(), name='patient-info'),
    path('patient-login/', PatientLoginView.as_view(), name='patient-login'),
]
