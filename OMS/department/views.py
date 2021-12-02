from django.shortcuts import render
from django.db import connection
from django.shortcuts import render,redirect
from django.http import HttpResponse
from helpers.format import format_query
from helpers.format import executeSQL
from helpers.navbar import which_nav
from helpers.email import send_email

# Create your views here.
def department_list(request):
    logged_in = request.session.get('logged_in')
    utype = request.session.get('usertype')

    if logged_in:
        navname = "logged_navbar.html"
    else:
        navname = "navbar.html"
    
    sql = f"SELECT * FROM Department"
    departments = executeSQL(sql, ['DeptID', 'DeptName', 'NumberOfEmployees', 'Budget', 'Location'])

    return render(request, 'department/department_list.html', {"departments":departments, "titles": list(departments[0].keys()), "nav": navname})