# Final_project_py4e
This is the repository for my final project of Python 4 Everybody course on Coursera (Capstone).

In the Nominatim folder, I used two APIs from Open street map, the search API gives the latitude and longitude for a given address, while the search API allows to find the address for a given latitude and longitude.
This Nominatim folder could be useful if chosing another data source than me.

In the Yr_no can be found my final project, where I first used the acinn_parser.py program in order to parse the website of the department of Atmospheric and Cryospheric Sciences at the University of Innsbruck in order to retrieve data about several weather stations accessible at different webpages. For the pages that were formatted in same way, I could retrieve (in Europe) the latitude and longitude of the weather station (open source data). I then went on and used the second program yrno_modified.py in order to use these retrieved lat. long. values for the weather stations and to predict the weather at these locations. Both the parser and the yrno_modified.py program use the same SQLite3 database that they contribute on building (the yrno_modified.py program adds a table to the weatherstations.sqlite database in order to save the forecast data).

If you would like to test this program (and to understand my thoughts process), then I would recommend to first use the nominatim search API in order to retrieve the lat and long for an address that interests you. Then I would go on and use the yr.no unmodified simple program to predict the weather for this location: user is prompted for lat and long and then provided with an output as a json file for this location.

If parsing a website and interested about weather forecast for other locations, don't hesitate to contribute and create another parser program. 

IF possible include the latitude and longitude of the parsed location as demonstrated in the acinn_parser.py program and save these in the weatherstations.sqlite database. If only the names of the address could be found, then that would be an opportunity to use the Nominatim parser for the newly retrieved locations. 

The idea with using already known weather stations with free access data is to compare the forecast (prediction) versus the reality (record). Also, sometimes it may allow for interpolation if weather instruments break. The Norwegian Meteorological Institute is known to use trustful algorithm to predict weather and the LocationForecast API that was used is free to use and uses my Coursera profile as user-agent of the request. 

This set of programs could be used to predict weather anywhere on the planet and save this forecast for analysis, much like a weather station would do. 

Here analysis and visualizations provided are simple and use the program gline.js inspired by the Python for Everybody specization. The latest version of the gline2.py provided a visualization of the average temperature per timestep and through time (the timeframe of the forecast) at all the weather stations in Austria. 
It is possible to change this program to view the precipitations instead or to trace a separate curve for each weather station in order to compare the weather at different locations for the same time period.
