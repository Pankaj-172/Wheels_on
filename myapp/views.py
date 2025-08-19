from django.shortcuts import render, redirect 
from django.contrib.auth.models import User    
from django.contrib.auth import authenticate, login   
from django.contrib import messages  


# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email= request.POST.get('email')
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect('/')  

    return render(request,'idex.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact_us(request):
    return render(request,'contact_us.html')

def gallery(request):
    return render(request,'gallery.html')

def booking(request):
    return render(request,'booking.html')



def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)   
            return redirect("/")   

    return render(request, "signup.html")   

