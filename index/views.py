from django.http import Http404
from django.shortcuts import render, redirect, reverse
from .models import AppIndex
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    app_list = AppIndex.objects.all()   
    return render(request, 'index/index.html', {'app_list':app_list})

def app_choice(request, app_id):
    try: 
        app = AppIndex.objects.get(pk=app_id)   
        
        if app_id == 1: 
            return HttpResponseRedirect('/symp/')
        elif app_id == 2:
            return HttpResponseRedirect('/casetracker/')
        elif app_id == 3: 
            return HttpResponseRedirect('/facility/')
    except AppIndex.DoesNotExist:
        raise Http404("Page does not exist, please go back to the site index")
    return render(request, 'index/errormsg.html', {'app':app})

