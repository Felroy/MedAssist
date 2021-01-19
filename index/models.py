from django.db import models

class AppIndex(models.Model):
    app_title = models.CharField(max_length=250)    
    app_logo_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.app_title

class AppDetails(models.Model):
    app_detail = models.ForeignKey(AppIndex, on_delete=models.CASCADE)