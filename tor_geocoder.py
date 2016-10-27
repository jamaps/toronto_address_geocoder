# geolocates addresses from a csv table using
# a custom address table built from trim_address_file.py

# this example geocodes Toronto's open business license dataset

import csv
import time

start_time = time.time()

# csv file that is ripe for geocoding
in_csv = 'business_licenses/business_trim.csv'

# address file from trim_address_file.py
add_in = 'address_points/address_trim.csv'

# read in input address table
address_table = []
with open(add_in, 'r') as csvadd:
    reader = csv.reader(csvadd)
    # grab header
    # ['number', 'street', 'upper', 'X', 'Y', 'class']
    for row in reader:
        a_header = row
        print a_header
        break
    # append to address_table
    for row in reader:
        if row != a_header:
            address_table.append(row)

# output tables and headers
# the headers were grabbed the csv tables
# plus adding in new fields for X, Y, and address class

out_good_header = ['Category', 'Licence No.', 'Operating Name', 'Issued', 'Client Name', 'Business Phone', 'Business Phone Ext.', 'Licence Address Line 1', 'Licence Address Line 2', 'Licence Address Line 3', 'Conditions', 'Free Form Conditions Line 1', 'Free Form Conditions Line 2', 'Plate No.', 'Endorsements', 'Cancel Date','X','Y','Address Class']

address_out_good = []
address_out_good.append(out_good_header)

out_bad_header = ['Category', 'Licence No.', 'Operating Name', 'Issued', 'Client Name', 'Business Phone', 'Business Phone Ext.', 'Licence Address Line 1', 'Licence Address Line 2', 'Licence Address Line 3', 'Conditions', 'Free Form Conditions Line 1', 'Free Form Conditions Line 2', 'Plate No.', 'Endorsements', 'Cancel Date']

address_out_bad = []
address_out_bad.append(out_bad_header)

# lets open up what needs to be geocoded ...
with open(in_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)

    # grab header and print it
    for row in reader:
        header = row
        print header
        break

    # try to match addresses - loop through each row
    good = 0 # counter of those that work
    q = 0 # total couner
    for row in reader:
        if row != header:

            # input address name
            # needs to be customized depending on input data
            address_in = row[2].split(',')[0]

            for address in address_table:
                if address_in == address[2]:
                    good += 1
                    geocoded = 1

                    # add in X, Y, and class to row
                    out_row = row + [address[3],address[4],address[5]]
                    address_out_good.append(out_row)

                    break

                else:
                    geocoded = 0

            if geocoded == 0:
                address_out_bad.append(row)
                print address_in


        q += 1

        # code in break if needed
        # if q == 500:
        #     break


# output good and bad results to table - success rate of 95% from testing

out_csv_good = 'business_licenses/business_coded_tor_add.csv'
out_csv_bad = 'business_licenses/business_still_need.csv'

with open(out_csv_good, 'w') as csvw:
    writer = csv.writer(csvw)
    for row in address_out_good:
        writer.writerow(row)

with open(out_csv_bad, 'w') as csvw:
    writer = csv.writer(csvw)
    for row in address_out_bad:
        writer.writerow(row)

# print good over total
print good
print q

# and print the elapsed time
print '[]' * 14
print time.time() - start_time
