from django.contrib import admin
from .models import Doctor, Patient, Post, Appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Post)
admin.site.register(Appointment)