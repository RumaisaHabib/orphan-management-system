from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.db import connection
from helpers.format import executeSQL
import hashlib

# Create your views here.
def signupVolunteer(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST["email"]
        print(email)
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
        
        hashed_pwd = str(int(hashlib.sha256(pwd.encode('utf-8')).hexdigest(), 16) % 10**8)
        
        usertype = "volunteer"
        try:
            # add this parent
            sql = fr"insert into Volunteers values('{cnic}', '{dd}', '{name}', '{age}', '{sex}', '{joindate}', '{contractenddate}', {phone}, '{email}','{organization}' )"
            executeSQL(sql)

            # now add this user
            sql = fr"insert into Users values('{cnic}', '{email}', '{hashed_pwd}', '{usertype}')"
            executeSQL(sql)
            
        except Exception as e:
            print('ERROR SIGNING UP', e)
            return render(request, '/signuperror.html')
 
    if request.session.get("logged_in")==1:
        print("you're already logged in")
        # another page rendered instead: to be made.
        return redirect('home:index') 
    return render(request, "signup/signup.html")



def signup(request):
    departments = executeSQL("select DeptID, DeptName from Department", ["id", "name"])
    print(departments)
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

        try:
            # add this parent
            sql = fr"insert into ApplicantParent values('{cnic}', '{name}', '{dob}', '{maritalStat}', '{profession}', {earning}, {children}, '{address}', {phone})"
            executeSQL(sql)

            # now add this user
            sql = fr"insert into Users values('{cnic}', '{email}', '{hashed_pwd}', '{usertype}')"
            executeSQL(sql)
        except Exception as e:
            print('ERROR SIGNING UP', e)
            return render(request, '/signuperror.html')

        return redirect('/')

    if request.session.get("logged_in")==1:
            print("you're already logged in")
            # another page rendered instead: to be made.
            return redirect('home:index')
    return render(request, "signup/successfulsignup.html")


