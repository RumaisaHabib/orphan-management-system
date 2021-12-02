from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'department'

urlpatterns = [
    path('', views.department_list, name='department_list'),
]