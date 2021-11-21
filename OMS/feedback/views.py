from django.http import request
from django.shortcuts import redirect, render
from django.db import connection
from helpers.navbar import which_nav

# Create your views here.
def feedback(request):
    return render(request, "feedback/feedback.html", {"nav": which_nav(request)})

def submit(request):
    if request.method == 'POST':
        name = request.POST["name"]
        feedback = request.POST['feedback']
        utype = request.POST['usertype']
        print(name)
        print(feedback)
        #insert into databse once the table is made 
        return redirect("home:index")
    else:
        return render(request, "feedback/nofeed.html", {"nav": which_nav(request)})