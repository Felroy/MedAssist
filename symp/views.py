from django.http import HttpResponse
from index.models import AppIndex
from django.shortcuts import render
from .forms import SympForm



# Create your views here.
def sympcheck(request):
    form = SympForm
    return render(request, 'symp/sympcheck.html', {'form':form})

#def dialogue(request):
    