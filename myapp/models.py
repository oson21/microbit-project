from django.db import models
#from django.utils import.models import timezone for showing time in future

class microbit(models.Model):
    lastTemperatureReading = models.CharField(max_length=6)
    lastLightReading = models.CharField(max_length=6)
    # time_posted = models.DateTimeField(default=timezone.now)

class microbitsummary(models.Model):
    temperatureMean = models.CharField(max_length=6)
    lightMean = models.CharField(max_length=6)

def __str__(self):
    return self.lastLightReading
