from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.db import connection

# Create your views here.
def signup(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST["email"]
        print(email)
        pwd = request.POST["password"]
        utype = request.POST["usertype"]
        sql = fr"INSERT INTO Users (Email, Password, Usertype) VALUES('{email}', '{pwd}', '{utype}');"
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
    