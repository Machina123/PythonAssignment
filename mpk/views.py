from django.http import HttpResponse
import json
import requests
from . import stops


def index(request):
    return HttpResponse("Hello World")


def get_departures(request):
    if "stop" in request.GET:
        req = requests.get(stops.MPK_ENDPOINT_DEPARTS + "?stop=" + request.GET["stop"] + "&mode=departure")
        return HttpResponse(json.dumps(req.json()))
    else:
        return HttpResponse(json.dumps({"success": False, "error": "No stop specified"}))


def get_stops(request):
    return HttpResponse(json.dumps({v: k for k, v in stops.MPK_TRAMSTOPS.items()}))
