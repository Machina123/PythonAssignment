from django.urls import path
from . import views

urlpatterns = [
    path('szukajka', views.szukajka),
]