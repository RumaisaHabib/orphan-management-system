from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

app_name = "myadmin"

urlpatterns = [
    path('', views.admin, name='myadmin_home'),
    path('orphanslist/', views.orphans_list, name="orphans_list"),
    path('addorphan/', views.add_orphan, name="add_orphan"),
    path('addorphan/addorphrec/', views.add_orphan_record, name="add_orphan_record"),
    path('orphanslist/updateorph/updaterecord/', views.update_record, name="update_record"),
    path('orphanslist/updateorph/<str:orphanid>/', views.update_orphan, name="update_orphan"),
    path('adoptionrequest/', views.adoption_request_list, name='adoption-request-list'),
    path('adoptionrequest/updaterequest/<str:applicationid>', views.update_request_view, name='update-request-view'),
    path('adoptionrequest/updaterequest/update/', views.update_request, name='update-request')
]