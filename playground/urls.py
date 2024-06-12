from django.urls import path
from . import views
from . import student_views, teacher_views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path("logout/", views.logoutUser, name="logout"),
    path('about/', views.about, name='about'),
    path('student_signin/', student_views.student_signin, name='student_signin'),
    path('teacher_signin/', teacher_views.teacher_signin, name='teacher_signin'),
    path('student_signup/', student_views.student_signup, name='student_signup'),
    path('teacher_signup/', teacher_views.teacher_signup, name='teacher_signup'),
    path('signout/', views.signout, name='signout'),  
    path('rag_chatbot/', views.rag_chatbot, name='rag_chatbot'),
    path('teachers/', views.teachers_view, name='teachers'),
    path('students/', views.students_view, name='students'),
    
]
