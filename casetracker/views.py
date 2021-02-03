from django.http import HttpResponse
from index.models import AppIndex
from django.shortcuts import render


# Create your views here.
def localcasetracker(request):
    app2 = AppIndex.objects.get(pk=2)   
    return render(request, 'casetracker/casetracker.html')


    