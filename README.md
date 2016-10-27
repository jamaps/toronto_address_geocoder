###  Toronto Address Geocoder

#### Jeff Allen, 2016

A custom geocoder that computes points from address strings for Toronto. Written in Python using the City of Toronto's open dataset of [address points](http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=91415f9cd70bb210VgnVCM1000003dd60f89RCRD&vgnextchannel=1a66e03bb8d1e310VgnVCM10000071d60f89RCRD)

trim_address_points.py takes the original dataset from the City (see link above) and wrangles it to be more apt for geocoding.

tor_geocoder.py uses the new address.csv for geocoding addresses in another csv. The output is the same as the imput csv but with new fields for X, Y, and land class (residential, commercial, etc.)
