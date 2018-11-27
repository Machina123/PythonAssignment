from typing import Dict

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
import urllib.parse
import base64
import requests
import json

from . import appdata

# Create your views here.
redirect_url = urllib.parse.quote_plus(appdata.LOCAL_ENDPOINT_REDIRURL)

def index(request):
    resp_string = ""
    is_success = "error"
    if "code" in request.GET:
        resp_string += "Got authorization code:" + request.GET["code"]
        auth_data = open("spotify_auth.dat", "w")
        auth_data.write(request.GET["code"])
        auth_data.close()
        is_success = "success"
    elif "error" in request.GET:
        resp_string += "Error during authorization: " + request.GET["error"]
    return redirect("/?spotify=" + is_success)


def authcode(request):
    scopes = urllib.parse.quote_plus("user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-birthdate user-read-email")
    url = appdata.SPOTIFY_ENDPOINT_AUTH + "?response_type=code&client_id=" + appdata.SPOTIFY_CLIENT_ID + "&scopes=" + scopes + "&redirect_uri=" + redirect_url
    return HttpResponseRedirect(url)


def get_token(request):
    try:
        spoti_auth = base64.b64encode((appdata.SPOTIFY_CLIENT_ID + ":" + appdata.SPOTIFY_CLIENT_SECRET).encode())
        spoti_auth_token_file = open("spotify_auth.dat", "r")
        spoti_auth_token = spoti_auth_token_file.read()
        spoti_auth_token_file.close()
        params = {"client_id": appdata.SPOTIFY_CLIENT_ID, "client_secret": appdata.SPOTIFY_CLIENT_SECRET, "grant_type": "authorization_code", "code": spoti_auth_token, "redirect_uri": appdata.LOCAL_ENDPOINT_REDIRURL}
        req = requests.post(appdata.SPOTIFY_ENDPOINT_TOKEN, data=params)
        resp = req.json()
        if "error" in resp:
            return redirect("/spotify/authcode")
        elif "access_token" in resp:
            spoti_access_token_file = open("spoti_access_token.json", "w")
            spoti_access_token_file.write(json.dumps(resp))
            spoti_access_token_file.close()
            return redirect("/")
    except FileNotFoundError:
        return redirect("/spotify/authcode")