from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def admin(request):
    utype = request.session.get('usertype')
    logged_in = request.session.get('logged_in')

    if utype != 'admin' or not logged_in:
        return render(request, 'myadmin/not_admin.html')

    return render(request, 'myadmin/admin_home.html')