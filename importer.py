from flask import Flask
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect
#----------------------------------------
# initialization
#----------------------------------------
app = Flask(__name__)

#----------------------------------------
# database
#----------------------------------------
DB_NAME = 'film_location'
DB_USERNAME = 'susan'
DB_PASSWORD = 'susan'
DB_HOST_ADDRESS = 'ds031098.mongolab.com:31098/film_location'

app.config["MONGODB_DB"] = DB_NAME
connect(DB_NAME, host='mongodb://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST_ADDRESS)
db = MongoEngine(app)
from mongoengine import connect
from flask.ext.mongoengine import MongoEngine

DB_NAME = 'film_location'
DB_USERNAME = 'ArcTanSusan'
DB_PASSWORD = 'area51'
DB_HOST_ADDRESS = 'ds031098.mongolab.com:31098/film_location'

app.config["MONGODB_DB"] = DB_NAME
connect(DB_NAME, host="mongodb://localhost/film_location")
# connect(DB_NAME, host='mongodb://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST_ADDRESS)
db = MongoEngine(app)

class Film_Location(db.Document):
    title = db.StringField(max_length=200, required=True)
    release_year = db.IntField(min_value=1900, max_value=3000, required=True)
    location = db.StringField(max_length=200, required=True)
    production_company = db.StringField(max_length=200, required=True)
    director = db.StringField(max_length=200, required=True)
    writer = db.StringField(max_length=200, required=True)
    actor1 = db.StringField(max_length=200, required=True)
    actor2 = db.StringField(max_length=200, required=True)
    actor3 = db.StringField(max_length=200, required=True)

def load_db():
    with open("SF_films.json") as f:
        read_data = f.read()
    f.closed

    all_data = eval(read_data)
    for film_location in all_data:
        try:
            # check for existence of movie title and film location
            if  film_location["locations"] and film_location["title"]:
                new_film_location = Film_Location(title=film_location["title"],
                                                release_year=film_location["release_year"],
                                                location=film_location["locations"],
                                                production_company=film_location["production_company"],
                                                director=film_location["director"],
                                                writer=film_location["writer"],
                                                actor1=film_location["actor_1"],
                                                actor2=film_location["actor_2"],
                                                actor3=film_location["actor_3"]
                                                )
            new_film_location.save()
        except:
            print "KEY error!"

load_db()