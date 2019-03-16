from django.shortcuts import render
#from EnvSensor.models import Sensor
#Get and Post requests
def home(request):
    return render(request,"home.html")

