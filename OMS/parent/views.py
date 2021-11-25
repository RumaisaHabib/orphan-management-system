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
	print(orphans)
	return render(request, 'parent/orphanslist.html', {"orphans":orphans, "titles": list(orphans[0].keys()), "nav": which_nav(request)})

def applyFilter(request):
	if request.method == "POST":
		utype = request.session.get('usertype')
		if utype != 'parent':
		    return render(request, 'parent/not_parent.html', {"nav": which_nav(request)})

		sql = f"select * from Orphan where 1"
		for x,y in request.POST.items():
			if y == "":
				continue
			if x in ["Name", "Sex", "Education"]:
				sql += f" and {x} like '%{y}%' "
			elif x == "DateOfBirth":
				sql += f" and {x} > '{y}' "

		print(sql)
		orphans = executeSQL(sql, ['CNIC', 'Name', 'DateOfBirth', 'Education', 'Sex', 'Special Needs'])
		if len(orphans) > 0:
			return render(request, 'parent/tableForFilters.html', {"orphans":orphans, "titles": list(orphans[0].keys()), "nav": which_nav(request)})
		else:
			return HttpResponse("")
	else:
		return viewOrphans(request)

def adoptOrphan(request, orphanid):
	orphid = orphanid.split('=')[1]

	utype = request.session.get('usertype')
	if utype != 'parent':
	    return render(request, 'parent/not_parent.html', {"nav": which_nav(request)})
    
	sql = fr"insert into AdoptionRequest (OrphanCNIC, ParentCNIC, Status) values('{orphid}',  '{request.session.get('cnic')}', 'Pending');"
	executeSQL(sql)

	return render(request, 'parent/adoptionreqsubmitted.html', {"nav": which_nav(request)})
	
def getAppointment(request):
	utype = request.session.get('usertype')
	if utype != 'parent':
	    return render(request, 'parent/not_parent.html', {"nav": which_nav(request)})

	admins = executeSQL("select CNIC, Name from Admin", ['cnic', 'name'])

	return render(request, 'parent/getAppointment.html', {"nav": which_nav(request), "admins":admins})

def bookAppointment(request):
	utype = request.session.get('usertype')
	if utype != 'parent':
	    return render(request, 'parent/not_parent.html', {"nav": which_nav(request)})

	print([x for x in request.POST.items()])
	adminCnic = request.POST["admin"]
	time = request.POST["appointment"]
	parentcnic = request.session.get("cnic")

	executeSQL(fr"insert into Appointment (ParentCNIC, AdminCNIC, AppointmentTime) values('{parentcnic}', '{adminCnic}', '{time}')")

	return redirect("/")