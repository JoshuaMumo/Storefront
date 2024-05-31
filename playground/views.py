from django.shortcuts import render
from django.http import JsonResponse, HttpRequest

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def signout(request):
    return render(request, 'signout.html')

def chatbot(request):
    return render(request, 'chatbot.html')

