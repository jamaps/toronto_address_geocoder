###  Toronto Address Geocoder

A custom geocoder that computes points from address strings for Toronto. Written in Python using the City of Toronto's open dataset of [address points](http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=91415f9cd70bb210VgnVCM1000003dd60f89RCRD&vgnextchannel=1a66e03bb8d1e310VgnVCM10000071d60f89RCRD). This was written to quickly batch geocode large datasets (over 10,000) which would be too time intensive (or time out!) via web geocoding APIs.

**trim_address_points.py** takes the original dataset from the City (see link above) and wrangles it to be more apt for geocoding.

**tor_geocoder.py** uses the new address.csv for geocoding addresses in another csv. The output is the same as the input csv but with new fields for X, Y, and land class (residential, commercial, etc.)

**tor_geocoder_permits** is a modification of the above file to geocode the ~450,000 building permits that have been issued in Toronto since 2001.

**web_geocoder** is a simple web geocoder which can be used for the odd instances where an address fails to geocode. It geocodes the remaining points.csv using geopy
