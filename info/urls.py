from django.urls import path
from . import views

urlpatterns = [
    path('tvn', views.tvn, name="tvn"),
    path('rmf', views.rmf, name="rmf"),
    path('interia', views.interia, name="interia")
]