from django.urls import path
from sensor import views

urlpatterns = [
    path("",views.home),
    path("register/",views.register),
    path("login/",views.login),
    path("dashboard/",views.dashboard),

]