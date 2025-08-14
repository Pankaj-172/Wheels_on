from django.shortcuts import render

# Create your views here.

def index(request):
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

