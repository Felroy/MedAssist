from django.http import HttpResponse
from index.models import AppIndex
from django.shortcuts import render


# Create your views here.
def facilitylocator(request):
    app3 = AppIndex.objects.get(pk=3)   
    return render(request, 'facility/facility.html')


    