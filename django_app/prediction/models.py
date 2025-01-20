from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Prediction(models.Model):
    image = models.ImageField(upload_to='prediction_images')
    date = models.DateTimeField(auto_now_add=True)
    inference = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_predictions"  # Unique name to avoid conflict
    )

    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'

    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")


class Patient(AbstractUser):  
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    
    # Remove the ManyToManyField if it's redundant, OR provide a different name
    predictions = models.ManyToManyField(
        Prediction,
        blank=True,
        related_name="related_patients"  # Unique name for this relationship
    )

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="patient_users",  # Unique name for groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="patient_permissions",  # Unique name for permissions
        blank=True
    )

    def __str__(self):
        return self.username
