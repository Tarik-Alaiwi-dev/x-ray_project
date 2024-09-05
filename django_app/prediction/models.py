from django.db import models

class Prediction(models.Model):
    image = models.ImageField(upload_to='prediction_images')
    date = models.DateTimeField(auto_now_add=True)
    inference = models.CharField(max_length=100)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.date
    
