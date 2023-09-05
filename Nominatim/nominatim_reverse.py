import urllib.request, urllib.parse, urllib.error
import json
import ssl

form = False

if form is False:
    form = 'json'
    serviceurl = 'https://nominatim.openstreetmap.org/reverse?'
else: 
    serviceurl = 'https://nominatim.openstreetmap.org/reverse?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    lat = input('Enter latitude: ')
    lon = input('Enter longitude: ')
    if len(lat) < 1 or len(lon) < 1: break

    parms = dict()
    if form is not False: parms['format'] = form
    parms['lat'] = lat
    parms['lon'] = lon
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    js = json.loads(data)
    #print(json.dumps(js, indent=4)) #:print the json
    
    place_id = js["place_id"]
    address = js["display_name"]
    print("Place id", place_id)
    print("Address", address)