import os
from flask import Flask, render_template, send_from_directory, redirect, request, session, url_for

#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)

app.config.update(
    DEBUG = True,
)

#----------------------------------------
# controllers
#----------------------------------------

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')

#----------------------------------------
# database
#----------------------------------------

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

def print_all_locations():
    for film_location in Film_Location.objects:
        print film_location.location
print_all_locations()
#----------------------------------------
# launch
#----------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    app.config["SECRET_KEY"] = "\xd5\x82\xb5\x8de|\xa3fN\xe3\xd8U\xa3\xdc\xe6\xb8\x81\x91\xdbU\x9e\xab\xdew"
