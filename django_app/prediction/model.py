import torch
import torch.nn as nn
from torchvision import transforms
import torch.nn.functional as F
from PIL import Image
import os
import io

class PneumoniaCNN(nn.Module):
    def __init__(self):
        super(PneumoniaCNN, self).__init__()
        # Change conv1 to match the saved model's architecture
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3)  
        self.conv2 = nn.Conv2d(64, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(128 * 18 * 18, 512)
        self.fc2 = nn.Linear(512, 1)
        self.pool = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 128 * 18 * 18)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = torch.sigmoid(self.fc2(x))
        return x

# Define the function to load the model
def load_model(model_path):
    model = PneumoniaCNN()
    state_dict = torch.load(model_path, map_location=torch.device('cpu'))
    model.load_state_dict(state_dict, strict=False)
    model.eval()
    return model

# Define the transformation for input images
def preprocess_image(image_file):
    image = Image.open(io.BytesIO(image_file.read())).convert('RGB')
    
    transform = transforms.Compose([
        transforms.Resize((150, 150)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)  # Add a batch dimension

# Define the function to make predictions
def predict(model, image_path):
    image = Image.open(image_path).convert('L')
    image_tensor = preprocess_image(image)
    with torch.no_grad():
        output = model(image_tensor)
        prediction = torch.sigmoid(output)
        predicted_class = int(torch.round(prediction).item())
    return predicted_class
