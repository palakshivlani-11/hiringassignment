from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.

def getimg(request):
    img = Image.objects.get()
    print(img.created_on)
    print(img.updated_on)
    print(img.kid.parentemail)
    return HttpResponse("<h1>Hello</h1>")