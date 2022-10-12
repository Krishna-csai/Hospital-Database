from django.db import models
from datetime import timedelta

# Create your models here.
class Doctor(models.Model):
    firstname = models.CharField(max_length = 15)
    profile = models.ImageField(default='default.jpg')
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
    
class Post(models.Model):
    class choices(models.TextChoices):
        MentalHealth = "1", "Mental Health"
        HeartDiseases = "2", "Heart Diseases"
        Covid19 = "3", "Covid19"
        Immunization = "4", "Immunization"
        
    title = models.CharField(max_length = 200)
    image = models.ImageField()
    category = models.CharField(
        max_length = 20,
        choices=choices.choices,
        default=choices.MentalHealth
    )
    summary = models.TextField()
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']
        
    def __str__(self):
        return self.title    

class Appointment(models.Model):
    doctor = models.TextField(max_length=50)
    speciality = models.TextField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    endtime = models.TextField()