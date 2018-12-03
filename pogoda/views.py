from django.shortcuts import render
import bs4 as bs
import urllib.request
import json
from django.http import HttpResponse, HttpResponseRedirect
import forecastio