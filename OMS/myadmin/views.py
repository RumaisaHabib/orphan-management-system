from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from helpers.format import format_query

# Create your views here.
def admin(request):
    utype = request.session.get('usertype')
    logged_in = request.session.get('logged_in')
    print(logged_in)
    if logged_in:
        navname = "logged_navbar.html"
    else:
        navname = "navbar.html"
        
    if utype != 'admin':
        return render(request, 'myadmin/not_admin.html', {"nav": navname})

    return render(request, 'myadmin/admin_home.html', {"nav": navname})

def orphans_list(request):
    sql = f"SELECT * FROM Users"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        orphans = format_query(cursor.fetchall(), ['email', 'password', 'usertype'])
    logged_in = request.session.get('logged_in')
    if logged_in:
        navname = "logged_navbar.html"
    else:
        navname = "navbar.html"
    return render(request, 'myadmin/orphans_list.html', {"orphans":orphans, "nav": navname}) # This will pass the orphans as a js object
    
    # Please prettify the html. 