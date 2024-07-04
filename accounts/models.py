from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    #will affect what is in the fields in the form.py
    
    age = models.PositiveBigIntegerField(null=True,blank=True)