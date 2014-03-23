#Project chosen for this code challenge#
Plot SF Movie Locations on a Map

###Task###
Create a service that shows on a map where movies have been filmed in San Francisco. The user should be
able to filter the view using autocompletion search. The data is available on DataSF: Film Locations.

###The technical track you chose (full stack, back-end or front-end)###
I've decided to make a full-stack webapp, because I like to program in both Python and Javascript.

###Reasoning behind your technical choices (and level of experience with those)###
I decided to use MongoDB, because it is production-level and deployment friendly, easy-to-use noSQL storage system.
**Level of experience with MongoDB**: beginner.

I decided to do geo-encoding on the Python controller level code, because it is much simpler to do than with Javascript.
The urllib libraries are especially useful for doing GET requests to the maps APIs and for url encoding.
**Level of experience with Python**: proficient.

I decided to use the Google Maps API for both the map display, geo-coding, and autocompletion search, because
this is the most well-known map API that contains many features.
**Level of experience with Javascript**: proficient.

###A limitation in Javascript prevented me from implementing a more optiomal solution for creating HTML strings.###

You will notice that the infowindow pop-up that shows the place details is implemented as a string called `contentString`,
which is a string containing the HTML. The place details API method `InfoWindow` requires that the content of the
info window be a string. This is a rather strict technical requirement of the Javascript place details API. For better
readability, I would've used the jquery `append` method to create html elements one at a time. If I go down that
route, then the input paramters for `contentString` would then be an object instead of the required string input type
that the Google Maps API requires.

Javascript lacks an in-built convenience method to cast an object to a string, unfortunately.

###Trade-offs you might have made, anything you left out, or what you might do differently if you were to spend
additional time on the project###
There is only 1 collection in `models.py`. If I had more time, I would organize `models.py` to have >1
collection such as "Movies", "Locations", and "Actors", which are interconnected collections. This would make the filtering
process faster on the front-end. I would have filter settings on the front-end for "Movies", "Locations", and "Actors",
in which the search results come from three different db queries.

###Link to other code you're particularly proud of###
As a hobby, I've been contributing to three large Python-based open source projects. Below are my commits that have
landed on the master repositories of the following Python projects:

**Django the web framework**
https://github.com/django/django/commits/master?author=onceuponatimeforever

**OpenHatch.org**: Both UI/Javascript and Python work.
https://github.com/openhatch/oh-mainline/commits/master?author=onceuponatimeforever

**IPython notebook**: all UI work.
https://github.com/ipython/ipython/commits/master?author=onceuponatimeforever

###Link to your resume or public profile###
http://www.linkedin.com/pub/susan-tan/21/484/317