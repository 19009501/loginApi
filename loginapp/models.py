# from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
class User(models.Model):
    name=models.CharField(max_length=35)
    
