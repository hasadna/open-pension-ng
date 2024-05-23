from django.db import models

class Kupot(models.Model):
    company = models.CharField(max_length=255)
    track = models.CharField(max_length=255)
    track_number = models.CharField(max_length=255)
    track_code = models.CharField(max_length=255, null=True)

class Reports(models.Model):
    kupa = models.ForeignKey(Kupot, on_delete=models.CASCADE)
    report_date = models.DateField()
    file_name = models.CharField(max_length=255, null=True)
    ingested_at = models.DateTimeField(auto_now=True)


class Summary(models.Model):
    kupa = models.ForeignKey(Kupot, on_delete=models.CASCADE)
    report= models.ForeignKey(Reports, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    fair_value = models.FloatField()
    percent_of_total = models.FloatField()

class AssetDetails(models.Model):
     reports = models.ForeignKey(Reports, on_delete=models.CASCADE)
     category = models.CharField(max_length=255,null=True)
     stock_name = models.CharField(max_length=255)
     stock_code = models.CharField(max_length=255,null=True)
     issuer_code = models.CharField(max_length=30,null=True)
     stock_exchange = models.CharField(max_length=255,null=True)
     rating = models.CharField(max_length=10,null=True)
     rater = models.CharField(max_length=50,null=True)
     purcahse_date = models.DateField(null=True)
     average_life_span = models.FloatField(null=True)
     currency = models.CharField(max_length=50,null=True)
     interest_rate = models.FloatField(null=True)
     proceeds = models.FloatField(null=True)
     value = models.FloatField(null=True)
     exchange_rate = models.FloatField(null=True)
     interest_dividend = models.FloatField(null=True)
     market_value = models.FloatField(null=True)
     percent_of_value = models.FloatField(null=True)
     percent_of_asset_channel = models.FloatField(null=True)
     percent_of_total_assets = models.FloatField(null=True)
     info_provider = models.CharField(max_length=100,null=True)
     sector = models.CharField(max_length=100,null=True)
     base_asset = models.CharField(max_length=100,null=True)
     fair_value = models.FloatField(null=True)
     consortium = models.CharField(max_length=4,null=True)
     last_valuation_date = models.DateField(null=True)
     roi_in_period = models.FloatField(null=True)
     estimated_value = models.FloatField(null=True)
     address = models.CharField(max_length=255,null=True)
     average_interest_rate = models.FloatField(null=True)
     asset_type = models.CharField(max_length=255,null=True)
     commitment = models.FloatField(null=True)
     effective_interest = models.FloatField(null=True)
     coordinated_cost = models.FloatField(null=True)
     commitment_end_date = models.DateField(null=True)

class FilesNotIngested(models.Model):
    file_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    info = models.CharField(max_length=1024)

class UnmappedFields(models.Model):
    file_name = models.CharField(max_length=255)
    tab_name  = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
