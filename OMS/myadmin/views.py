from django.db import connection
from django.shortcuts import render,redirect
from django.http import HttpResponse
from helpers.format import format_query
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

    if logged_in:
        navname = "logged_navbar.html"
    else:
        navname = "navbar.html"
    
    if utype != 'admin':
        return render(request, 'myadmin/not_admin.html', {"nav": navname})

    sql = f"SELECT * FROM Orphan"
    orphans = executeSQL(sql, ['CNIC', 'Name', 'Special Needs', 'Date of Birth', 'Education', 'Sex'])

    return render(request, 'myadmin/orphans_list.html', {"orphans":orphans, "titles": list(orphans[0].keys()), "nav": navname}) # This will pass the orphans as a js object
    # Please prettify the html. 
    # # beauty lies in the heart. 
    
def add_orphan(request):
    logged_in = request.session.get('logged_in')
    utype = request.session.get('usertype')

    if logged_in:
        navname = "logged_navbar.html"
    else:
        navname = "navbar.html"
    
    if utype != 'admin':
        return render(request, 'myadmin/not_admin.html', {"nav": navname})
    
    return render(request, 'myadmin/add_orphan.html', {"nav": navname})

def add_orphan_record(request):
    if request.method == "POST":
        CNIC = request.POST["CNIC"]
        Name = request.POST["name"]
        SpecialNeeds = request.POST["specialneeds"]
        DateOfBirth=request.POST["DateOfBirth"]
        Education=request.POST["education"]
        Sex=request.POST["sex"]
        Hobbies=request.POST["hobbies"]
        sql = fr"INSERT INTO Orphan (CNIC, Name, SpecialNeeds, DateOfBirth, Education, Sex) VALUES('{CNIC}', '{Name}', '{SpecialNeeds}','{DateOfBirth}', '{Education}', '{Sex}');"
        print([x for x in request.POST.items()])
        executeSQL(sql)
    logged_in = request.session.get('logged_in')
    utype = request.session.get('usertype')

    if logged_in:
        navname = "logged_navbar.html"
    else:
        navname = "navbar.html"
    
    if utype != 'admin':
        return render(request, 'myadmin/not_admin.html', {"nav": navname})
    
    return redirect('/myadmin/addorphan/', {"nav": navname})
    
def update_orphan(request, orphanid):
    orphid = orphanid.split('=')[1]

    sql = fr"select * from Orphan where CNIC='{orphid}'"
    result = executeSQL(sql, ['CNIC', 'Name', 'SpecialNeeds', 'DateOfBirth', 'Education', 'Sex'])
    print(result)
    logged_in = request.session.get('logged_in')
    utype = request.session.get('usertype')

    if utype != 'admin' or not logged_in:
        return render(request, 'myadmin/not_admin.html', {"nav": 'navbar.html'})
    else:
        navname = "logged_navbar.html"
    
    return render(request, 'myadmin/update_orphan.html', {"result":result[0],"titles": list(result[0].keys()), "nav": navname})
    # return update form template

    # return redirect('/myadmin/orphanslist/')

def update_record(request):
    # sql("update Orphan where CNIC=id")
    if request.method == "POST":
        CNIC = request.POST["CNIC"]
        Name = request.POST["name"]
        SpecialNeeds = request.POST["specialneeds"]
        DateOfBirth=request.POST["DateOfBirth"]
        Education=request.POST["education"]
        Sex=request.POST["sex"]
        
        sql = fr"INSERT INTO Orphan (CNIC, Name, SpecialNeeds, DateOfBirth, Education, Sex) VALUES('{CNIC}', '{Name}', '{SpecialNeeds}','{DateOfBirth}', '{Education}', '{Sex}');"
        print([x for x in request.POST.items()])
        executeSQL(sql)
    
    return redirect('/myadmin/orphanlist/')
    