from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import plotly.offline as opy
import plotly.plotly as py
import plotly.graph_objs as go
from django.contrib.auth.models import User
from sensor.models import Sensor, System
from sensor.forms import UserForm
from django.utils import timezone
import datetime

def home(request):
    sensor = Sensor.objects.all()
    print(sensor)
    context = {
        "sensor":sensor[0]
    }
    return render(request,"home.html",context)

def register(request):
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save() 

		else:
			print(user_form.errors)

	else:
		user_form = UserForm()

	return render(request, 'register.html', {'user_form' : user_form})

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			login(request, user)
			return HttpResponseRedirect('/home')
		else:
			print("Invalid login details : {0},{1}".format(username, password))
			return HttpResponse('Your login credentials were wrong')

	else:
		return render(request, 'login.html')

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

# @login_required
def dashboard(request):
	date_query = request.GET.get('date')
	graph_query = request.GET.get('graph')
	today = timezone.now()

	if date_query:
		if date_query == "week":
			date_begin = today - datetime.timedelta(days=7)
		elif date_query == "month":
			date_begin = today - datetime.timedelta(days=30)
		elif date_query == "90":
			date_begin = today - datetime.timedelta(days=90)
		else:
			date_begin = today - datetime.timedelta(days=1)
	else:
		date_begin = today - datetime.timedelta(days=1)

	system = System.objects.filter(user=request.user)
	sensor = Sensor.objects.filter(system=system[0]).filter(date__range=[date_begin, today])
	current_status = sensor[0]
	print(sensor[0])
    #with all datas, set it to an array
	dates = []
	yValues = []
	availableValues = len(sensor)
	if graph_query:
		graphType = graph_query
	else:
		graphType = "pH"

	for info in sensor:
		dates.append(info.date.strftime("%b %d %Y %I %p"))
		yValues.append(getattr(info,graphType))
	
	dates.reverse()
	yValues.reverse()

	graph = [go.Scatter(
		x = dates,
		y = yValues
	)]

	# notifications =
	context = {
		"graph": opy.plot(graph, auto_open=False, output_type='div'),
		"current_status": current_status,
	}

	return render(request,"dashboard.html",context)