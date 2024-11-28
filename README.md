# Pneumonia Detection System
The Pneumonia Detection System is a full-stack web application designed to diagnose pneumonia from X-ray lung imagery. It uses an AI pre-trained binary classification model, fine-tuned using PyTorch and data from [Kaggle](https://www.kaggle.com/datasets/tolgadincer/labeled-chest-xray-images), to classify lungs as pneumonic or non-pneumonic. The application uses a custom API created in Django and utilizes an SQLite database. The front end was created with Bulma CSS and Vue.js frameworks. <br><br>

## How It Works
Users can post an X-ray image of lungs, and the application will use its model to predict if the image shows healthy or potentially sick lungs. The uploaded image, prediction, and upload date are then stored in the database. The application displays the latest record from the database in an appealing way. <br><br>

## How It Looks Now
<p align="center">
  <img src="https://tarik-alaiwi-dev.github.io/resources/projects/pds.PNG" alt="Size Limit CLI" width="738">
</p>
<br><br>

## How To Run It Locally
### Steps for the first console
1. Clone this repository
```bash
git clone https://github.com/Tarik-Alaiwi-dev/x-ray_project.git
cd x-ray_project
```
2. Install the virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install necessary packages
```bash
pip install -r requirements.txt
```
4. Run Django app
```bash
cd django_app
python manage.py runserver
```
### Open the second console in `x-ray_project` directory
1. Change directory to Vue.js app
```bash
cd vue_app
```
2.  Install npm
```bash
npm install
```
3. Run Vue.js app
```bash
npm run serve
```
**You should see an URL looking like this: `http://localhost:8000/`. Paste it to your browser and see the demo of the application.**
<br><br>

## What's Next
The project is still under development. The final application should be fitted to the needs of patients, medical clinics, and radiology clinics. Things to do:
- login feature
- separate views for doctors, patients, and radiographers
- authentication feature for each type of user
- another table for doctors and radiographers or new field(s) in the 'users' table
- add tests
- improve the model and add notebook from training and data preprocessing
