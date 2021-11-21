from django.http import request
from django.shortcuts import redirect, render
from django.db import connection
from helpers.navbar import which_nav
from helpers.format import executeSQL

# Create your views here.
def feedback(request):
    return render(request, "feedback/feedback.html", {"nav": which_nav(request)})

def submit(request):
    if request.method == 'POST':
        cnic = request.POST['cnic']
        feedback = request.POST['feedback']
        email = request.POST['email']
        utype = request.POST['usertype']
        sql = fr"SELECT * FROM Feedback"
        result = executeSQL(sql, ['FeedbackID', 'CNIC', 'Email', 'Comment'])
        newid = len(result)
        sql = fr"INSERT INTO Feedback VALUES ('{newid}', '{cnic}', '{email}', '{feedback}')"
        executeSQL(sql)
        return redirect("home:index")
    else:
        return render(request, "feedback/nofeed.html", {"nav": which_nav(request)})