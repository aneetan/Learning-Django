from django.db import models
from django.contrib.auth.models import AbstractUser


#user model having all original functionality of a user model
class User(AbstractUser):
    name = models.CharField(max_length=100, null = True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)
    
    #setting the username field of django as email
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS= []


