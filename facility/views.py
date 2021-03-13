from django.http import HttpResponse
from index.models import AppIndex
from django.shortcuts import render
from .models import Clinic
import folium
from geopy.geocoders import Nominatim
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance



def facilitylocator(request): 
  #geocoding user input
  loc = request.POST.get('your_address')
  geolocator = Nominatim(user_agent='felroy01998@gmail.com')
  location1 = geolocator.geocode(loc) 

  #turning user's location into POINT(latitude, longitude) format 
  point1 = Point(location1.latitude, location1.longitude)

  #Creating map + attributes
  mapfigure= folium.Figure(width=1200, height=800)  
  map = folium.Map(location=[location1.latitude, location1.longitude], zoom_start=12).add_to(mapfigure)
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
    
 
  #filtering and sorting clinic based on user's location
  sort = Clinic.objects.filter(location__distance_lt=(point1, Distance(km=5)))
  
  map=map._repr_html_()
  context = {
    'map': map,
    'sort':sort
    }
  print(sort)
  return render(request, 'facility/facility.html', context)   

#def nearestclinic(request):
  loc = request.POST.get('your_address')
  geolocator = Nominatim(user_agent='felroy01998@gmail.com')
  location1 = geolocator.geocode(loc)
  
  
  

  return render(request, 'facility/facility.html', {'sort': sort})
#def test(request): 
    #response=requests.post(place_details).json()
    #return render(request, 'facility/facility.html', {'response':response})



    