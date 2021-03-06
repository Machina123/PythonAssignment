from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('departures', views.get_departures, name="departures"),
    path('stops', views.get_stops, name="stops")
]