from django.db import models

class Prediction(models.Model):
    image = models.ImageField(upload_to='prediction_images')
    date = models.DateTimeField(auto_now_add=True)
    inference = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'
    
    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")
    
