from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.db import connection
from helpers.format import executeSQL
from helpers.navbar import which_nav

# Create your views here.
def viewOrphans(request):
	utype = request.session.get('usertype')
	if utype != 'parent':
	    return render(request, 'parent/not_parent.html', {"nav": which_nav(request)})

	sql = f"SELECT * FROM Orphan"
	orphans = executeSQL(sql, ['CNIC', 'Name', 'DateOfBirth', 'Education', 'Sex', 'Special Needs'])

	return render(request, 'parent/orphanslist.html', {"orphans":orphans, "titles": list(orphans[0].keys()), "nav": which_nav(request)})


def adoptOrphan(request, orphanid):
	orphid = orphanid.split('=')[1]

	utype = request.session.get('usertype')
	if utype != 'parent':
	    return render(request, 'parent/not_parent.html', {"nav": which_nav(request)})
    
	sql = fr"insert into AdoptionRequest (OrphanCNIC, ParentCNIC, Status) values('{orphid}',  '{request.session.get('cnic')}', 'Pending');"
	executeSQL(sql)

	return render(request, 'parent/adoptionreqsubmitted.html', {"nav": which_nav(request)})
	

