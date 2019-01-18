# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:47:19 2019

@author: levik
"""

#importing necessary libraries

import urllib.request
import json
from requests import get
from math import radians, sin, cos, sqrt, asin



#obtaining ISS location info
req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
response = urllib.request.urlopen(req)


#reading info and defining dictionary with info
iss_location = json.loads(response.read())



#obtaining IP address
ip = get('https://api.ipify.org').text

#defining ISS Lat/Long variables
ISS_lat = (iss_location['iss_position']['latitude'])
ISS_long = (iss_location['iss_position']['longitude'])

print("the ISS is located at Latitude "+ISS_lat+" and Longitude "+ISS_long)
print("\n")


#defining URL for location API
ipurl = 'http://api.ipstack.com/'+ip+'?access_key=8f55a29a90e2a665cd50a73057988b64'

#defining and reading Location info from API
IPlocation = urllib.request.urlopen(ipurl)
json_string = IPlocation.read()
IPlocation.close()

#Creating location dictionary/defining laction lat/long variables
location = json.loads(json_string)
location_lat = location['latitude']
location_long = location['longitude']
location_country = location['country_name']

print("you are located at Latitude ",location_lat," and Longitude ",location_long)
print("\n")

#define constant of earth radius
earth_radius = 3959

#defininf the difference in radians of latitudes and longitudes
latdiff = radians(float(location_lat)-float(ISS_lat))
longdiff = radians(float(location_long)-float(ISS_long))


#defining lat and long in radians
lat1 = radians(float(ISS_lat))
lat2 = radians(float(location_lat))

#defining haversine and center angle equations
haversine= sin(latdiff/2)**2 + cos(lat1)*cos(lat2)*sin(longdiff/2)**2
centerangle= 2*asin(sqrt(haversine))

#determining distance value +240 for distance above earth
distance = (earth_radius*centerangle)+240
print("You are about",round(distance,2), "miles away from the ISS!")
