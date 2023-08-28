import urllib.request, urllib.parse, urllib.error
import json
import ssl
import requests
import sqlite3

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
    
    """store relevant data in semi-permanent storage"""
    
    time = list()
    for x in js["properties"]["timeseries"][0:55]:
        time.append(x["time"])
    #print(time)
    temperature = list()
    for y in js["properties"]["timeseries"][0:55]:
        temperature.append(y["data"]["instant"]["details"]["air_temperature"])
    #print(temperature)
    precipitation = list()
    for p in js["properties"]["timeseries"][0:55]:
        precipitation.append(p["data"]["next_1_hours"]["details"]["precipitation_amount"])
    #print(precipitation)
    
    weather = [{'time':tim, 'temperature': temp, 'precipitation': precip}
        for tim, temp, precip in zip(time, temperature, precipitation)
       ]
    
    #print(weather)