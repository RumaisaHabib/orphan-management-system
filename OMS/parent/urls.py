from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

app_name = "parent"

urlpatterns = [
    path('vieworph/', views.viewOrphans, name='myadmin_home'),
    path('vieworph/adoptorphan/<str:orphanid>/', views.adoptOrphan, name="adoptOrphan"),
]