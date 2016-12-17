# geocodes via web APIs

import csv
import os
import time
from geopy.geocoders import GoogleV3
from geopy.geocoders import Nominatim

# input csv dir/name.csvs
csv_in = 'building_permits/min_bad.csv'

# output csv dir/name.csv
csv_out = 'building_permits/min_good.csv'
csv_out_fail = 'building_permits/min_bad_still.csv'


# name of geocoding service
geolocator_G = GoogleV3()
geolocator_N = Nominatim()

# outputs
out_table = []
fail_table = []

with open(csv_in, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        header = row
        break
    counter = 0
    for row in reader:
        if row != header:
            # first try nominatum
            try:
                address = row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3] + ', Toronto, ON'
                print address
                time.sleep(1)
                location = geolocator_N.geocode(address, timeout=60)
                lat = location.latitude
                lon = location.longitude
                print lon, lat
                out_row = row + [lon,lat]
                out_table.append(out_row)
            # then try google
            except:
                try:
                    address = row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3] + ', Toronto, ON'
                    print address
                    time.sleep(1)
                    location = geolocator_G.geocode(address, timeout=60)
                    lat = location.latitude
                    lon = location.longitude
                    print lon, lat
                    out_row = rofw + [lon,lat]
                    out_table.append(out_row)
                except:
                    print 'FAIL'
                    fail_table.append(row)

            counter += 1
            print counter


#write outputs to file

with open(csv_out, 'w') as csvw:
    writer = csv.writer(csvw)
    for row in out_table:
        writer.writerow(row)


with open(csv_out_fail, 'w') as csvw:
    writer = csv.writer(csvw)
    for row in fail_table:
        writer.writerow(row)

# print those that fail
print len(fail_table)
