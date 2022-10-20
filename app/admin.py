from django.contrib import admin
from .models import AddPerson, Post, Appointment
# Register your models here.
admin.site.register(AddPerson)
admin.site.register(Post)
admin.site.register(Appointment)