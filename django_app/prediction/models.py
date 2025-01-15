from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

User = get_user_model()

class Prediction(models.Model):
    image = models.ImageField(upload_to='prediction_images')
    date = models.DateTimeField(auto_now_add=True)
    inference = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="predictions")

    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'
    
    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")

class Patient(AbstractUser):  
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    predictions = models.ManyToManyField(Prediction, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="patient_users",  # 🔹 Nowa nazwa dla relacji `groups`
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="patient_permissions",  # 🔹 Nowa nazwa dla relacji `user_permissions`
        blank=True
    )

    def __str__(self):
        return self.username
    
    
    
    
