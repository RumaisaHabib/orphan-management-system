from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

app_name = "feedback"

urlpatterns = [
    path('', views.feedback, name='feedback-form'),
    path('submit/', views.submit, name='feedbakc-submit')
]