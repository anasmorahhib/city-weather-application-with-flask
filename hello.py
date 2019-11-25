from wiki import get_city_info
from weather import get_temperature
from geo import get_location
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    title = "Homepage"	
    return render_template("index.html", title=title, location = get_location(), temperature = get_temperature(), city_info = get_city_info())

@app.route("/get-weather", methods=['POST'])
def get_weather():
	if request.method == 'POST':
		data = request.json
		location = get_location(data['city'])
		return {'temperature': get_temperature(location), 'wiki': get_city_info(data['city'])}