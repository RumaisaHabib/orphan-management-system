from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.db import connection
from helpers.format import format_query 

from home.views import index

# Create your views here.
def login(request):
    if request.method == "POST":
            email = request.POST["email"]
            pwd = request.POST["password"]
            utype = request.POST["usertype"]
            sql = fr"SELECT * FROM Users WHERE Email = '{email}' AND Password = '{pwd}' AND Usertype = '{utype}';"
            with connection.cursor() as cursor:
                cursor.execute(sql)
                if len(cursor.fetchall()) > 0:
                    print("Successfully logged in")
                    request.session['logged_in'] = 1
                    request.session['usertype'] = utype
                    return redirect('myadmin:myadmin_home')
            return redirect('home:index')

            # Redirect command redirects the page to specified url. helps stop that error of needing to reload page when
            # you submit something. For log in need to make two kinds of redirects. if successful redirect to success
            # page. If unsuccessful redirect to failure page.
            
    
    else:
        if request.session.get("logged_in")==1:
            print("you're already logged in")
            # another page rendered instead: to be made.
            return render(request, "account/login.html")
        return render(request, "account/login.html")

def logout(request):
    request.session["logged_in"] = 0
    request.session["usertype"] = None
    return redirect('home:index')
