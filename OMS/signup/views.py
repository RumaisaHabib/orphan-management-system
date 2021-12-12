from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.db import connection
from helpers.format import executeSQL
import hashlib
from helpers.user import exists
from helpers.navbar import which_nav

# Create your views here.
def signupVolunteer(request):
    if request.method == "POST":
        email = request.POST["email"]
        pwd = request.POST["password"]
        cnic = str(request.POST["CNIC"])
        age=request.POST["age"]
        sex=request.POST["sex"]
        organization=request.POST["organization"]
        phone= request.POST["phone"]
        contractenddate=request.POST["contractenddate"]
        joindate=request.POST["joindate"]
        dd=request.POST["deptid"]
        name = request.POST["name"]
        status = 'Pending'
        
        hashed_pwd = str(int(hashlib.sha256(pwd.encode('utf-8')).hexdigest(), 16) % 10**8)
        
        usertype = "volunteer"
        if exists(email, usertype):
            return render(request, 'signup/signuperror.html', {'nav':which_nav(request)})
        try:
            # add this parent
            sql = fr"insert into Volunteers values('{cnic}', '{dd}', '{name}', '{age}', '{sex}', '{joindate}', '{contractenddate}', {phone}, '{organization}', '{status}')"
            executeSQL(sql)

            # now add this user
            sql = fr"insert into Users values('{cnic}', '{email}', '{hashed_pwd}', '{usertype}')"
            executeSQL(sql)
            
        except Exception as e:
            print('ERROR SIGNING UP', e)
            return render(request, 'signup/signuperror.html', {'nav':which_nav(request)})
 
    if request.session.get("logged_in")==1:
        print("you're already logged in")
        # another page rendered instead: to be made.
        return redirect('home:index') 
    return render(request, "signup/successfulsignup.html")



def signup(request):
    departments = executeSQL("select DeptID, DeptName from Department", ["id", "name"])
    return render(request, "signup/signup.html", {"dept": departments})

def signupParent(request):
    if request.method == "POST":
        cnic = request.POST["CNIC"]
        name = request.POST["name"]
        email = request.POST["email"]
        pwd = request.POST["password"]
        hashed_pwd = str(int(hashlib.sha256(pwd.encode('utf-8')).hexdigest(), 16) % 10**8)
        dob = request.POST["dateofbirth"]
        maritalStat = request.POST["maritalstatus"]
        profession = request.POST["profession"]
        earning = request.POST["monthlyearning"]
        children = request.POST["noofpreviouschildren"]
        address = request.POST["address"]
        phone = request.POST["phone"]
        usertype = "parent"

        if exists(email, usertype):
            return render(request, 'signup/signuperror.html', {'nav':which_nav(request)})

        try:
            # add this parent
            sql = fr"insert into ApplicantParent values('{cnic}', '{name}', '{dob}', '{maritalStat}', '{profession}', {earning}, {children}, '{address}', {phone})"
            executeSQL(sql)

            # now add this user
            sql = fr"insert into Users values('{cnic}', '{email}', '{hashed_pwd}', '{usertype}')"
            executeSQL(sql)
        except Exception as e:
            print('ERROR SIGNING UP', e)
            return render(request, 'signup/signuperror.html', {'nav':which_nav(request)})

    if request.session.get("logged_in")==1:
            print("you're already logged in")
            # another page rendered instead: to be made.
            return redirect('home:index')
    return render(request, "signup/successfulsignup.html")


