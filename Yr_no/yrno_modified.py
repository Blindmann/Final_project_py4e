import urllib.request, urllib.parse, urllib.error
import json
import ssl
import requests

sitename = 'https://www.coursera.org/user/48cb508b6a8c58da3c105301dd5f79cb'

serviceurl = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    lat = input('Enter latitude: ')
    lon = input('Enter longitude: ')
    if len(lat) < 1 or len(lon) < 1: break

    parms = dict()
    parms['lat'] = lat
    parms['lon'] = lon
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)

    headers = {'user-agent': sitename}

    r = requests.get(url, headers=headers)
    
    if r.status_code != 200 :
        print("Error code=", r.status_code, url)
        break
    print (r.status_code)
    print (r.headers['content-type'])
    print ("Expires", r.headers['expires'])
    print ("Last modified", r.headers['last-modified'])
    
    result = r.text
    
    js = json.loads(result)
    #print(json.dumps(js, indent=4)) #:print the json
    
    
    