from django.db import models

class Room(models.Model):
    #host =
    # topic =
    name = models.CharField(max_length=100)
    #the form and database for this field can have null values  
    description = models.TextField(null=True, blank=True)
    #participant
    # Auto generate the date field 
    updated = models.DateTimeField(auto_now=True)  

    #auto_now takes asnapshot everytime we save the item and 
    #auto_now_add takes a time stap when we first save or create it

    created = models.DateTimeField(auto_now_add=True)


    #When you implement the __str__ method in a class,
    # you're telling Python how to convert an instance of that class into a string
    
    #string representation of a room
    def __str__(self):
        #must be a string
        return self.name