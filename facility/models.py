from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from django.db import models
from django.db.models import Manager as GeoManager
from geopy.geocoders.googlev3 import GoogleV3
from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path



class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    location = gis_models.PointField(geography=True, null=True)

    objects = GeoManager()


    #def __unicode__(self):
     #   return self.name

    #def appendDB(self, **kwargs):
   #     if not self.location:
  #          address = u'%s %s' % (self.city, self.address)
    #        address = address.encode('utf-8')
    #        geocoder = GoogleV3()
#
    #        try:
       #         _, latlon = geocoder.geocode(address)
      #      except (ValueError):
        #        pass
        #    else:
        #        point = "POINT(%s %s)" #% (latlon[1], latlon[0])
          #      self.location = geos.fromstr(point)
                
       # super(Clinic, self).save()