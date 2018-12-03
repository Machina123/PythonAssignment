from django.urls import path
from . import views

urlpatterns = [
    path('tvn', views.tvn, name="tvn")
]