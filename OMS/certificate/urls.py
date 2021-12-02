from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'certificate'

urlpatterns = [
    path('', views.certificate),
    path('download/', views.download),
    
]