from django.urls import path
from . import info

urlpatterns = [
    path('tvn', info.tvn, name="tvn"),
    path('rmf', info.rmf, name="rmf"),
    path('interia', info.interia, name="interia")
]