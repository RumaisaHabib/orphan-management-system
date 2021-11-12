from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from helpers.format import executeSQL

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
    logged_in = request.session.get('logged_in')
    utype = request.session.get('usertype')

    if utype != 'admin' and not logged_in:
        return render(request, 'myadmin/not_admin.html', {"nav": 'navbar.html'})
    else:
        navname = "logged_navbar.html"

    sql = f"SELECT * FROM Orphan"
    orphans = executeSQL(sql, ['CNIC', 'Name', 'Special Needs', 'Date of Birth', 'Education', 'Sex'])

    return render(request, 'myadmin/orphans_list.html', {"orphans":orphans, "titles": list(orphans[0].keys()), "nav": navname}) # This will pass the orphans as a js object
    
    # Please prettify the html. 