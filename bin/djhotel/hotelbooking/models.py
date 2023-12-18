from django.db import models
from PIL import Image

# Create your models here.

class HotelImage(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')