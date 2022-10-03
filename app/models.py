from django.db import models

# Create your models here.
class Doctor(models.Model):
    firstname = models.CharField(max_length = 15)
    lastname = models.CharField(max_length = 15)
    username = models.CharField(max_length = 25)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 50)
    address = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.username
    

class Patient(models.Model):
    firstname = models.CharField(max_length = 15)
    lastname = models.CharField(max_length = 15)
    username = models.CharField(max_length = 25)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 50)
    address = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.username