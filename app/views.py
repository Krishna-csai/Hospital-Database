from time import strftime
from django.shortcuts import render
from .models import Doctor, Patient, Post, Appointment
from django.http import HttpResponse, JsonResponse
import datetime

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html' , { 'posts': posts })

def mentalhealth(request):
    posts = Post.objects.filter(category ='1')
    return render(request, 'blogs.html' , { 'posts': posts })

def heartdieseases(request):
    posts = Post.objects.filter(category ='2')
    return render(request, 'blogs.html' , { 'posts': posts })

def covid19(request):
    posts = Post.objects.filter(category ='3')
    return render(request, 'blogs.html' , { 'posts': posts })

def immunization(request):
    posts = Post.objects.filter(category = '4')
    return render(request, 'blogs.html' , { 'posts': posts })

def calender(request):
    results = test_calendar()
    context = {"results": results}
    return render(request, 'calender.html', context)

def createappointment(request, name ):
    doctor = Doctor.objects.get(username=name)
    if request.method == 'POST':
        if request.POST.get('speciality') and request.POST.get('date') and request.POST.get('time'):
            post=Appointment()
            post.speciality= request.POST.get('speciality')
            post.date= request.POST.get('date')
            post.time= request.POST.get('time')
            time = request.POST.get('time')
            endtime = datetime.datetime.strptime(time, "%H:%M") + datetime.timedelta(minutes=45)
            endtime1 = endtime.strftime("%H:%M")
            post.endtime = endtime1
            post.doctor= name
            post.save()
            
            return render(request, 'appointmentdone.html', {"doctor": doctor , "post": post})  
    else:
        return render(request,'form.html')

def appointment(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointment.html', {'doctors': doctors})

def viewblog(request, title):
    posts = Post.objects.get(title=title)
    return render(request, 'detail.html', {'posts': posts})
    
def doctor(request):
        if request.method == 'POST':
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirmpassword')
            if password == confirmpassword :
                post=Doctor()
                post.firstname = request.POST.get('firstname')
                post.lastname = request.POST.get('lastname')
                post.username = request.POST.get('username')
                post.email = request.POST.get('email')
                post.password = request.POST.get('password')
                post.address = request.POST.get('address')
                post.save()
                
                result = 'Name - '+post.firstname+' '+post.lastname+' Username - '+post.username+' Email - '+post.email+' Address - '+post.address

                return HttpResponse(result)

            else :
                return render(request, 'wrongpassword.html')
            
        else:
                return render(request,'doctor.html')
            
def patient(request):
        if request.method == 'POST':
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirmpassword')
            if password == confirmpassword :
                post=Patient()
                post.firstname = request.POST.get('firstname')
                post.lastname = request.POST.get('lastname')
                post.username = request.POST.get('username')
                post.email = request.POST.get('email')
                post.password = request.POST.get('password')
                post.address = request.POST.get('address')
                post.save()
                result = 'Name - '+post.firstname+' '+post.lastname+' Username - '+post.username+' Email - '+post.email+' Address - '+post.address

                return HttpResponse(result) 

            else :
                return render(request, 'wrongpassword.html')
            
        else:
                return render(request,'patient.html')