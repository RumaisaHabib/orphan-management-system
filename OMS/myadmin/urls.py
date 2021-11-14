from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

app_name = "myadmin"

urlpatterns = [
    path('', views.admin, name='myadmin_home'),
    path('orphanslist/', views.orphans_list, name="orphans_list"),
    path('addorphan/', views.add_orphan, name="add_orphan"),
    path('addorphan/addorphrec/', views.add_orphan_record, name="add_orphan_record"),
    path('orphanslist/updateorph/<str:orphanid>/', views.update_orphan, name="update_orphan"),
]