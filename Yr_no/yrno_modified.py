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

conn = sqlite3.connect('weatherstations.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Forecast
    (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    stations_id INTEGER, 
    temperature FLOAT, precipitation FLOAT,
     date TEXT)''')

count = 0

cur.execute('SELECT max(id) FROM Stations')
maxid = cur.fetchone()
maxid = maxid[0]
print(maxid)

stat = list()
time = list()
temperature = list()
precipitation = list()

while count < maxid :
    
    cur.execute('SELECT * FROM Stations')
    
    for row in cur:
        count = count + 1
        stations_id = row[0]
        lat = row[2]
        lon = row[3]

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
        #count = count + 1
    
        js = json.loads(result)
        #print(json.dumps(js, indent=4)) #:print the json
    
        """store relevant data in semi-permanent storage"""
    
        
        for x in js["properties"]["timeseries"][0:55]:
            time.append(x["time"])
            stat.append(stations_id)
        #print(time)
        #
        for y in js["properties"]["timeseries"][0:55]:
            temperature.append(int(y["data"]["instant"]["details"]["air_temperature"]))
        #print(temperature)
        #
        for p in js["properties"]["timeseries"][0:55]:
            precipitation.append(int(p["data"]["next_1_hours"]["details"]["precipitation_amount"]))
        #print(precipitation)
    
        weather = [{'station_id': sta, 'time':tim, 'temperature': temp, 'precipitation': precip}
            for sta, tim, temp, precip in zip(stat, time, temperature, precipitation)
        ]
        
    #print(weather)
        
for entry in weather:
    
    station_id = entry['station_id']
    date = entry['time']
    temperature = entry['temperature']
    precipitation = entry['precipitation']
    
    #print((station_id, date, temperature, precipitation))
            
    cur.execute('''INSERT OR REPLACE INTO Forecast
    (stations_id, temperature, precipitation, date) VALUES ( ? , ? , ? , ? )''',
        ( station_id, temperature, precipitation, date ) )
    
    conn.commit()
            
        # [ 
        #   { 'time': '2023-08-29T11:00:00Z', 'temperature': 10.0, 'precipitation': 0.3    }, 
        #   { 'time': '2023-08-29T12:00:00Z', 'temperature': 10.5, 'precipitation': 0.1    },
        
    
#for entry in weather:

    #date = entry['time']
    #temperature = entry['temperature']
    #precipitation = entry['precipitation']

    #print((date, temperature, precipitation))
    
    #cur.execute('''SELECT stations_id FROM Forecast)''')
    
    #for row in cur:
        
        #cur.execute('''INSERT OR REPLACE INTO Forecast
                #(temperature, precipitation, date) VALUES ( ? , ? , ? )''',
                #( temperature, precipitation, date ) )