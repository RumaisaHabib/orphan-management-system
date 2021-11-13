from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('changepass/', views.change_password, name='changepass')
]
