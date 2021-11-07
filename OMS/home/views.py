from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

# Create your views here.
def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Temporary")
        print(cursor.fetchall())
    return render(request, "home/index.html")