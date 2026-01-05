from django.shortcuts import render
from importer import models
from django.http import HttpResponse

root="/"


def companies(request):
    company_list = models.Kupot.objects.values("company").distinct().order_by("company")
    return render(request, 'importer/index.html', context={'company_list': company_list})


def kupot(request, company_name):
    company_list = models.Kupot.objects.values().filter(company=company_name)
    return render(request, 'importer/kupa.html', context={'company_name': company_name, 'company_list': company_list})

def duchot(request, kupa_id, kupa):
    report_list = models.Reports.objects.values().filter(kupa_id=kupa_id)
    return render(request, 'importer/reports.html', context={'report_list': report_list})

def tabs(request, report_id, report_date):
    reports =   models.Reports.objects.values().filter(id=report_id)
    tab_list = models.AssetDetails.objects.values("category").filter(reports_id=report_id).distinct()
    return render(request, 'importer/tabs.html', context={'file_name': reports[0]['file_name'], 'tab_list': tab_list})

def details(request, report_id, tab):
    field_list = models.AssetDetails._meta.get_fields()
    #list(models.AssetDetails.objects.values().filter(reports_id=report_id).filter(category=tab).values().first().keys())
    output = "<table border=1>"
    table_headers = [f.verbose_name for f in field_list]
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