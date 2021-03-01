from django.http import HttpResponse
from index.models import AppIndex
from django.shortcuts import render
from .models import Clinic
import folium




# Create your views here.
def facilitylocator(request): 

   map = folium.Map(location=[40.7118, -74.0131], zoom_start=12)
   testi = Clinic.objects.all()
   for item in testi:
       folium.Marker(
       location=item.location,
       popup=item.name,
       icon=folium.Icon()
     ).add_to(map)
       

   
   map=map._repr_html_()


   return render(request, 'facility/facility.html', {'map': map})   


#def test(request):
    #response=requests.post(place_details).json()
    #return render(request, 'facility/facility.html', {'response':response})



    