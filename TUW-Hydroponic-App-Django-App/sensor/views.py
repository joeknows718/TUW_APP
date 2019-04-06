from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import plotly.offline as opy
import plotly.plotly as py
import plotly.graph_objs as go
from django.contrib.auth.models import User
from sensor.models import Sensor, System
from sensor.forms import UserForm
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
	if date_query:
		date = datetime.date(date_query)
		print(date)
	else:
		date = datetime.date.today()
	system = System.objects.filter(user=request.user)
	print(system[0])
	sensor = Sensor.objects.filter(system=system[0])

    #with all datas, set it to an array
    # date = Sensor.objects.filter(D/)
	dates = []
	ph = []
	co2 = []
	temp = []
	ec = []
	availableValues = len(sensor)
	for info in sensor:
		dates.append(info.date.strftime("%b %d %Y %I %p"))
		ph.append(info.pH)
		co2.append(info.CO2)
		ec.append(info.EC)
		temp.append(info.Temp)
	print(dates,ph,temp,co2,ec)

	ph_graph = [go.Bar(
		x= dates, #dates
		y=ph #range
	)]
	ec_graph = [go.Bar(
		x= dates, #dates
		y=ec #range
	)]
	temp_graph = [go.Bar(
		x= dates, #dates
		y=temp #range
	)]
	co2_Graph = [go.Bar(
		x= dates, #dates
		y=co2 #range
	)]

	context = {
		"ph": opy.plot(ph_graph, auto_open=False, output_type='div'),
		"ec": opy.plot(ec_graph, auto_open=False, output_type='div'),
		"temp": opy.plot(temp_graph, auto_open=False, output_type='div'),
		"co2": opy.plot(co2_Graph, auto_open=False, output_type='div'),
	}
    
    # print(context["graph"])

    # for _ in range(24):
    #     Sensor.objects.create(
    #         pH = random.uniform(0.0, 9.9),
    #         Temp = random.randrange(-10,90),
    #         CO2 = random.uniform(25.00,45.00),
    #         EC = random.uniform(0.0, 2.0),
    #         Humidity = random.uniform(00.00, 99.99)
    #     )
    #     print("test")

    # datetime_object = datatime.strptime(sensor[0].date,)
	return render(request,"dashboard.html",context)