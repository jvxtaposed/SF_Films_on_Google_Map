"""
This python script seeds the empty MongoDB database with information from the raw JSON file.
This script only gets invoked once on the Python terminal locally.
"""

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect
from models import Film_Location

# Libraries used for geocoding the string location text
import urllib2
import urllib
import json
#----------------------------------------
# Database Configuration
#----------------------------------------
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)
DB_NAME = 'film_location'
app.config["MONGODB_DB"] = DB_NAME
DB_USERNAME = "susan"
DB_PASSWORD = "susan"
DB_HOST_ADDRESS = "ds031098.mongolab.com:31098/film_location"
try:
    connect(DB_NAME, host='mongodb://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST_ADDRESS)
    db = MongoEngine(app)
except:
    print "ERROR: Connection to MongoDB hosted on MangoLab.com has failed!"
    raise
#----------------------------------------
# Load database with values from JSON file.
#----------------------------------------
def geocode(nongeocoded_location):
    """
    Convert a string text of the location (ie:'Twin Peaks') into its associated latitude and longitude float types.
    Do geocode first as part of the pre-processing of input JSON location text data before storing latitude
    and longitude into the db.
    """
    raw_address_dict = {"address": nongeocoded_location}
    encoded_address = urllib.urlencode(raw_address_dict)
    url="http://maps.googleapis.com/maps/api/geocode/json?"+encoded_address+"&sensor=false"
    response = urllib2.urlopen(url)
    # Convert the JSON string-type response into JSON format.
    jsongeocode = json.loads(response.read())
    if jsongeocode["results"]!=[]:
        latitude = jsongeocode["results"][0]["geometry"]["location"]["lat"]
        longitude = jsongeocode["results"][0]["geometry"]["location"]["lng"]
        return latitude, longitude
    else:
        # No results came from the API. Return function asap with arbitrary -1 values to store later into db.
        return -1,-1

def load_db():
    with open("SF_films.json") as f:
        read_data = f.read()
    f.closed

    all_data = eval(read_data)
    # Iterate through all dictionary items in the list. Each dictinary item contains keys such as "title","locations",
    # "release year", "production_company", "director", "writer"
    for film_data in all_data:
        # check for existence of 2 most important attributes: movie title and film location
        if "locations" in film_data and "title" in film_data:
            new_film_data = Film_Location(title=film_data["title"],
                                            location=film_data["locations"]
                                            )
            latitude, longitude = geocode(film_data["locations"])
            print latitude, longitude
            new_film_data.latitude = latitude
            new_film_data.longitude = longitude
            # Do checks on rest of JSON data to see if JSON dictionary key exists before setting object's new attribute.
            if "release_year" in film_data:
                new_film_data.release_year = film_data["release_year"]
            if "production_company" in film_data:
                new_film_data.production_company = film_data["production_company"]
            if "director" in film_data:
                new_film_data.director = film_data["director"]
            if "writer" in film_data:
                new_film_data.writer = film_data["writer"]
            if "actor_1" in film_data:
                new_film_data.actor_1 = film_data["actor_1"]
            if "actor_2" in film_data:
                new_film_data.actor_2 = film_data["actor_2"]
            if "actor_3" in film_data:
                new_film_data.actor_3 = film_data["actor_3"]
            new_film_data.save()

    for film_location in Film_Location.objects:
        print film_location.title
load_db()
