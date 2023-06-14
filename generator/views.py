from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    char=list("abcdefghijklmnopqrstuvwxyz")
    length=int(request.GET.get("length"))
    if request.GET.get('uppercase'):
        char.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if request.GET.get('special'):
        char.extend("!@#$%^&*()-_+={}[]\|?/`~")
    if request.GET.get('numbers'):
        char.extend("123456789")
    temp_pass=""
    for i in range(length):
        temp_pass+=random.choice(char)
    return render(request, 'generator/password.html', {'password':temp_pass})

def about(request):
    return render(request, 'generator/about.html')