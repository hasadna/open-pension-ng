from django.shortcuts import render
from importer import models
from django.http import HttpResponse

root="/"
# Create your views here.
def companies(request):
    output = "רשימת החברות:<br><select size= 4 onchange='window.location.replace(\"/\"+this.options[this.selectedIndex].innerHTML)'>"
    company_list = models.Kupot.objects.values().distinct()
    for k in company_list:
        output = output+"<option value="+str(k["id"])+">"+k["company"]+"</option>"
    output = output+"</select>"
    return HttpResponse(output)

def kupot(request, company_name):
    output = "רשימת מסלולים ל"+company_name+":<br><select size = 10 \
        onchange=window.location.replace(\"/\duchot/\"+this.options[this.selectedIndex].value+\"/\"+this.options[this.selectedIndex].innerHTML)>"
    company_list = models.Kupot.objects.values().filter(company=company_name)
    for k in company_list:
        output = output+"<option value="+str(k["id"])+">"+k["track"]+"</option>"
    output = output+"</select><br><button onclick='window.location.replace(\"/\")'>back</button>"
    return HttpResponse(output)

def duchot(request, kupa_id, kupa):
    output = "רשימת דוח\"ות ל"+str(kupa)+":<br><select size = 10 onchange='window.location.replace(\"/tabs/\"+this.options[this.selectedIndex].value+\"/\"+this.options[this.selectedIndex].innerHTML)'>"
    report_list = models.Reports.objects.values().filter(kupa_id=kupa_id)
    for k in report_list:
        output = output+"<option value="+str(k["id"])+">"+str(k["report_date"])+"</option>"
    output = output+"</select><br><button onclick='window.location.replace(\"/\")'>back</button>"
    return HttpResponse(output)

def tabs(request, report_id, report_date):  
    output = "רשימת טאבים:<br><select size = 10 onchange='window.location.replace(\"/details/\"+report_id+\"/\"+this.options[this.selectedIndex].innerHTML)'>"
    tab_list = models.AssetDetails.objects.values("category").filter(reports_id=report_id).distinct()
    for k in tab_list:
        output = output+"<option>"+k["category"]+"</option>"
    output = output+"</select><br><button onclick='window.location.replace(\"/\")'>back</button>"
    return HttpResponse(output)