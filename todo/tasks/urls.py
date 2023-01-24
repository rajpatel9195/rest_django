from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('task/', taskAPI.as_view()), 
    path('taskall/',views.taskall)   
]