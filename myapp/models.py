from django.db import models
from django.utils import timezone

class microbit(models.Model):
    microbitID = models.CharField(max_length=6)
    lastTemperatureReading = models.CharField(max_length=6)
    lastLightReading = models.CharField(max_length=6)
    timeOfReading = models.DateTimeField(default=timezone.now)


class microbitsummary(models.Model):
    temperatureMean = models.CharField(max_length=6)
    lightMean = models.CharField(max_length=6)
    numberOfMicrobits = models.CharField(max_length=6)
    timeOfReading = models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.lastLightReading
