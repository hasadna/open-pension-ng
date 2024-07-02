"""
URL configuration for djang project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from importer import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.companies, name="חברות"),
    path("<str:company_name>/", views.kupot, name="קופות"),
    path("duchot/<int:kupa_id>/<str:kupa>", views.duchot, name="דוחות"),
    path("tabs/<int:report_id>/<str:report_date>", views.tabs, name="טאבים"),
    path("details/<int:report_id>/<str:tab>", views.details, name="")
]
