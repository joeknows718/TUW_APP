from django.db import models

class Sensor(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    pH = models.DecimalField(max_digits=1, decimal_places=1)
    CO2 = models.DecimalField(max_digits=2, decimal_places=2)
    EC = models.DecimalField(max_digits=2, decimal_places=2)