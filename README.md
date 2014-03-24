#Project chosen for this code challenge#
Plot SF Movie Locations on a Map

###Task###
Create a service that shows on a map where movies have been filmed in San Francisco. The user should be
able to filter the view using autocompletion search. The data is available on DataSF: Film Locations.

### How to run this app locally on your computer###
0. Clone this github repo on the command line.
1. Make sure you have virtualenv installed. Then, create a virtualenv by`virtualenv <myEnvName> --no-site-packages`.
2. Enter your newly created virtualenv  by `source <myEnvName> bin/activate`.
3. Install all dependencies with `pip install -r requirements.txt`.
4.`python app.py` and go to the url: localhost:5000.

###The technical track you chose (full stack, back-end or front-end)###
I made a full-stack webapp, because I love to program in both Python and Javascript.

###Reasoning behind your technical choices (and level of experience with those)###
I decided to use Flask, because I was familiar with this Python microframework from making previous webapps.

**Level of experience with Flask**: proficient.

I decided to use MongoDB, because it is a production-level, deployment friendly, and easy-to-use noSQL storage system.

**Level of experience with MongoDB**: beginner.

I decided to do geo-encoding on the controller level, because it is much simpler to do in Python than with using Javascript.
The urllib libraries are especially useful for doing GET requests to the maps APIs and for url encoding.

**Level of experience with Python**: proficient.

I decided to use the Google Maps API for the map display, geo-coding, and autocompletion search, because
this is the most well-known map API that contains many features.

**Level of experience with Google Maps API**: beginner.
**Level of experience with Javascript**: proficient.

The purple ribbon at the top of the webapp comes from this source: http://css-tricks.com/snippets/css/ribbon/

###A limitation in Javascript prevented me from implementing a more optiomal solution for concatenating HTML strings.###

You will notice that the infowindow pop-up that shows the place details is implemented as a string called `content`,
which is a string containing the HTML. The place details API method `InfoWindow` requires that the content of the
info window be a string. This is a rather strict technical requirement of the Javascript place details API. For better
readability, I would've used the jquery `append` method to create html elements one at a time. If I go down that
route, then the input paramters for `content` would then be an object instead of the required string input type
that the Google Maps API requires. Javascript lacks an in-built convenience method to cast an object to a string, unfortunately.

###Trade-offs you might have made, anything you left out, or what you might do differently if you were to spend additional time on the project###

The biggest disadvantage of this single-page webapp is that the entire work is monolithic. Most of the page rendering
and the filtering is done by one Javascript `initialize` function. If I had more time, I would refactor the large JS
function into smaller Javascript functions so that the components would be easier to maintain and debug.

Of all the map APIs, I decided to use the Google Maps API was made because of its excellent and
extensive documentation and comprehensive ecosystem of map tools. I also used the out-of-the-box autocomplete
searchbox. However, the searchbox does autocompletion, making suggestions for `places` by default, rather than
making suggestions for auto-completing `movie titles`.

Google's geocoding API produced some inaccurate results. If you zoom out to see the entire USA map, you can see
that some locations were geocoded to the wrong states. Better pre-processing of the raw JSON data would've reduced
the number of geocoding inaccuracies.

The geo-coding was done just once on the server-side when the MongoDB database was initially seeded. Doing
geo-coding on the client-side would've been an unsound decision. If done on the client-side, then the daily
geo-coding API limit would have been exceeded very quickly every time that all the markers are loaded on the page.

I ran out of time to write up Python unittetests, sadly. If I had more time, I would've learned Jasmine for doing tests
on my Javascript code as well.

Since the app has a backend, if I had more time, I would make a bookmarking feature for users to login and then
bookmark their favorite film locations to visit later.

###Link to other code you're particularly proud of###
I'm a believer of working on open source as a way to learn more about the internals of a tool, get more familar with
a language, and build up software skills through code reviews. As a hobby over the past year, I've
been contributing to 3 large Python-based open source projects. Below are my commits that have landed on the
master repositories of the following Python projects:

**Django the web framework**: All in Python.
https://github.com/django/django/commits/master?author=onceuponatimeforever

**OpenHatch.org**: My contributions are in both Javascript and Python.
https://github.com/openhatch/oh-mainline/commits/master?author=onceuponatimeforever

**IPython notebook**: My contributions are all UI work in Javascript.
https://github.com/ipython/ipython/commits/master?author=onceuponatimeforever

###Link to your resume or public profile###
http://www.linkedin.com/pub/susan-tan/21/484/317
