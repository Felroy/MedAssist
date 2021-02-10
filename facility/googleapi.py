import googlemaps
import pprint

# API key, hardcoded value
api_key = 'AIzaSyCgKjRiMpRKAyJFlzEKch-32JpfEwRDOwg'

# 
locmap = googlemaps.Client(key = api_key)

# search query
places_search = locmap.places_nearby(location= '-33.8679522, 151.1037362', radius = 2000, type = 'cafe')



for search in places_search['results']:

    search_place_id = search['place_id']
    search_query = ['name', 'type', 'geometry/location']
  
    place_details = locmap.place(place_id = search_place_id, fields = search_query)
    

    