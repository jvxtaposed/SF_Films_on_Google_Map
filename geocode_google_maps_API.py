import urllib2
import urllib

raw_address_dict = {"address":"Twin Peaks"}
encoded_address= urllib.urlencode(raw_address_dict)
url="http://maps.googleapis.com/maps/api/geocode/json?"+encoded_address+"&sensor=false"
response = urllib2.urlopen(url)
jsongeocode = eval(response.read())
print jsongeocode["results"][0]["geometry"]["location"]
