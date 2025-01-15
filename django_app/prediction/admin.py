from django.contrib import admin
from .models import Prediction, Patient

admin.site.register(Prediction)

admin.site.register(Patient)
