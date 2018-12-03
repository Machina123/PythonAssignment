from django.urls import path
from . import views

urlpatterns = [
    path('pogoda', views.pogoda, name="pogoda")
]