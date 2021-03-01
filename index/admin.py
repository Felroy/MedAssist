from django.contrib import admin
from .models import AppIndex, AppDetail
from django.contrib.gis.admin import OSMGeoAdmin
from facility.models import Clinic
from symp.models import DiseaseList

admin.site.register(AppIndex)
admin.site.register(AppDetail)
admin.site.register(DiseaseList)
# Register your models here.

@admin.register(Clinic)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')