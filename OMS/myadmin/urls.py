from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

app_name = "myadmin"

urlpatterns = [
    path('', views.admin, name='myadmin_home'),
    path('view/', views.view_list, name="view_list"),
    path('view/orphanslist/', views.orphans_list, name="orphans_list"),
    path('employeeslist/', views.employees_list, name="employees_list"),
    path('volunteerslist/', views.volunteers_list, name="volunteers_list"),
    path('addorphan/', views.add_orphan, name="add_orphan"),
    path('addorphan/addorphrec/', views.add_orphan_record, name="add_orphan_record"),
    path('orphanslist/updateorph/updaterecord/', views.update_record, name="update_record"),
    path('orphanslist/updateorph/<str:orphanid>/', views.update_orphan, name="update_orphan"),
    path('adoptionrequest/', views.adoption_request_list, name='adoption-request-list'),
    path('adoptionrequest/updaterequest/<str:applicationid>', views.update_request_view, name='update-request-view'),
    path('adoptionrequest/updaterequest/update', views.update_request, name='update-request'),
    path('mass_email/', views.mass_email, name='mass-email'),
    path('adoptionrequest/updaterequest/update/', views.update_request, name='update-request')
]