from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.db import connection
from helpers.format import format_query, executeSQL
import hashlib
from helpers.navbar import which_nav

from home.views import index

# Create your views here.
def login(request):
    if request.method == "POST":
            email = request.POST["email"]
            pwd = request.POST["password"]
            hashed_pwd = str(int(hashlib.sha256(pwd.encode('utf-8')).hexdigest(), 16) % 10**8)
            utype = request.POST["usertype"]
            if utype == 'admin':
                sql = fr"SELECT * FROM Admin WHERE Email = '{email}' AND Password = '{hashed_pwd}';"
            else:
                sql = fr"SELECT * FROM Users WHERE Email = '{email}' AND Password = '{hashed_pwd}' AND Usertype = '{utype}';"
            with connection.cursor() as cursor:
                cursor.execute(sql)
                if len(cursor.fetchall()) > 0:
                    print("Successfully logged in")
                    request.session['logged_in'] = 1
                    request.session['usertype'] = utype
                    # if the user is not admin, also get their cnic from the db
                    if utype != "admin":
                        res = executeSQL(fr"select CNIC from Users where Email='{email}' and Password='{hashed_pwd}' AND Usertype = '{utype}';", ["cnic"])
                        request.session['cnic'] = res[0]['cnic']
                        cnic = request.session['cnic']
                    if utype == 'volunteer':
                        sql = fr"SELECT Status FROM Volunteers WHERE CNIC = '{cnic}'"
                        status = executeSQL(sql, ['Status'])[0]['Status']
                        if res == 'Pending' or 'Denied':
                            request.session['logged_in'] = 0
                            return render(request, 'account/volunteerfail.html', {'nav': which_nav(request), 'status':status})
                    return redirect('home:index') # This should redirect to success page or back home
            return redirect('home:index') # This branch will be for failure
    
    else:
        if request.session.get("logged_in")==1:
            print("you're already logged in")
            # another page rendered instead: to be made.
            return redirect('home:index')
        return render(request, "account/login.html")

def logout(request):
    request.session["logged_in"] = 0
    request.session["usertype"] = None
    return redirect('home:index')

def change_password(request):
    log = request.session['logged_in']
    if log == 0:
        return redirect('home:index')
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['password']
        pwd2 = request.POST['confirm password']
        utype = request.session['usertype']
        if pwd != pwd2:
            return render(request, 'account/changefail.html')
        if utype == 'admin':
            sql = fr"SELECT * FROM Admin WHERE Email = '{email}';"
            with connection.cursor() as cursor:
                cursor.execute(sql)
                if len(cursor.fetchall()) > 0:
                    hashed_pwd = str(int(hashlib.sha256(pwd.encode('utf-8')).hexdigest(), 16) % 10**8)
                    sql = fr"UPDATE Admin SET Password = '{hashed_pwd}' WHERE Email = '{email}'"
                    cursor.execute(sql)
                    return render(request, 'account/changesuccess.html')
            return render(request, 'account/changefail.html')
        else:
            sql = fr"SELECT * FROM Users WHERE Email = '{email}' AND Usertype = '{utype}';"
            with connection.cursor() as cursor:
                cursor.execute(sql)
                if len(cursor.fetchall()) > 0:
                    hashed_pwd = str(int(hashlib.sha256(pwd.encode('utf-8')).hexdigest(), 16) % 10**8)
                    sql = fr"UPDATE Users SET Password = '{hashed_pwd}' WHERE Email = '{email}' AND Usertype = '{utype}'"
                    cursor.execute(sql)
                    return render(request, 'account/changesuccess.html')
            return render(request, 'account/changefail.html')
    else:
        return render(request, 'account/changepass.html')
