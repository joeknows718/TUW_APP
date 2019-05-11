
from sensor.models import Sensor, System
from django.utils import timezone
import datetime
import random

def run():
	system = System.objects.all()[0]
	today = timezone.now()
	for i in range(1, 4320):
		date = today - datetime.timedelta(hours=i)
		newSensor = Sensor(
			system = system,
			date = date,
			pH = random.uniform(0,14),
			Temp = random.randint(0,14),
			CO2 = random.uniform(0,14),
			EC = random.uniform(0,14))
		newSensor.save()