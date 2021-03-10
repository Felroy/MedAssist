from django.http import HttpResponse
from index.models import AppIndex
from django.shortcuts import render
import folium


# Create your views here.
def localcasetracker(request):
    

    map = folium.Map(location=[51.528308,-0.3817686], zoom_start=12) 
    map=map._repr_html_()
    return render(request, 'casetracker/casetracker.html', {'casemap' : map})


    