from datetime import datetime

import geocoder
import requests
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def temp_here(response):
    endpoint = 'https://api.open-meteo.com/v1/forecast'
    location = geocoder.ip('me').latlng
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    now = datetime.now()
    hour = now.hour
    meteor_data = requests.get(api_request).json()
    temp = meteor_data['hourly']['temperature_2m'][hour]
    return HttpResponse(f"Here it is {temp} degrees")
