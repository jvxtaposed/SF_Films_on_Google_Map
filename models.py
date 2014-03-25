from flask import Flask
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect

#----------------------------------------
# database configuration
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
# Define classes below.
#----------------------------------------
class Film_Location(db.Document):
    """The movie title, location, latitude, and longitude are required fields for the row to exist in db, because the 2
    most important attributes on the client side are the movie title and its filming locations."""
    title = db.StringField(max_length=1000, required=True)
    release_year = db.IntField(min_value=1900, max_value=3000, required=False)
    location = db.StringField(max_length=1000, required=True)
    latitude = db.FloatField(min_value=-1000, max_value=1000, required=True)
    longitude= db.FloatField(min_value=-1000, max_value=1000, required=True)
    production_company = db.StringField(max_length=200, required=False)
    director = db.StringField(max_length=1000, required=False)
    writer = db.StringField(max_length=1000, required=False)
    actor_1 = db.StringField(max_length=1000, required=False)
    actor_2 = db.StringField(max_length=1000, required=False)
    actor_3 = db.StringField(max_length=1000, required=False)
    fun_facts = db.StringField(max_length=1000, required=False)
