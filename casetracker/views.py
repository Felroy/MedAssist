from django.http import HttpResponse
from index.models import AppIndex
from django.shortcuts import render
import os
import folium
import pandas as pd  
import geopandas as gpd
import fiona
from shapely import speedups

speedups.disable()


# Create your views here.
def localcasetracker(request):
    boroughs = os.path.join(os.path.dirname(os.path.dirname(__file__)),'london_boroughs.json')
    cases =  os.path.join(os.path.dirname(os.path.dirname(__file__)),'nhse_weekly_vaccines_london_ltla.csv')
    boroughs_cases = pd.read_csv(cases)
    #london = 'D:\health\LondonBoundary\ESRI\London_Borough_Excluding_MHW.shp'
    #mergeDF = gpd.read_file(london)
    # ERROR AREA HERE # mergeDF=mergeDF[['name', 'geometry']]

    #geoj=pd.read_csv('geojson.csv')
    #finalmerge=mergeDF.merge(geoj,on="name")

    map = folium.Map(location=[51.528308,-0.3817686], zoom_start=12) 
    vaccines = folium.Choropleth(
        geo_data=boroughs,
        name='Vaccines',
        data=boroughs_cases,
        columns=['name', 'vaccines'],
        key_on='feature.properties.name',
        fill_color='YlGn',
        fill_opacity=0.4,
        line_opacity=0.5,
        legend_name='Vaccines registered as of 21-02-2021',
        show=True ,      
    ).add_to(map)
    
    #style_function = lambda x: {'fillColor': '#ffffff', 
    #                        'color':'#000000', 
    #                        'fillOpacity': 0.1, 
    #                        'weight': 0.1}
    #highlight_function = lambda x: {'fillColor': '#000000', 
     #                           'color':'#000000', 
    #                            'fillOpacity': 0.50, 
    #                            'weight': 0.1}
    #NIL = folium.features.GeoJson(
    #finalmerge,
    #finalmerge.head(3),
    #style_function=style_function, 
    #control=False,
    #highlight_function=highlight_function, 
    #tooltip=folium.features.GeoJsonTooltip(
     #   fields=['name'],
     #   aliases=['name'],
      #  style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    #)
    #)
    #map.add_child(NIL)



    #borough_properties = folium.GeoJson(
     #   boroughs_cases,
    #    tooltip=folium.GeoJsonTooltip(
     #       fields=['name'],
    #       aliases=['name'],
    #        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    #    )
    #)
    #map.add_child(borough_properties)
    pop = folium.Choropleth(
        geo_data=boroughs,
        name='Population vaccinated',
        data=boroughs_cases,
        columns=['name', 'population'],
        key_on='feature.properties.name',
        fill_color='YlOrRd',
        fill_opacity=0.4,
        line_opacity=0.5,
        legend_name='Population registered as of 21-02-2021',
        show= False,       
    ).add_to(map)

    
    folium.LayerControl().add_to(map)
    map=map._repr_html_()
    return render(request, 'casetracker/casetracker.html', {'casemap' : map})


    