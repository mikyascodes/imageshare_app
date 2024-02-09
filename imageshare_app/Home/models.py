from django.db import models
from django.utils import timezone
from datetime import datetime 
from PIL import Image
from user.models import Memeber
# Create your models here.

class Imagepage (models.Model):
    img = models.ImageField(upload_to="uploads/", default="default.jpg")                       
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    post_date = models.DateTimeField(default= datetime.now)
    user_name = models.CharField(max_length=20)






