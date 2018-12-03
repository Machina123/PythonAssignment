from django.urls import path
from . import views

urlpatterns = [
    path('mac', views.mac),
    path('subway', views.subway),
    path('dagrasso', views.dagrasso),
]