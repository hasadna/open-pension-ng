from django.contrib import admin

# Register your models here.

from .models import Kupot
from .models import Reports
from .models import AssetDetails

admin.site.register(Kupot)
admin.site.register(Reports)
admin.site.register(AssetDetails)