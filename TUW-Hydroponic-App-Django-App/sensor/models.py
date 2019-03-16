from django.db import models

# Create your models here.
class Sensor(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    pH = models.DecimalField(max_digits=2, decimal_places=1)
    Temp=models.IntegerField()
    CO2 = models.DecimalField(max_digits=3, decimal_places=2)
    EC = models.DecimalField(max_digits=6, decimal_places=2)