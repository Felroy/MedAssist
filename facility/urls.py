from django.urls import path
from . import views

app_name = 'facilitylocator'
urlpatterns = [    
    path('', views.facilitylocator, name='facilitylocator'),
]
