import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
from io import BytesIO

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
def predict(image_file, model_path):
    model = load_model(model_path)
    image = preprocess_image(image_file)

    with torch.no_grad():
        image = image.to(next(model.parameters()).device)

        outputs = model(image)
        _, predicted = torch.max(outputs, 1)

    class_names = ['NO PNEUMONIA DETECTED', 'PNEUMONIA DETECTED']
    predicted_class = class_names[predicted.item()]

    print(f"Predicted class: {predicted_class}")
    return predicted_class
