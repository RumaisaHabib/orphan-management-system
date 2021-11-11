from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse

# Create your views here.
def index(request):
    logged_in = request.session.get('logged_in')
    if logged_in:
        navname = "logged_navbar.html"
    else:
        navname = "navbar.html"
    return render(request, "home/index.html", {"nav": navname})