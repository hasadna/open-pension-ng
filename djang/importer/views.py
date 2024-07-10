from django.shortcuts import render
from importer import models
from django.http import HttpResponse

root="/"

def companies(request):
    output = "רשימת החברות:<br><select size= 10 onchange='window.location.replace(\"/\"+this.options[this.selectedIndex].innerHTML)'>"
    company_list = models.Kupot.objects.values("company").distinct().order_by("company")
    for k in company_list:
        output = output+"<option >"+k["company"]+"</option>"
    output = output+"</select>"
    return HttpResponse(output)

def kupot(request, company_name):
    output = "רשימת מסלולים ל"+company_name+":<br><select size = 10 \
        onchange=window.location.replace(\"/\duchot/\"+this.options[this.selectedIndex].value+\"/\"+this.options[this.selectedIndex].innerHTML)>"
    company_list = models.Kupot.objects.values().filter(company=company_name)
    for k in company_list:
        output = output+"<option value="+str(k["id"])+">"+k["track"]+"</option>"
    output = output+"</select><br><button onclick='window.location.replace(\"/\")'>Home</button>"
    return HttpResponse(output)

def duchot(request, kupa_id, kupa):
    output = "רשימת דוח\"ות ל"+str(kupa)+":<br><select size = 10 onchange='window.location.replace(\"/tabs/\"+this.options[this.selectedIndex].value+\"/\"+this.options[this.selectedIndex].innerHTML)'>"
    report_list = models.Reports.objects.values().filter(kupa_id=kupa_id)
    for k in report_list:
        output = output+"<option value="+str(k["id"])+">"+str(k["report_date"])+"</option>"
    output = output+"</select><br><button onclick='window.location.replace(\"/\")'>Home</button>"
    return HttpResponse(output)

def tabs(request, report_id, report_date):
    reports =   models.Reports.objects.values().filter(id=report_id)
    output = "קובץ  "+reports[0]["file_name"]+"<br>רשימת טאבים:<br>"+\
    "<select size = 10 onchange='window.location.replace(\"/details/"+str(report_id)+"/\"+this.options[this.selectedIndex].innerHTML)'>"
    tab_list = models.AssetDetails.objects.values("category").filter(reports_id=report_id).distinct()
    for k in tab_list:
        output = output+"<option>"+k["category"]+"</option>"
    output = output+"</select><br><button onclick='window.location.replace(\"/\")'>Home</button>"
    return HttpResponse(output)

def details(request, report_id, tab):
    field_list = models.AssetDetails._meta.get_fields()
    #list(models.AssetDetails.objects.values().filter(reports_id=report_id).filter(category=tab).values().first().keys())
    output = "<table border=1>"
    for f in field_list:
        output = output + "<th>"+f.verbose_name+"</th>"
    value_list = models.AssetDetails.objects.values().filter(reports_id=report_id).filter(category=tab).values()
    for v in value_list:
        output = output+"<tr>"
        for f in field_list:
            if f.name in v and v[f.name] is not None:
                    output = output + "<th>"+str(v[f.name])+"</th>"
            else:     
                output = output + "<th></th>"
        output = output + "</tr>"        
    output = output+"</table><br><button onclick='window.location.replace(\"/\")'>Home</button>" 
    return HttpResponse(output)