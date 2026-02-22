from django.db import models

# Create your models here.

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')  # zdjęcia trafią do media/photos/
    uploaded_at = models.DateTimeField(auto_now_add=True)