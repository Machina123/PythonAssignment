from django.shortcuts import render
import requests
from django.http import HttpResponse, HttpResponseRedirect
import json

api_key = "c26cd8d618c32f318fef96a3b9756d1c"
lat = 50.0614300
lng = 19.9365800
url = "https://api.darksky.net/forecast/"+api_key+"/"+str(lat)+","+str(lng)+"?lang=pl&units=si"

def pogoda(request):
    json_data = requests.get(url).json()
    return HttpResponse(json.dumps(json_data['currently']))