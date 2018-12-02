from django.urls import path
from . import info

urlpatterns = [
    path('tv', info.tv, name="tvn"),
    path('rmf', info.rmf, name="rmf"),
    path('interia', info.interia, name="interia")
]