from django.urls import path
from .views import PredictionView

urlpatterns = [
    path('submit-form/', PredictionView.as_view(), name='submit-form'),
]
