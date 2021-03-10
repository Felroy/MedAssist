from django.http import HttpResponse
from index.models import AppIndex
from django.shortcuts import render
from .models import Clinic
import folium
from geopy.geocoders import Nominatim
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance 


# Create your views here.
def facilitylocator(request): 
  loc = request.POST.get('your_address')
  geolocator = Nominatim(user_agent='felroy01998@gmail.com')
  location1 = geolocator.geocode(loc)
    
  map = folium.Map(location=[location1.latitude, location1.longitude], zoom_start=12)
  folium.Marker(
    location=[location1.latitude, location1.longitude],
    popup='You are here!',
    icon=folium.Icon(color='red')    
  ).add_to(map)
  test = Clinic.objects.all()
  for item in test:
      folium.Marker(
      location=item.location,
      popup=item.name,
      icon=folium.Icon()
    ).add_to(map)      

  
  map=map._repr_html_()


  return render(request, 'facility/facility.html', {'map': map})   

def nearestclinic(request):
  loc = request.POST.get('your_address')
  geolocator = Nominatim(user_agent='felroy01998@gmail.com')
  location1 = geolocator.geocode(loc)
  point = Point(location1.latitude, location1.longitude)
  
  sort = Clinic.objects.filter(location__distance_lt=(point, Distance(km=2)))

  return render(request, 'facility/facility.html', {'sort': sort})
#def test(request): 
    #response=requests.post(place_details).json()
    #return render(request, 'facility/facility.html', {'response':response})



    