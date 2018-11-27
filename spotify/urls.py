from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('authcode', views.authcode, name="auth"),
    path('token', views.get_token, name="token"),
]