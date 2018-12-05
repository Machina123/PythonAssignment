from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
import urllib.parse
import requests
from requests.auth import HTTPBasicAuth
import json
import time

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
        spoti_auth_token_file = open("spotify_auth.dat", "r")
        spoti_auth_token = spoti_auth_token_file.read()
        spoti_auth_token_file.close()
        params = {"client_id": appdata.SPOTIFY_CLIENT_ID, "client_secret": appdata.SPOTIFY_CLIENT_SECRET,
                  "grant_type": "authorization_code", "code": spoti_auth_token,
                  "redirect_uri": appdata.LOCAL_ENDPOINT_REDIRURL}

        req = requests.post(appdata.SPOTIFY_ENDPOINT_TOKEN, data=params)
        resp = req.json()
        if "error" in resp:
            is_success = "error"
            return redirect("/?spotify=" + is_success)
        elif "access_token" in resp:
            spoti_access_token_file = open("spoti_access_token.json", "w")
            spoti_access_token_file.write(json.dumps(resp))
            spoti_access_token_file.close()
            spoti_last_refresh_file = open("spoti_last_token_refresh.dat", "w")
            spoti_last_refresh_file.write(str(int(time.time())))
            spoti_last_refresh_file.close()
    elif "error" in request.GET:
        resp_string += "Error during authorization: " + request.GET["error"]
    return redirect("/?spotify=" + is_success)


def authcode(request):
    scopes = "user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-private user-read-birthdate user-read-email"
    url = appdata.SPOTIFY_ENDPOINT_AUTH + "?response_type=code&client_id=" + appdata.SPOTIFY_CLIENT_ID + "&scope=" + scopes + "&redirect_uri=" + redirect_url
    return redirect(url)


def get_token(request):
    try:
        spoti_auth_token_file = open("spotify_auth.dat", "r")
        spoti_auth_token = spoti_auth_token_file.read()
        spoti_auth_token_file.close()
        params = {"client_id": appdata.SPOTIFY_CLIENT_ID, "client_secret": appdata.SPOTIFY_CLIENT_SECRET,
                  "grant_type": "authorization_code", "code": spoti_auth_token,
                  "redirect_uri": appdata.LOCAL_ENDPOINT_REDIRURL}

        req = requests.post(appdata.SPOTIFY_ENDPOINT_TOKEN, data=params)
        resp = req.json()
        if "error" in resp:
            return HttpResponse(json.dumps({"success": False, "error": resp["error"]}))
        elif "access_token" in resp:
            spoti_access_token_file = open("spoti_access_token.json", "w")
            spoti_access_token_file.write(json.dumps(resp))
            spoti_access_token_file.close()
            spoti_last_refresh_file = open("spoti_last_token_refresh.dat", "w")
            spoti_last_refresh_file.write(str(int(time.time())))
            spoti_last_refresh_file.close()
            return HttpResponse(json.dumps(resp))
    except FileNotFoundError:
        return HttpResponse(json.dumps({"success": False, "error": "User not logged in"}))


def refresh_token(request):
    return HttpResponse(json.dumps(int_refresh_token()))


def read_token():
    spoti_acesstoken = open("spoti_access_token.json", "r")
    spoti_tokendata = json.loads(spoti_acesstoken.read())
    spoti_acesstoken.close()
    return spoti_tokendata["access_token"]


def get_user_data(request):
    headers = {"Authorization": "Bearer " + read_token()}
    req = requests.get(appdata.SPOTIFY_ENDPOINT_USER, headers=headers)
    resp = req.json()
    return HttpResponse(json.dumps(resp))


def now_playing(request):
    refresh = int_refresh_token()
    if "success" in refresh:
        if refresh["success"] is True:
            headers = {"Authorization": "Bearer " + read_token()}
            req = requests.get(appdata.SPOTIFY_ENDPOINT_NOW_PLAYING, headers=headers)
            resp = req.json()
            return HttpResponse(json.dumps(resp))
        else:
            return HttpResponse(json.dumps({"success": False, "error": "User not authorized"}))
    else:
        return HttpResponse(json.dumps({"success": False, "error": "User not authorized"}))


