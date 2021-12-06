from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

app_name = "myadmin"

urlpatterns = [
    path('', views.admin, name='myadmin_home'),
    path('view/', views.view_list, name="view_list"),
    path('view/orphanslist/', views.orphans_list, name="orphans_list"),
    path('view/employeeslist/', views.employees_list, name="employees_list"),
    path('view/volunteerslist/', views.volunteers_list, name="volunteers_list"),
    path('addorphan/', views.add_orphan, name="add_orphan"),
    path('addorphan/addorphrec/', views.add_orphan_record, name="add_orphan_record"),

    path('view/volunteerslist/updatevol/updaterecord/', views.update_record_v, name="update_record_v"),
    path('view/volunteerslist/updatevol/approvevol/', views.approve_volunteer, name='approve_vounteer'),
    path('view/volunteerslist/updatevol/<str:volunteerid>/', views.update_volunteer, name="update_volunteer"),

    path('view/employeeslist/updateemp/updaterecord/', views.update_record_e, name="update_record_e"),
    path('view/employeeslist/updateemp/<str:employeeid>/', views.update_employee, name="update_employee"),

    path('view/orphanslist/updateorph/updaterecord/', views.update_record_o, name="update_record_o"),
    path('view/orphanslist/updateorph/<str:orphanid>/', views.update_orphan, name="update_orphan"),

    path('adoptionrequest/', views.adoption_request_list, name='adoption-request-list'),
    path('adoptionrequest/updaterequest/<str:applicationid>', views.update_request_view, name='update-request-view'),
    path('adoptionrequest/updaterequest/update/', views.update_request, name='update-request'),
    path('mass_email/', views.mass_email, name='mass-email'),

    path('appointmentrequest/', views.appointment_list, name="appointmentspage"),
    path('appointmentrequest/updateappointment/<str:appointmentid>', views.update_appointment_view, name="appointmentsupdatepage"),
    path('appointmentrequest/updateappointment/update/', views.update_appointment, name='update-request'),
    path('addemployee/', views.add_employee, name="add_employee"),
]