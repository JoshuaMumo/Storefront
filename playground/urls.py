from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('chatbot/', views.chatbot, name='chatbot'),
]
