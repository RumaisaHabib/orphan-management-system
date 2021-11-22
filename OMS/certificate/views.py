from django.shortcuts import render

from django.db import connection
from django.shortcuts import render,redirect
from django.http import HttpResponse
from helpers.format import format_query
from helpers.format import executeSQL
from helpers.navbar import which_nav
from helpers.email import send_email

# Libraries needed for file handling 
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.


def download(request):
    #create bytestream buffer
    buf = io.BytesIO()
    #create canvas
    c = canvas.Canvas(buf, pagesize= letter, bottomup=0)
    # create text object
    text_ob = c.beginText()
    text_ob.setTextOrigin(inch, inch)
    text_ob.setFont("Helvetica", 14)
    
 
    # remove this after database is ready
    # sql = fr"INSERT INTO Volunteers (CNIC, DeptID, Name, Age, Sex, JoinDate, ContractEndDate, Phone, Email, Organization) VALUES('3342843729394', '1', 'Alina','17', 'Female', '666666', '999999', '57657657', 'me@ffdg', 'PSRD');"
    # executeSQL(sql, ['CNIC', 'DeptID', 'Name', 'Age', 'Sex', 'JoinDate', 'ContractEndDate', 'Phone', 'Email', 'Organization'])
    # remove til here

    sql = f"SELECT * FROM Volunteers WHERE CNIC='6969696969695'"
    volunteer = executeSQL(sql, ['CNIC', 'DeptID', 'Name', 'Age', 'Sex', 'JoinDate', 'ContractEndDate', 'Phone', 'Email', 'Organization'])
    print(volunteer)
    # text in the certifcate  
    lines = [
        "To whom it may concern.",
        " ",
        "This is to certify that <insert volunteer name here> has volunteered",
        "at our Orphanage since <insert joindate here> till <insert contractenddate>", 
        "This certificate appreciates the exemplary work done by the volunteer in", 
        "bringing happiness and joy in children's lives.",
        " ",
        "Regards,",
        "Happy Hearts Orphanage",
        " "
        " ",        
        "This is a computer-generated report and does not need a signature.",
    ]
        
    for line in lines:
        text_ob.textLine(line)
    
    c.drawText(text_ob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    return FileResponse(buf, as_attachment= True, filename= 'Certificate.pdf')