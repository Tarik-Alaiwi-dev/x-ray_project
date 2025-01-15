from django.http import JsonResponse

from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import PredictionSerializer, PatientSerializer

from .model import load_model, predict
from .models import Prediction, Patient

import os

# Load the pre-trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'chest_xray_model.pth')
model = load_model(MODEL_PATH)

class PredictionListAPIView(generics.GenericAPIView):
    serializer_class = PredictionSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get(self, request, *args, **kwargs):
        latest_object = Prediction.objects.filter(user=request.user).order_by('-date').first()

        if latest_object:
            serializer = self.get_serializer(latest_object)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"error": "No predictions found for this user."}, status=404)
    
    

class ImageClassificationView(generics.CreateAPIView):
    serializer_class = PredictionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Retrieve the uploaded image
        image = serializer.validated_data['image']

        # Preprocess and predict the class
        prediction_result = predict(image, MODEL_PATH)

        # Save the prediction to the database
        prediction = Prediction.objects.create(image=image, inference=prediction_result)
        prediction.save()

        # Return the result
        return Response({
            'inference': prediction_result
        }, status=status.HTTP_200_OK)
    

# Widok do pobrania i edycji pacjenta (tylko dla zalogowanego użytkownika)
class PatientDetailView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  # Pacjent może edytować tylko swoje dane

# Widok do logowania i generowania tokena JWT
class PatientLoginView(generics.GenericAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


