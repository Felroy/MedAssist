from django.http import HttpResponse
from index.models import AppIndex
from django.shortcuts import render
import os
import folium
import pandas as pd  
import geopandas as gpd
import fiona
from shapely import speedups
from .models import Borough
from django.http import JsonResponse


speedups.disable()


# Create your views here.
def localcasetracker(request):
    boroughs = os.path.join(os.path.dirname(os.path.dirname(__file__)),'london_boroughs.json')
    cases =  os.path.join(os.path.dirname(os.path.dirname(__file__)),'nhse_weekly_vaccines_london_ltla.csv')
    boroughs_cases = pd.read_csv(cases)
    mergeDF = gpd.read_file(boroughs)


    #geoj=pd.read_csv('geojson.csv')
    finalmerge=mergeDF.merge(boroughs_cases,on="name")

    mapfigure= folium.Figure(width=1200, height=800)  
    map = folium.Map(location=[51.528308,-0.3817686], zoom_start=12).add_to(mapfigure)
    vaccines = folium.Choropleth(
        geo_data=boroughs,
        name='Vaccines',
        data=boroughs_cases,
        columns=['name', 'vaccines'],
        key_on='feature.properties.name',
        fill_color='YlGn',
        fill_opacity=0.4,
        line_opacity=0.5,
        legend_name='Vaccines registered between 08-12-2020 and 21-02-2021',
        show=True ,      
    ).add_to(map)
       
    pop = folium.Choropleth(
        geo_data=boroughs,
        name='Percentage of population vaccinated',
        data=boroughs_cases,
        columns=['name', 'percentstr'],
        key_on='feature.properties.name',
        fill_color='YlOrRd',
        fill_opacity=0.4,
        line_opacity=0.5,
        legend_name='Percentage of population vaccinated between 08-12-2020 and 21-02-2021',
        show= False,       
    ).add_to(map)
    style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}

    
    borough_properties = folium.GeoJson(
            finalmerge,
            style_function=style_function,
            highlight_function=highlight_function,
            control=False,
            tooltip=folium.GeoJsonTooltip(
                fields=['name', 'vaccines', 'percentstr'],
                aliases=['Borough:', 'Vaccines given:', 'Percentage of population vaccinated:'],
                style=("background-color: white; color: #333333;font-family: arial; font-size: 12px; padding: 10px;") 
            )
        )
    map.add_child(borough_properties)
    map.keep_in_front(borough_properties)
    
    folium.LayerControl().add_to(map)
    map=map._repr_html_()
    return render(request, 'casetracker/casetracker.html', {'casemap' : map})

def vaccinechart(request):
    labels=[]
    data=[]

    queryvalid = Borough.objects.values('borough_name', 'vaccines_given') 
    for item in queryvalid:
        labels.append(item['borough_name']) 
        data.append(item['vaccines_given'])

    return JsonResponse(data={
        'labels':labels,
        'data': data,
    })
    
   