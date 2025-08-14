from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('about_us/',about,name='about'),
    path('services/',services,name='services'),
    path('contact_us/',contact_us,name='contact_us'),
    path('gallery/',gallery,name='gallery'),
    path('booking/',booking,name='booking'),
]