from django.http import HttpResponse
from index.models import AppIndex
from django.shortcuts import render
from .forms import SympForm, EmergencyList
from .models import DiseaseList

# Create your views here.
def sympcheck(request):
    form = SympForm
    emform = EmergencyList
    

    context= {
        'form':form,
        'emform':emform
        }
    return render(request, 'symp/sympcheck.html', context)

def evaluation(request):
    return render(request, 'symp/evaluation.html')

#def dialogue(request):
    