def int_refresh_token():
    return_obj = {}
    try:
        spoti_acesstoken = open("spoti_access_token.json", "r")
        spoti_lastrefreshf = open("spoti_last_token_refresh.dat", "r")
        spoti_lastrefresh = int(spoti_lastrefreshf.read())
        spoti_tokendata = json.loads(spoti_acesstoken.read())
        spoti_acesstoken.close()
        spoti_lastrefreshf.close()
        if "expires_in" in spoti_tokendata:
            return_obj["success"] = True
            if (spoti_lastrefresh + int(spoti_tokendata["expires_in"])) < time.time():
                params = {"grant_type": "refresh_token", "refresh_token": spoti_tokendata["refresh_token"]}
                req = requests.post(appdata.SPOTIFY_ENDPOINT_TOKEN, data=params,
                                    auth=HTTPBasicAuth(appdata.SPOTIFY_CLIENT_ID, appdata.SPOTIFY_CLIENT_SECRET))
                resp = req.json()
                spoti_acesstoken = open("spoti_access_token.json", "w")
                spoti_lastrefreshf = open("spoti_last_token_refresh.dat", "w")
                spoti_tokendata["access_token"] = resp["access_token"]
                spoti_tokendata["expires_in"] = resp["expires_in"]
                spoti_acesstoken.write(json.dumps(spoti_tokendata))
                spoti_lastrefreshf.write(str(int(time.time())))
                spoti_acesstoken.close()
                spoti_lastrefreshf.close()
                return_obj["message"] = "Token refreshed"
            else:
                return_obj["message"] = "No need to refresh, token is still valid"
        else:
            return_obj["success"] = False
            return_obj["message"] = "Client is not authhorized, please go to /spotify/authcode first"
    except FileNotFoundError:
        return_obj["success"] = False
        return_obj["message"] = "Client is not authhorized, please go to /spotify/authcode first"
    return return_obj


def next_track(request):
    refresh = int_refresh_token()
    if "success" in refresh:
        if refresh["success"] is True:
            headers = {"Authorization": "Bearer " + read_token()}
            req = requests.post(appdata.SPOTIFY_ENDPOINT_NEXT, headers=headers)
            if req.status_code == requests.codes.no_content:
                return HttpResponse(json.dumps({"success": True}))
            else:
                return HttpResponse(json.dumps(req.json()))
        else:
            return HttpResponse(json.dumps({"success": False, "error": "User not authorized"}))
    else:
        return HttpResponse(json.dumps({"success": False, "error": "User not authorized"}))


def prev_track(request):
    refresh = int_refresh_token()
    if "success" in refresh:
        if refresh["success"] is True:
            headers = {"Authorization": "Bearer " + read_token()}
            req = requests.post(appdata.SPOTIFY_ENDPOINT_PREVIOUS, headers=headers)
            if req.status_code == requests.codes.no_content:
                return HttpResponse(json.dumps({"success": True}))
            else:
                return HttpResponse(json.dumps(req.json()))
        else:
            return HttpResponse(json.dumps({"success": False, "error": "User not authorized"}))
    else:
        return HttpResponse(json.dumps({"success": False, "error": "User not authorized"}))


def pause(request):
    refresh = int_refresh_token()
    if "success" in refresh:
        if refresh["success"] is True:
            headers = {"Authorization": "Bearer " + read_token()}
            req = requests.put(appdata.SPOTIFY_ENDPOINT_PAUSE, headers=headers)
            if req.status_code == requests.codes.no_content:
                return HttpResponse(json.dumps({"success": True}))
            else:
                return HttpResponse(json.dumps(req.json()))
        else:
            return HttpResponse(json.dumps({"success": False, "error": "User not authorized"}))
    else:
        return HttpResponse(json.dumps({"success": False, "error": "User not authorized"}))


def play(request):
    refresh = int_refresh_token()
    if "success" in refresh:
        if refresh["success"] is True:
            headers = {"Authorization": "Bearer " + read_token()}
            req = requests.put(appdata.SPOTIFY_ENDPOINT_PLAY, headers=headers)
            if req.status_code == requests.codes.no_content:
                return HttpResponse(json.dumps({"success": True}))
            else:
                return HttpResponse(json.dumps(req.json()))
        else:
            return HttpResponse(json.dumps({"success": False, "error": "User not authorized"}))
    else:
        return HttpResponse(json.dumps({"success": False, "error": "User not authorized"}))
