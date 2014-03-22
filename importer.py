"""
This python script seeds the empty MongoDB database with information from the raw JSON file.
"""

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect
from models import Film_Location
#----------------------------------------
# Database Configuration
#----------------------------------------
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)
DB_NAME = 'film_location'
app.config["MONGODB_DB"] = DB_NAME
connect(DB_NAME, host="mongodb://localhost/film_location")
db = MongoEngine(app)

#----------------------------------------
# Load database with values from JSON file.
#----------------------------------------
def load_db():
    with open("SF_films.json") as f:
        read_data = f.read()
    f.closed

    all_data = eval(read_data)
    for film_data in all_data:
        try:
            # check for existence of 2 most important attributes: movie title and film location
            if "locations" in film_data and "title" in film_data:
                new_film_data = Film_Location(title=film_data["title"],
                                                location=film_data["locations"]
                                                )
                # Do checks on rest of JSON data to see if JSON dictionary key exists before placing as attribute in document.
                rest_of_fields = ["release_year", "production_company", "director", "writer",
                                        "actor1","actor2","actor3"]
                for field in rest_of_fields:
                    if field in film_data:
                        new_film_data.field = film_data[field]
            new_film_data.save()
        except:
            print "KEY error!"

load_db()
