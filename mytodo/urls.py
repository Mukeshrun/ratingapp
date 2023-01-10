from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo_list/', views.todo_list, name='todo_list'),
    path('todo_create/', views.todo_create, name='todo_create')
]