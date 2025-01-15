from rest_framework import serializers
from .models import Prediction, Patient
from django.contrib.auth.hashers import make_password

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['date', 'inference', 'image']

class PatientSerializer(serializers.ModelSerializer):
    predictions = PredictionSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'username', 'f_name', 'l_name', 'password', 'predictions']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)