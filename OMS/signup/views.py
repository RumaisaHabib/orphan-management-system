from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.db import connection

# Create your views here.
def signup(request):
    if request.method == "POST":
        print(request.POST)
        email = request.POST["email"]
        print(email)
        pwd = request.POST["password"]
        sql = fr"INSERT INTO Users ('Email', 'Password') VALUES ('{email}', '{pwd}');"
        with connection.cursor() as cursor:
            cursor.execute(sql)
        return render(request, "signup/signup.html")
    return render(request, "signup/signup.html")
    