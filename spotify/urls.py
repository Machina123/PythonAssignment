from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('authcode', views.authcode, name="auth"),
    path('token', views.get_token, name="token"),
    path('refresh_token', views.refresh_token, name="refresh_token"),
    path('user', views.get_user_data, name="user"),
    path('now_playing', views.now_playing, name="now-playing"),
    path('next', views.next_track, name="next"),
    path('prev', views.prev_track, name="prev"),
    path('pause', views.pause, name="pause"),
    path('play', views.play, name="play"),
]