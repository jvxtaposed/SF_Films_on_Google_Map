from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
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
connect(DB_NAME, host="mongodb://localhost/film_location")
db = MongoEngine(app)

#----------------------------------------
# Define classes below.
#----------------------------------------
class Film_Location(db.Document):
    title = db.StringField(max_length=1000, required=True)
    release_year = db.IntField(min_value=1900, max_value=3000, required=False)
    location = db.StringField(max_length=1000, required=True)
    production_company = db.StringField(max_length=200, required=False)
    director = db.StringField(max_length=1000, required=False)
    writer = db.StringField(max_length=1000, required=False)
    actor1 = db.StringField(max_length=1000, required=False)
    actor2 = db.StringField(max_length=1000, required=False)
    actor3 = db.StringField(max_length=1000, required=False)
    fun_facts = db.StringField(max_length=1000, required=False)
