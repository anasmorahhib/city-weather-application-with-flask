from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather

API_KEY = '930544485c67feef5f30989c07d4fa41'

def get_temperature (location={"lat": 31.630000 , "long": -8.008889}):
	# Synchronous way
	darksky = DarkSky(API_KEY)

	latitude = location['lat']
	longitude = location['long']
	forecast = darksky.get_forecast(
	    latitude, longitude,
	    extend=False, # default `False`
	    lang=languages.ENGLISH, # default `ENGLISH`
	    units=units.AUTO, # default `auto`
	    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
	)
	return forecast.currently.temperature

