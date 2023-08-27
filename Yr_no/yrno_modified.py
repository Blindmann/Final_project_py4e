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
    
    """store the data in semi-permanent storage"""
    
    time = list()
    for x in js["properties"]["timeseries"][0:87]:
        time.append(x["time"])
    print(time)
            
    #print(time)
    #time = js["properties"]["timeseries"][0]["time"]
    #temperature = js["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]
    #precipitation = js["properties"]["timeseries"][0]["data"]["next_1_hours"]["details"]["precipitation_amount"]
    #time_1 = js["properties"]["timeseries"][6]["time"]
    #temperature_1 = js["properties"]["timeseries"][6]["data"]["instant"]["details"]["air_temperature"]
    #precipitation_1 = js["properties"]["timeseries"][6]["data"]["next_1_hours"]["details"]["precipitation_amount"]
    #time_2 = js["properties"]["timeseries"][12]["time"]
    #temperature_2 = js["properties"]["timeseries"][12]["data"]["instant"]["details"]["air_temperature"]
    #precipitation_2 = js["properties"]["timeseries"][12]["data"]["next_1_hours"]["details"]["precipitation_amount"]
    #time_3 = js["properties"]["timeseries"][18]["time"]
    #temperature_3 = js["properties"]["timeseries"][18]["data"]["instant"]["details"]["air_temperature"]
    #precipitation_3 = js["properties"]["timeseries"][18]["data"]["next_1_hours"]["details"]["precipitation_amount"]
    #print("Time: ", time, "temperature: ", temperature, "Precipitation amount: ", precipitation)
    #print("Time: ", time_1, "temperature: ", temperature_1, "Precipitation amount: ", precipitation_1)
    #print("Time: ", time_2, "temperature: ", temperature_2, "Precipitation amount: ", precipitation_2)
    #print("Time: ", time_3, "temperature: ", temperature_3, "Precipitation amount: ", precipitation_3)
    
    #weather['time'] = time
    #weather['temperature'] = temperature
    #weather['precipitation'] = precipitation
    #print(weather)