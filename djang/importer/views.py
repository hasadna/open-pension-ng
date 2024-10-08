from django.shortcuts import render
from importer import models
from django.http import HttpResponse
from django.http import FileResponse

root="/"


def companies(request):
    output = "רשימת החברות:<br><select size= 10 onchange='window.location.replace(\"/\"+this.options[this.selectedIndex].innerHTML)'>"
    company_list = models.Kupot.objects.values("company").distinct().order_by("company")
    return render(request, 'importer/index.html', context={'company_list': company_list})


def kupot(request, company_name):
    output = "רשימת מסלולים ל"+company_name+":<br><select size = 10 \
        onchange=window.location.replace(\"/\duchot/\"+this.options[this.selectedIndex].value+\"/\"+this.options[this.selectedIndex].innerHTML)>"
    company_list = models.Kupot.objects.values().filter(company=company_name)
    for k in company_list:
        output = output+"<option value="+str(k["id"])+">"+k["track"]+"</option>"
    output = output+"</select><br><button onclick='window.location.replace(\"/\")'>Home</button>"
    return render(request, 'importer/kupa.html', context={'company_name': company_name, 'company_list': company_list})
    # return HttpResponse(output)

def duchot(request, kupa_id, kupa):
    output = "רשימת דוח\"ות ל"+str(kupa)+":<br><select size = 10 onchange='window.location.replace(\"/tabs/\"+this.options[this.selectedIndex].value+\"/\"+this.options[this.selectedIndex].innerHTML)'>"
    report_list = models.Reports.objects.values().filter(kupa_id=kupa_id)
    for k in report_list:
        output = output+"<option value="+str(k["id"])+">"+str(k["report_date"])+"</option>"
    output = output+"</select><br><button onclick='window.location.replace(\"/\")'>Home</button>"
    return HttpResponse(output)

def tabs(request, report_id, report_date):
    reports =   models.Reports.objects.values().filter(id=report_id)
    file_name = reports[0]["file_name"]
    file_name = file_name[file_name.rfind("/"):]
    output = "<a href='/files"+file_name+"'>פתח קובץ:</a><br>רשימת טאבים:<br>"+\
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

def files(request,file_name):
        filename="./xlsx-files/"+file_name
        return FileResponse(open(filename, "rb"),
           headers={
            "Content-Type": "application/vnd.ms-excel",
            "Content-Disposition": 'attachment; filename="'+filename+'"',
           }
        )