from django.http import HttpResponse
from index.models import AppIndex
from django.shortcuts import render
from facility.googleapi import place_details
import requests



# Create your views here.
def facilitylocator(request):    
    return render(request, 'facility/facility.html')


#def test(request):
    #response=requests.post(place_details).json()
    #return render(request, 'facility/facility.html', {'response':response})



    