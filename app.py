import os
from flask import Flask, render_template, send_from_directory, redirect, request, session, url_for

#----------------------------------------
# initialization of Flask Application
#----------------------------------------

app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

#----------------------------------------
# Database Configuration
#----------------------------------------
from mongoengine import connect
from flask.ext.mongoengine import MongoEngine
from models import Film_Location

DB_NAME = 'film_location'
app.config["MONGODB_DB"] = DB_NAME
connect(DB_NAME, host="mongodb://localhost/film_location")
# connect(DB_NAME, host='mongodb://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST_ADDRESS)
db = MongoEngine(app)

#----------------------------------------
# Controllers
#----------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route("/drop")
def drop_collection():
    """Go to this url to drop the entire collection. Used only for dev testing on local server only."""
    Film_Location.drop_collection()
    return render_template('index.html',all_data={})

@app.route("/", methods=["GET","POST"])
def search_by_movie_title():
    """The single-page map webapp is rendered here. Display film data sorted by movie titles."""
    all_data = {}
    for film_location in Film_Location.objects:
        try:
            if film_location.title and film_location.location:
                # The film_location's title is already a key in the dictionary.
                if film_location.title in all_data:
                    all_data[film_location.title].append((film_location.location,str(film_location.latitude),str(film_location.longitude),str(film_location.actor_1),str(film_location.release_year)))
                # The film_location's title is not yet a key in the dictionary, so add the key-value pair.
                else:
                    all_data[film_location.title] = [(film_location.location,str(film_location.latitude),str(film_location.longitude),str(film_location.actor_1),str(film_location.release_year))]
        except:
            print "KEY error!"
            raise
    search_type = {}
    search_type["movie_search"] = "any random string here"
    return render_template('index.html', all_data=all_data, search_type=search_type)

@app.route("/display_location", methods=["GET","POST"])
def search_by_location():
    """Display film data sorted by non-geocoded locations."""
    all_data = {}
    for film_location in Film_Location.objects:
        try:
            if film_location.title and film_location.location:
                if film_location.title in all_data:
                    all_data[film_location.location].append(str(film_location.title))
                else:
                    all_data[film_location.location] = [str(film_location.title)]
        except:
            print "KEY error!"
            raise
    search_type = {}
    search_type["location_search"] ="any random string here"
    return render_template('display.html', all_data=all_data, search_type=search_type)
#----------------------------------------
# Launch the app locally on PORT 5000. Go to localhost:5000.
#----------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    app.config["SECRET_KEY"] = "\xd5\x82\xb5\x8de|\xa3fN\xe3\xd8U\xa3\xdc\xe6\xb8\x81\x91\xdbU\x9e\xab\xdew"
