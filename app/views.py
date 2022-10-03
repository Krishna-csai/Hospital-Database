from django.shortcuts import render
from .models import Doctor, Patient
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'homepage.html')
    
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