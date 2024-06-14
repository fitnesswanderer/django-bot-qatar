"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include(('chatbot_project.urls2','chatbot_project'),namespace = 'chatbot_project')),
    path('home/', include(('chatbot_project.urls2','chatbot_project'),namespace = 'chatbot_project2')),
    
]
