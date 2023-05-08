from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)

class Report(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    submission_date = models.DateField()
