# models.py
from timeit import default_timer
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models
from django.core.validators import FileExtensionValidator
from cloudinary.models import CloudinaryField
import cloudinary.uploader
import logging

logger = logging.getLogger(__name__)






class Auction(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=50)
    image = models.ImageField(upload_to='auction_images/')

    def __str__(self):
        return self.name
    


class Adverts(models.Model):
    image = models.ImageField(upload_to='advert_images/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    





    
    
    
    
    
    
    
    
    
    
    


  
  
  
