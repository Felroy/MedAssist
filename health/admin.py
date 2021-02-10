from django.contrib.gis.admin import OSMGeoAdmin
from facility.models import Clinic

@admin.register(Clinic)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')