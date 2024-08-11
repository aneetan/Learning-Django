from django.db import models
from django.contrib.auth.models import AbstractUser

#-----------------user model ----------------------------------
class User(AbstractUser):
    name = models.CharField(max_length=100, null = True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null = True, default="3.jpg")
    
    #setting the username field of django as email
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS= []



class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=100)
    #the form and database for this field can have null values  
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank= True)  #related name as the user is used already
    # Auto generate the date field 
    updated = models.DateTimeField(auto_now=True)  

    #auto_now takes asnapshot everytime we save the item and 
    #auto_now_add takes a time stap when we first save or create it

    created = models.DateTimeField(auto_now_add=True)


    #When you implement the __str__ method in a class,
    # you're telling Python how to convert an instance of that class into a string

    # order the data (- for inverse) based on new create
    class Meta:
        ordering = ['-updated', '-created']
    #string representation of a room
    def __str__(self): 
        #must be a string
        return self.name
    


    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        #to return the first 50 characters
        return self.body[0:50]
    




    

