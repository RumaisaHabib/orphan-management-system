from django.http.response import HttpResponse
from helpers.navbar import which_nav
from helpers.format import executeSQL
from django.shortcuts import render
from datetime import date

# Create your views here.
def donation_page(request):
    return render(request, 'donation/donation_info.html', {'nav': which_nav(request)})

def donated(request):
    transid = request.POST['Transaction ID']
    amount = request.POST['Amount']
    date1= date.today()
    sql = fr"INSERT INTO Donation VALUES ('{transid}', '{amount}','{date1}')"
    executeSQL(sql)
    return render(request, 'donation/thanku.html', {'nav': which_nav(request)})