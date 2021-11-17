from django.http import request
from django.shortcuts import render
from django.db import connection
from helpers.navbar import which_nav

# Create your views here.
def feedback(request):
    return render(request, "feedback/feedback.html", {"nav": which_nav(request)})

def submit(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, "feedback/nofeed.html", {"nav": which_nav(request)})