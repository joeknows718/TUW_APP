

# Create your views here.
from django.shortcuts import render
from sensor.models import Sensor
#Get and Post requests
def home(request):
    sensor = Sensor.objects.all()
    print(sensor)
    context = {
        "sensor":sensor[0]
    }
    return render(request,"home.html",context)