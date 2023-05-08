from django.db import models

class Kupot(models.Model):
    company = models.CharField(maxlength=255)
    track = models.CharField(maxlength=255)
    track_number = models.CharField(maxlength=255)
    track_code = models.CharField(maxlength=255)

class Reports(models.Model):
    kupa = models.ForeignKey(Kupot, on_delete=models.CASCADE)
    report_date = models.DateField()
    category = models.CharField(maxlength=255)
    fair_value = models.FloatField()
    percent_of_total = models.FloatField()


class AssetDetails(model.Model):
     report_id = models.ForeignKey(Reports, on_delete=models.CASCADE)
     category = models.CharField(maxlength=255)
     stock_name = models.CharField(maxlength=255)
     stock_code = models.IntegerField()
     issuer_code = models.IntegerField()
     stock_exchange = models.CharField(maxlength=255)
     rating = models.CharField(maxlength=10)
     rater = models.CharField(maxlength=50)
     purcahse_date = models.DateField()
     average_life_span = models.FloatField()
     currency = models.CharField(maxlength=50)
     interest_rate = models.FloatField()
     proceeds = models.FloatField()
     value = models.FloatField()
     exchange_rate = models.FloatField()
     interest_dividend = models.FloatField()
     market_value = models.FloatField()
     percent_of_value = models.FloatField()
     percent_of_asset_channel = models.FloatField()
     percent_of_total_assets = models.FloatField()
     info_provider = models.CharField(maxlength=100)
     sector = models.CharField(maxlength=100)
     base_asset = models.CharField(maxlength=100)
     fair_value = models.FloatField()
     consortium = model.BooleanField()
     last_valuation_date = models.DateField()
     roi_in_period = models.FloatField()
     estimated_value = models.FloatValue()
     address = models.CharField(maxlength=255)

