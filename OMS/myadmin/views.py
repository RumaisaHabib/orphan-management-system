from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from helpers.format import format_query

# Create your views here.
def admin(request):
    utype = request.session.get('usertype')
    logged_in = request.session.get('logged_in')

    if utype != 'admin' or not logged_in:
        return render(request, 'myadmin/not_admin.html')

    return render(request, 'myadmin/admin_home.html')

def orphans_list(request):
    sql = f"SELECT * FROM Users"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        orphans = format_query(cursor.fetchall(), ['email', 'password', 'usertype'])
    return render(request, 'myadmin/orphans_list.html', {"orphans":orphans}) # This will pass the orphans as a js object
    
    # Please prettify the html. 