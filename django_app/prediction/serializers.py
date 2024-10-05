from rest_framework import serializers
from .models import Prediction

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['date', 'inference', 'image']

from rest_framework import serializers

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['image']

    def create(self, validated_data):
        # This method is called during the save() method in the view
        return Prediction.objects.create(**validated_data)
