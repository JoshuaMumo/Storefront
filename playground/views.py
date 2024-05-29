from django.shortcuts import render
from django.http import JsonResponse, HttpRequest

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def registration(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')

def chatbot(request):
    return render(request, 'chatbot.html')

