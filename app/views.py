from time import strftime
from unicodedata import category
from django.shortcuts import render
from .models import AddPerson, Post, Appointment
from django.http import HttpResponse, JsonResponse
import datetime
from django.contrib.auth import login, authenticate

currentuser = 'none'

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

def createappointment(request, name ):
    addperson = AddPerson.objects.get(username=name)
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
    doctors = AddPerson.objects.all()
    return render(request, 'appointment.html', {'doctors': doctors})

def viewblog(request, title):
    posts = Post.objects.get(title=title)
    return render(request, 'detail.html', {'posts': posts})
    
def addperson(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password == confirmpassword :
            post=AddPerson()
            post.firstname = request.POST.get('firstname')
            post.lastname = request.POST.get('lastname')
            post.username = request.POST.get('username')
            post.email = request.POST.get('email')
            post.category = request.POST.get('category').lower()
            post.password = request.POST.get('password')
            post.addressline1 = request.POST.get('addressline1')
            post.city = request.POST.get('city')
            post.state = request.POST.get('state')
            post.pincode = request.POST.get('pincode')
            if (post.category == "doctor" or post.category == "patient"):
                post.save()
                username1 = request.POST.get("username")
                currentuser = AddPerson.objects.get(username = username1)
                return HttpResponse("Account Created Successfully "+ post.category + " " + post.username)
            else:
                return HttpResponse("Please Enter a Correct Category...");
            
        else :
            return render(request, 'wrongpassword.html')
        
    else:
            return render(request,'addperson.html')
            
def login(request):
    if request.method == 'POST':
        username1 = request.POST.get("username")
        password1 = request.POST.get("password")
        try:
            users = AddPerson.objects.get(username = username1)
            currentuser = AddPerson.objects.get(username = username1)
            password = users.password
            category = users.category
            if password == password1:
                if category == "doctor":
                    return HttpResponse("Hello Doctor " + username1)
                else:
                    return HttpResponse("Hello Patient "+ username1)
            
            else:
                return HttpResponse("Wrong Password")
        except:
            return HttpResponse("No User Found, Create A New Account")
        
    
    else:
        return render(request,'login.html')
