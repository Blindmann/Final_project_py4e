# Weather Forecast Anywhere using SQLite3 database #

This is the repository for my final project of the [Python 4 Everybody](https://www.coursera.org/learn/python-data-visualization) course on Coursera (Capstone).

This set of programs could be used to predict weather anywhere on the planet and save this forecast for analysis and visualization (here using the D3.js JavaScript library), much like a weather station would do. 

## Folder structure #

- In the **Nominatim** folder, I used _two APIs_ from Open street map:

  * the [search API](https://nominatim.org/release-docs/latest/api/Search/) gives the latitude and longitude for a given address (_Nominatim_search.py_),
  * the [reverse API](https://nominatim.org/release-docs/latest/api/Reverse/) allows to find the address for a given latitude and longitude (_Nominatim_reverse.py_).
  
  > *This Nominatim folder could be useful if chosing another data source than me.*

- In the **Yr_no** folder can be found the main content of my final project, where I:
    1) used the **first** _acinn_parser.py_ program in order to parse the [website of the department of Atmospheric and Cryospheric Sciences](https://acinn-data.uibk.ac.at/) at the University of Innsbruck. That way, I could retrieve data about several weather stations accessible at different webpages from the source url. For the pages that were formatted in the same way, I could retrieve (for Europe) the latitude and longitude of each weather station (open source data).
    2) used the **second** program _yrno_modified.py_ in order to use these retrieved latitude longitude values for each weather stations and to predict the weather at these locations (using the [LocationForecast API](https://developer.yr.no/doc/locationforecast/HowTO/)).

       N.B.: Both the parser and the yrno_modified.py program use the same **_SQLite3 database_** that they contribute on building (the yrno_modified.py program adds a table to the **weatherstations.sqlite database** in order to save the forecast data).


## Additional informations for practical use #

### Simple workflow without storing the data in a SQLite3 database ###

  1) If you would like to test this program (and to understand my thought process), then I would recommend to first use the _Nominatim_search.py_ in order to retrieve the lat and long for an address that interests you.
  2) Then I would go on and use the _yrno.py_ unmodified simple program to predict the weather for this location: user is prompted for lat and long and then provided with an output as a json file for this location.

### Add your own locations of interest ###

  * If parsing a website and interested about weather forecast for other locations, don't hesitate to contribute and create another parser program. 

  * Include the latitude and longitude of the parsed location as demonstrated in the acinn_parser.py program in order to save these in the weatherstations.sqlite database. If only the names or the addresses could be found, then that would be an opportunity to use the Nominatim program in combination with the parser for the newly retrieved locations. 

### More informations to help choose locations with this particular combination of APIs ###

  * The idea with using already known weather stations with free access data could be to compare the forecast (prediction) versus the reality (record). Also, sometimes it may allow for interpolation if weather instruments break. The [Norwegian Meteorological Institute](https://www.yr.no/en) is known to use trustful algorithms to predict weather and the LocationForecast API that was used is free to use and uses my Coursera profile as user-agent of the request. [Open street map](https://www.openstreetmap.org/) has a set of different APIs that are available and can be modified as well, in order to find more information about retrieved locations and to make them compatible with the LocationForecast API of the Norwegian Meteorological Institute (which uses lat long). 

## Visualization #

Here analysis and visualizations provided are simple and use the program gline.js inspired by the Python for Everybody specialization taught by [Dr. Chuck Charles Severance](https://online.dr-chuck.com/) on Coursera. The latest version of the **gline2.py** provided a visualization of the average temperature per timestep and through time (the timeframe of the forecast) at all the weather stations in Austria. Don't forget to use the gline.htm after running the gline program to open a window in the browser and visualize the data!

It is possible to change this program to view the precipitations instead or to trace a separate curve for each weather station in order to compare the weather at different locations for the same time period.
