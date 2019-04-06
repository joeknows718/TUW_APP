from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class System(models.Model):
	user = models.ForeignKey(User, on_delete='CASCADE', null=True)
	pH_low_threshold = models.FloatField()
	Temp_low_threshold = models.IntegerField()
	CO2_low_threshold = models.FloatField()
	EC_low_threshold = models.FloatField()
	pH_high_threshold = models.FloatField()
	Temp_high_threshold = models.IntegerField()
	CO2_high_threshold = models.FloatField()
	EC_high_threshold = models.FloatField()

class Sensor(models.Model):
	system = models.ForeignKey(System, on_delete='CASCADE', null=True)
	date = models.DateTimeField(default=timezone.now())
	pH = models.FloatField()
	Temp = models.IntegerField()
	CO2 = models.FloatField()
	EC = models.FloatField()