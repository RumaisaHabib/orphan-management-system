from django.db import connection
from django.shortcuts import render,redirect
from django.http import HttpResponse
from helpers.format import format_query
from helpers.format import executeSQL
from helpers.navbar import which_nav

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
    orphans = executeSQL(sql, ['CNIC', 'Name', 'DateOfBirth', 'Education', 'Sex', 'Special Needs'])

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
    logged_in = request.session.get('logged_in')
    utype = request.session.get('usertype')

    if request.method == "POST" and logged_in and utype == 'admin':
        CNIC = request.POST["CNIC"]
        Name = request.POST["name"]
        SpecialNeeds = request.POST["specialneeds"]
        DateOfBirth=request.POST["DateOfBirth"]
        Education=request.POST["education"]
        Sex=request.POST["sex"]
        Hobbies=request.POST["hobbies"]
        sql = fr"INSERT INTO Orphan (CNIC, Name, SpecialNeeds, DateOfBirth, Education, Sex) VALUES('{CNIC}', '{Name}', '{SpecialNeeds}','{DateOfBirth}', '{Education}', '{Sex}');"
        print([x for x in request.POST.items()])
        try:
            executeSQL(sql)
        except:
            return render(request, 'myadmin/cnic_exists.html', {"nav": which_nav(request)})
    
    if utype != 'admin':
        return render(request, 'myadmin/not_admin.html', {"nav": which_nav(request)})
    
    return redirect('/myadmin/addorphan/', {"nav": which_nav(request)})
    
def update_orphan(request, orphanid):

    orphid = orphanid.split('=')[1]

    sql = fr"select * from Orphan where CNIC='{orphid}'"
    result = executeSQL(sql, ['CNIC', 'Name', 'DateOfBirth', 'Education', 'Sex', 'Special Needs'])
    
    print("updating this orphan:", result)
    
    logged_in = request.session.get('logged_in')
    utype = request.session.get('usertype')
    if utype != 'admin':
        return render(request, 'myadmin/not_admin.html', {"nav": which_nav(request)})

    return render(request, 'myadmin/update_orphan.html', {"result":result[0],"titles": list(result[0].keys()), "nav": which_nav(request)})
    
def update_record(request):
    logged_in = request.session.get('logged_in')
    utype = request.session.get('usertype')
    # sql("update Orphan where CNIC=id")
    if request.method == "POST":
        CNIC = request.POST["CNIC"]
        Name = request.POST["name"]
        SpecialNeeds = request.POST["specialneeds"]
        DateOfBirth=request.POST["DateOfBirth"]
        Education=request.POST["education"]
        Sex=request.POST["sex"]
        
        print([(x,k) for x,k in request.POST.items()])

        sql = fr"Update Orphan set Name='{Name}', SpecialNeeds='{SpecialNeeds}', DateOfBirth='{DateOfBirth}', Education='{Education}', Sex='{Sex}' where CNIC='{CNIC}';"
        executeSQL(sql)
    
    return redirect('/myadmin/orphanslist/')

def adoption_request_list(request):
    logged_in = request.session.get('logged_in')
    utype = request.session.get('usertype')
    if utype != 'admin':
        return render(request, 'myadmin/not_admin.html', {"nav": which_nav(request)})

    sql = fr"SELECT * FROM AdoptionRequest"
    result = executeSQL(sql, ['ApplicationID', 'OrphanCNIC', 'ParentCNIC', 'Status'])
    return render(request, 'myadmin/adoption_request_list.html', {"requests":result,"titles": list(result[0].keys()), "nav": which_nav(request)})

def update_request_view(request, applicationid):
    logged_in = request.session.get('logged_in')
    utype = request.session.get('usertype')
    if utype != 'admin':
        return render(request, 'myadmin/not_admin.html', {"nav": which_nav(request)})
    sql = fr"SELECT * FROM AdoptionRequest WHERE ApplicationID='{applicationid}'"
    result = executeSQL(sql, ['ApplicationID', 'OrphanCNIC', 'ParentCNIC', 'Status'])
    return render(request, 'myadmin/update_orphan.html', {"result":result[0],"titles": list(result[0].keys()), "nav": which_nav(request)})

    
def update_request(request):
    if request.method == 'POST':
        pass
    return redirect('/myadmin/orphanslist/')
    