from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

#@login_required 
def dashboard(request):
   return render(request, 'index.html')