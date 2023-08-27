import urllib.request, urllib.parse, urllib.error
import json
import ssl

form = False

if form is False:
    form = 'json'
    serviceurl = 'https://nominatim.openstreetmap.org/search?'
else: 
    serviceurl = 'https://nominatim.openstreetmap.org/search?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    location = input('Enter location in freeform: ')
    if len(location) < 1: break

    parms = dict()
    parms['q'] = location
    if form is not False: parms['format'] = form
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    js = json.loads(data)
    #print(json.dumps(js, indent=4)) #:print the json
    
    place_id = js[0]["place_id"]
    lat = js[0]["lat"]
    lng = js[0]["lon"]
    print("Place id", place_id)
    print('lat', lat, 'lng', lng)