import sqlite3
import time
import zlib

conn = sqlite3.connect('weatherstations.sqlite')
cur = conn.cursor()

cur.execute('SELECT id, Name FROM Stations')
names = dict()
for row in cur :
    names[row[0]] = row[1]

cur.execute('SELECT id, stations_id, temperature, precipitation, date FROM Forecast')
forecasts = dict()
for forecast_row in cur :
    forecasts[forecast_row[0]] = (forecast_row[1],forecast_row[2],forecast_row[3],forecast_row[4])
print("Loaded forecasts=",len(forecasts),"names=",len(names))

#This part allows us to see how many forecasts are available for each station and store this info in a dictionary, here 55 forecasts were created for each station.

#Next (if working more on the project), it could be interesting to see how many forecasts per hour are given.

stations = dict()

for (forecast_id, forecast) in list(forecasts.items()):
    name = forecast[0]
    #print(name)
    pieces = names[name] 
    stations[pieces] = stations.get(pieces,0) + 1
    
# print(stations)


# pick all the weather stations

w_stat = sorted(stations, key=stations.get, reverse=True)
w_stat = w_stat[:]
print(w_stat)

    
TEMP = dict()
PREC = dict()
times = list()
temperatures = list()
precipitations = list()

#cur.execute('SELECT id, stations_id, temperature, precipitation, date FROM Forecast')
for (forecast_id, forecast) in list(forecasts.items()):
    name = forecast[0]
    pieces = names[name]
    time = forecast[3]
    temperature = forecast[1]
    precipitation = forecast[2]
    if time not in times : times.append(time)
    key = (time, pieces)
    TEMP[key] = temperature
    PREC[key] = precipitation

times.sort()

# pick the weather forecasts (temperature, precipitation) for each date and time


            
    
print (TEMP)
print (PREC)
#print (times)

fhand = open('gline.js','w')
fhand.write("gline = [ ['Times'")
for w in w_stat:
    fhand.write(",'"+w+"'")
fhand.write("]")

for time in times:
    fhand.write(",\n['"+time+"'")
    for w in w_stat:
        key = (time, w)
        val = TEMP.get(key,0)
        fhand.write(","+str(val))
    fhand.write("]");

fhand.write("\n];\n")
fhand.close()

print("Output written to gline.js")
print("Open gline.htm to visualize the data")
