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

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/display", methods=["GET"])
def display_all_locations():
    """Display film data on new page /display."""
    all_data = {}
    for film_location  in Film_Location.objects:
        # Remove below line in final commit.
        # film_location.delete()
        try:
            if film_location.title and film_location.location:
                if film_location.title in all_data:
                    all_data[film_location.title].append(str(film_location.location))
                else:
                    all_data[film_location.title] = [str(film_location.location)]
        except:
            print "KEY error!"
    return render_template('display.html', all_data=all_data)
#----------------------------------------
# Launch the app locally on PORT 5000. Go to localhost:5000.
#----------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    app.config["SECRET_KEY"] = "\xd5\x82\xb5\x8de|\xa3fN\xe3\xd8U\xa3\xdc\xe6\xb8\x81\x91\xdbU\x9e\xab\xdew"
