from django.urls import path
from . import views


app_name = 'symp'
urlpatterns = [    
    path('', views.sympcheck, name='sympcheck'),
    path('evaluation/', views.evaluation, name='evaluation')
]

