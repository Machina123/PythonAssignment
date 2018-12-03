from django.http import HttpResponse
import json
import requests
from . import stops
# Create your views here.


def index(request):
    return HttpResponse("Hello World")


def get_departures(request):
    if "stop" in request.GET:
        req = requests.get(stops.MPK_ENDPOINT_DEPARTS + "?stop=" + request.GET["stop"] + "&mode=departure")
        return HttpResponse(json.dumps(req.json()))
    else:
        return HttpResponse(json.dumps({"success": False, "error": "No stop specified"}))
