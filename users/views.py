from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def dashboard(request):
   return render(request, 'dashboard.html')