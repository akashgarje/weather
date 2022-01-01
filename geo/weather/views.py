import json
import requests
from django.shortcuts import render
from .models import coordinate

# Create your views here.
def index(request):
    lat = request.GET['lat'] if 'lat' in request.GET else 40.7306
    lng = request.GET['lng'] if 'lng' in request.GET else -73.9352
    app = coordinate(lat=lat,lng=lng)
    app.save()
    r = requests.get(f'https://api.weather.gov/points/{lat},{lng}')
    print(r.text)
    json_data = json.loads(r.text)
    print(json_data)
    print(json_data['properties']['forecast'])
    r = requests.get(json_data['properties']['forecast'])
    json_data = json.loads(r.text)
    return render(request, "index.html", {'json_data':json_data})