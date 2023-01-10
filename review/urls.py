from django.urls import path
from .import views

urlpatterns=[
     path('',views.teacher,name='teacher'),
     path('login',views.login,name='login'),
     path('logout',views.logout,name='logout'),
     path('course',views.course,name='course'),
     path('faculty',views.faculty,name='faculty'),
     path('student',views.student,name='student')
]