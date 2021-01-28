from django.urls import path, re_path
from . import views

app_name = 'index'

urlpatterns = [   
    # / 
    path('', views.index, name='index'),

    # /idnumber/
    path('<int:app_id>/', views.app_choice, name='app_choice'),
]
