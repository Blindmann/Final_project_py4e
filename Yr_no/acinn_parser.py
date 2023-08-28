#This program should parse the open source weather stations data at https://acinn-data.uibk.ac.at/pages/station-list.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

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
    if s == "http://www.zamg.ac.at":
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
        lat.append(latitude)
    except:
        print("doesn't apply to this page", link)

    try:
        long_tags = soup.find('dl', class_="docutils").find('dt', string='Longitude:')
        longitude = long_tags.find_next_sibling('dd').string
        lng.append(longitude)
    except:
        print("doesn't apply to this page", link)
    #for tag in tags:
        #newtag = tag.contents[0]
    #lat.append(newtag)
    #print("===============================")
print(st)
print(lat)
print(lng)