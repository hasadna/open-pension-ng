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
     stock_name = models.CharField(max_length=255, verbose_name="שם ני\"ע")
     stock_code = models.CharField(max_length=255,verbose_name="מספר ני\"ע",null=True)
     issuer_code = models.CharField(max_length=30,verbose_name="מספר מנפיק",null=True)
     stock_exchange = models.CharField(max_length=255,verbose_name="זירת מסחר",null=True)
     rating = models.CharField(max_length=10,verbose_name="דירוג",null=True)
     rater = models.CharField(max_length=50, verbose_name="שם המדרג",null=True)
     purcahse_date = models.DateField(verbose_name="תאריך רכישה",null=True)
     average_life_span = models.FloatField(verbose_name="מח\"מ",null=True)
     currency = models.CharField(max_length=50,verbose_name="סוג מטבע",null=True)
     interest_rate = models.FloatField(verbose_name="שעור ריבית",null=True)
     proceeds = models.FloatField(verbose_name="תשואה לפדיון",null=True)
     value = models.FloatField(verbose_name="ערך נקוב",null=True)
     exchange_rate = models.FloatField(verbose_name="שער",null=True)
     interest_dividend = models.FloatField(verbose_name="פדיון ריבית דיבידנד",null=True)
     market_value = models.FloatField(verbose_name="שווי שוק",null=True)
     percent_of_value = models.FloatField(verbose_name="שעור מערך נקוב",null=True)
     percent_of_asset_channel = models.FloatField(verbose_name="שעור מנכסי אפיק ההשקעה",null=True)
     percent_of_total_assets = models.FloatField(verbose_name="שעור מנכסי השקעה",null=True)
     info_provider = models.CharField(verbose_name="ספק המידע",max_length=100,null=True)
     sector = models.CharField(verbose_name="ענף מסחר",max_length=100,null=True)
     base_asset = models.CharField(verbose_name="נכס הבסיס",max_length=100,null=True)
     fair_value = models.FloatField(verbose_name="שווי הוגן",null=True)
     consortium = models.CharField(verbose_name="קונסורציום",max_length=4,null=True)
     last_valuation_date = models.DateField(verbose_name="תאריך שערוך אחרון",null=True)
     roi_in_period = models.FloatField(verbose_name="שעור תשואה במהלך התקופה",null=True)
     estimated_value = models.FloatField(verbose_name="שווי משוערך",null=True)
     address = models.CharField(verbose_name="כתובת הנכס",max_length=255,null=True)
     average_interest_rate = models.FloatField(verbose_name="שיעור ריבית ממוצע",null=True)
     asset_type = models.CharField(verbose_name="אופי הנכס",max_length=255,null=True)
     commitment = models.FloatField(verbose_name="סכום ההתחייבות",null=True)
     effective_interest = models.FloatField(verbose_name="ריבית אפקטיבית",null=True)
     coordinated_cost = models.FloatField(verbose_name="עלות מתואמת",null=True)
     commitment_end_date = models.DateField(verbose_name="תאריך סיום ההתחייבות",null=True)

class FilesNotIngested(models.Model):
    file_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    info = models.CharField(max_length=1024)

class UnmappedFields(models.Model):
    file_name = models.CharField(max_length=255)
    tab_name  = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=255,null=True)
