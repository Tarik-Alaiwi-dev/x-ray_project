from django.http import JsonResponse

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import status

from .serializers import PredictionSerializer

from .model import predict
from .models import Prediction

from gradio_client import Client, FileData

import os
import io


# Load the pre-trained model
# MODEL_PATH = os.path.join(os.path.dirname(__file__), 'chest_xray_model.pth')
# model = load_model(MODEL_PATH)

class PredictionListAPIView(generics.GenericAPIView):
    serializer_class = PredictionSerializer

    def get(self, request, *args, **kwargs):
        # Get the latest record by 'date' field
        latest_object = Prediction.objects.latest()
        serializer = self.get_serializer(latest_object)
        return JsonResponse(serializer.data, safe=False)

# class ImageClassificationView(generics.CreateAPIView):
#     serializer_class = PredictionSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         # Save the image to the database
#         prediction = serializer.save()

#         # Get the full path of the saved image from the model
#         image_path = prediction.image.path

#         try:
#             # Open the image file in binary mode
#             with open(image_path, 'rb') as image_file:
#                 # Create a Gradio client for the Hugging Face Space
#                 client = Client("TarikKarol/pneumonia")

#                 # Send the binary image file to the Gradio Space for prediction
#                 result = client.predict(
#                     FileData(name=os.path.basename(image_path), file_obj=image_file),  # Use FileData with file object
#                     api_name="/predict"
#                 )

#                 # Debugging: Print the raw result to see what we receive
#                 print("Raw prediction result:", result)

#                 # Define class names based on your model's output
#                 class_names = ['YOU PROBABLY DO NOT HAVE PNEUMONIA', 'YOU MIGHT HAVE PNEUMONIA']

#                 # Access the predicted class (adjust index based on result structure)
#                 predicted_class_index = int(result[0])  # Assuming the result is a list
#                 predicted_class = class_names[predicted_class_index]

#                 # Update the prediction object with the result
#                 prediction.inference = predicted_class
#                 prediction.save()

#         except Exception as e:
#             print("Error during prediction:", e)
#             return Response({"error": "Prediction failed."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         # Return the result
#         return Response({
#             'inference': prediction.inference,
#             'image_url': prediction.image.url  # Assuming image.url works correctly
#         }, status=status.HTTP_201_CREATED)
    
import requests
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import ImageUploadSerializer
from .models import Prediction

class ImagePredictionView(generics.CreateAPIView):
    serializer_class = ImageUploadSerializer

    def perform_create(self, serializer):
        # Save the image in the database (this will call the `create()` method in the serializer)
        prediction_instance = serializer.save()  # Save the image first
        image = prediction_instance.image  # Get the saved image

        # Convert the image file to bytes
        image_path = image.path
        with open(image_path, 'rb') as image_file:
            image_bytes = image_file.read()

        # Hugging Face Space API URL
        huggingface_api_url = "https://tarikkarol-pneumonia.hf.space/call/predict"

        response = requests.post(huggingface_api_url, files={'image': image_bytes})

        result = response.json()
        print(result)

        # Send the image to Hugging Face API
        try:
            response = requests.post(huggingface_api_url, files={'image': image_bytes})

            result = response.json()
            print(result)

            # Check for a successful response
            if response.status_code == 200:
                result = response.json()
                
                # Debugging: Print the raw result to see what we receive
                print("Raw prediction result:", result)

                # Assuming the prediction result is a list or dictionary (adjust according to the actual response structure)
                # Check the structure of the result
                if isinstance(result, dict) and 'predictions' in result:
                    prediction_values = result['predictions']
                    # Assuming the prediction value is an index of the class
                    if isinstance(prediction_values, list) and len(prediction_values) > 0:
                        predicted_class_index = int(prediction_values[0])  # Get the index
                    else:
                        return Response({"error": "Invalid prediction format"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return Response({"error": "Invalid prediction format"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                # Define class names based on your model's output
                class_names = ['YOU PROBABLY DO NOT HAVE PNEUMONIA', 'YOU MIGHT HAVE PNEUMONIA']

                # Get the predicted class
                predicted_class = class_names[predicted_class_index]

                # Save the prediction result in the database
                prediction_instance.inference = predicted_class
                prediction_instance.save()

                return Response({
                    "inference": predicted_class,
                    "image_url": image.url
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"error": "Failed to get a valid response from Hugging Face"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





    


