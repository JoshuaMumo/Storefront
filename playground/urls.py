from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('student_signin/', views.student_signin, name='student_signin'),
    path('teacher_signin/', views.teacher_signin, name='teacher_signin'),
    path('student_signup/', views.student_signup, name='student_signup'),
    path('teacher_signup/', views.teacher_signup, name='teacher_signup'),
    path('signout/', views.signout, name='signout'),
    path('rag_chatbot/', views.rag_chatbot, name='rag_chatbot'),
    path('teachers/', views.teachers_view, name='teachers'),
    path('students/', views.students_view, name='students'),
]   
