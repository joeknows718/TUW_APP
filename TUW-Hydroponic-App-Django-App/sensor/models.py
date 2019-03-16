from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sensor(models.Model):
	user = models.ForeignKey(User, on_delete='CASCADE', null=True)
	date = models.DateTimeField(auto_now_add=True)
	pH = models.FloatField()
	Temp = models.IntegerField()
	CO2 = models.FloatField()
	EC = models.FloatField()