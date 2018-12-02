from django.urls import path
from . import wiadomosci

urlpatterns = [
    path('tv', wiadomosci.tv, name="tvn"),
    path('rmf', wiadomosci.rmf, name="rmf"),
    path('interia', wiadomosci.interia, name="interia")
]