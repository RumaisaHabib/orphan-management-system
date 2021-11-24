from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.db import connection
import hashlib

# Create your views here.
def signupVolunteer(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST["email"]
        print(email)
        pwd = request.POST["password"]
        hashed_pwd = str(int(hashlib.sha256(pwd.encode('utf-8')).hexdigest(), 16) % 10**8)
        utype = "volunteer"
        sql = fr"INSERT INTO Users (Email, Password, Usertype) VALUES('{email}', '{hashed_pwd}', '{utype}');"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            request.session['logged_in'] = 1
            request.session['usertype'] = utype
        return redirect('home:index')
    else:
        if request.session.get("logged_in")==1:
            print("you're already logged in")
            # another page rendered instead: to be made.
            return redirect('home:index')
        return render(request, "signup/signup.html")

def signup(request):
    return render(request, "signup/signup.html")

def signupParent(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST["email"]
        print(email)
        pwd = request.POST["password"]
        hashed_pwd = str(int(hashlib.sha256(pwd.encode('utf-8')).hexdigest(), 16) % 10**8)
        utype = "parent"
        sql = fr"INSERT INTO Users (Email, Password, Usertype) VALUES('{email}', '{hashed_pwd}', '{utype}');"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            request.session['logged_in'] = 1
            request.session['usertype'] = utype
        return redirect('home:index')
    else:
        if request.session.get("logged_in")==1:
            print("you're already logged in")
            # another page rendered instead: to be made.
            return redirect('home:index')
        return render(request, "signup/signup.html")