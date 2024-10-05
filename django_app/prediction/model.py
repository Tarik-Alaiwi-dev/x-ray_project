import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
from io import BytesIO
import os
import io
import base64

from gradio_client import Client, handle_file
from gradio_client.data_classes import FileData
from tempfile import NamedTemporaryFile

# Load the model
def load_model(model_path):
    model = models.resnet18(pretrained=False)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 2)

    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

# Preprocess uploaded image or image path/URL
def preprocess_image(image_file):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]) 
    ])

    # Handle both file path and InMemoryUploadedFile objects (from Django)
    if isinstance(image_file, BytesIO) or hasattr(image_file, 'read'):
        image = Image.open(image_file).convert('RGB')
    else:
        image = Image.open(image_file).convert('RGB')

    image = transform(image)
    image = image.unsqueeze(0)  
    return image

# Predict the class of the image
def predict(image_file):
    # Create a Gradio client for the Hugging Face Space
    client = Client("TarikKarol/pneumonia")

        # Send the temporary image file to the Gradio Space for prediction
    result = client.predict(
        image_file,  # Send the FileData object
        api_name="/predict"
    )

        # Debugging: Print the raw result to see what we receive
    print("Raw prediction result:", result)

        # Define the class names based on your model's output
    class_names = ['YOU PROBABLY DO NOT HAVE PNEUMONIA', 'YOU MIGHT HAVE PNEUMONIA']

        # Access the predicted class (adjust index based on result structure)
    predicted_class_index = int(result[0])  # Assuming the result is a list
    predicted_class = class_names[predicted_class_index]
    
    return predicted_class
