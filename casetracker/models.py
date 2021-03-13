from django.db import models

# Create your models here.
class Borough(models.Model):
    borough_name = models.CharField(max_length=30)
    vaccines_given = models.CharField(max_length=30)

    def __str__(self):
        return "{}-{}".format(self.borough_name, self.vaccines_given)

