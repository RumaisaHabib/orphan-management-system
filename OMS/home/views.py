from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request.session)
    print(request.session.get("usertype"))
    print(request.session.get("logged_in"))
    if request.session.get("logged_in"):
        return render(request, "home/logged_index.html")
    return render(request, "home/index.html")