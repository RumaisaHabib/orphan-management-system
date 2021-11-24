from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'donation'

urlpatterns = [
    path('', views.donation_page, name='donation-page'),
    path('donated/', views.donated, name='donated')
]