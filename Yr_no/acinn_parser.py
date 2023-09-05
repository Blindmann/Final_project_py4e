#This program should parse the open source weather stations data at https://acinn-data.uibk.ac.at/pages/station-list.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import sqlite3
import re

conn = sqlite3.connect('weatherstations.sqlite')
cur = conn.cursor()

cur.executescript('''

CREATE TABLE IF NOT EXISTS Stations (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Name   TEXT UNIQUE,
    Lat    FLOAT,
    Long   FLOAT
)
''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

origin = "https://acinn-data.uibk.ac.at"
extension = '/pages/station-list.html'

url = origin + extension

print("Retrieving", url)

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags within the Europa section 

eurolines = soup.find(id="europe")
#print(type(eurolines))
tags = eurolines('a')
links = list()
for tag in tags:
    s = tag.get('href')
    if s == "http://www.zamg.ac.at" or s == "../pages/hatpro-uibk-met.html" or s == "../pages/patscherkofel-1.html" or s == "../pages/patscherkofel-2.html" or s == "../pages/patscherkofel-3.html" or s == "../pages/tawes-uibk.html" or s == "../pages/i-box-arbeserkogel.html" or s == "../pages/i-box-eggen.html" or s == "../pages/i-box-hochhaeuser.html" or s == "../pages/i-box-kolsass.html" or s == "../pages/i-box-terfens.html" or s == "../pages/i-box-turbibox.html" or s == "../pages/i-box-weerberg.html":
        continue
    links.append(s[2:])
howmany = len(links)
print(howmany, "links were retrieved of type", type(links))
#print(links)

st = list()
lat = list()
lng = list()

for link in links:
    html = urllib.request.urlopen(origin + link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    title_tags = soup('title')
    for station in title_tags :
        indiv = station.contents[0]
    st.append(indiv)
    try:
        lat_tags = soup.find('dl', class_="docutils").find('dt', string='Latitude:')
        latitude = lat_tags.find_next_sibling('dd').string
        lat.append(latitude[:5])
    except:
        print("doesn't apply to this page", link)

    try:
        long_tags = soup.find('dl', class_="docutils").find('dt', string='Longitude:')
        longitude = long_tags.find_next_sibling('dd').string
        lng.append(longitude[:5])
    except:
        print("doesn't apply to this page", link)
    #for tag in tags:
        #newtag = tag.contents[0]
    #lat.append(newtag)
    #print("===============================")
    
stations = [{'name':nam, 'latitude': lat, 'longitude': lng}
    for nam, lat, lng in zip(st, lat, lng)
    ]

# [ 
#   { 'name': 'Ellboegen', 'latitude': '47.1874777175', 'longitude': '11.4293137193' }, 
#   { 'name': 'Hintereisferner', 'latitude': '46.805769', 'longitude': '10.774416' },

for entry in stations:

    name = entry['name']
    latitude = entry['latitude']
    longitude = entry['longitude']

    print((name, latitude, longitude))
    
    cur.execute('''INSERT OR REPLACE INTO Stations
        (Name, Lat, Long) VALUES ( ?, ? , ? )''',
        ( name, latitude, longitude ) )
    
    conn.commit()