from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="Weather")

def get_location(ville="Marrakech"):
	location = geolocator.geocode(ville)
	return {"lat": location.latitude, "long": location.longitude}

