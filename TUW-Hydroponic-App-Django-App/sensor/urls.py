from django.urls import path
from sensor import views

urlpatterns = [
    path("",views.home)
]