from django.db import models

# Create your models here.
class DiseaseList(models.Model):
    name = models.CharField(max_length=250)
    symplist = models.CharField(max_length=250)
    
