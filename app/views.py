from django.shortcuts import render
from .models import Doctor, Patient, Post
from django.http import HttpResponse, JsonResponse

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