from django.db import models

class Company(models.Model):
    pass

class Report(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    submission_date = models.DateField()
