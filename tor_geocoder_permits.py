# geolocates addresses from a csv table using
# a custom address table built from trim_address_file.py

# this example geocodes Toronto's open business license dataset

import csv
import time

start_time = time.time()

# address file from trim_address_file.py
add_in = 'address_points/address_trim.csv'

# grab address data and put into a thingamajig
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

for address in address_table:
    if '66 FINCH AVE W' == address[2]:
        print "MEOW"



# grab building permits from 2001 to 2015

years = range(2001,2016)
# builiding permit header
header = ['PERMIT_NUM', 'REVISION_NUM', 'PERMIT_TYPE', 'STRUCTURE_TYPE', 'WORK', 'STREET_NUM', 'STREET_NAME', 'STREET_TYPE', 'STREET_DIRECTION', 'POSTAL', 'GEO_ID', 'WARD_GRID', 'APPLICATION_DATE', 'ISSUED_DATE', 'COMPLETED_DATE', 'STATUS', 'DESCRIPTION', 'CURRENT_USE', 'PROPOSED_USE', 'DWELLING_UNITS_CREATED', 'DWELLING_UNITS_LOST', 'EST_CONST_COST', 'ASSEMBLY', 'INSTITUTIONAL', 'RESIDENTIAL', 'BUSINESS_AND_PERSONAL_SERVICES', 'MERCANTILE', 'INDUSTRIAL', 'INTERIOR_ALTERATIONS', 'DEMOLITION']

all_permits = []
for year in years:
    csvname = 'building_permits/clearedpermits' + str(year) + '.csv'
    print csvname
    with open(csvname,'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row == header:
                print 'meow'
            else:
                all_permits.append(row)

print len(all_permits)


out_header = ['PERMIT_NUM', 'REVISION_NUM', 'PERMIT_TYPE', 'STRUCTURE_TYPE', 'WORK', 'STREET_NUM', 'STREET_NAME', 'STREET_TYPE', 'STREET_DIRECTION', 'POSTAL', 'GEO_ID', 'WARD_GRID', 'APPLICATION_DATE', 'ISSUED_DATE', 'COMPLETED_DATE', 'STATUS', 'DESCRIPTION', 'CURRENT_USE', 'PROPOSED_USE', 'DWELLING_UNITS_CREATED', 'DWELLING_UNITS_LOST', 'EST_CONST_COST', 'ASSEMBLY', 'INSTITUTIONAL', 'RESIDENTIAL', 'BUSINESS_AND_PERSONAL_SERVICES', 'MERCANTILE', 'INDUSTRIAL', 'INTERIOR_ALTERATIONS', 'DEMOLITION','X','Y','Address Class']

print "mooooooo"


address_out_good = []
address_out_bad = []
address_out_empty = []

# try to match addresses - loop through each row
empty = 0
good = 0 # counter of those that work
q = 0 # total couner
for row in all_permits:
    if row != header:

        # input address name
        # needs to be customized depending on input data
        address_in = row[5] + ' ' + row[6] + ' ' + row[7]
        print address_in

        for address in address_table:
            if address_in == address[2]:
                good += 1
                geocoded = 1

                # add in X, Y, and class to row
                out_row = row + [address[3],address[4],address[5]]
                address_out_good.append(out_row)
                # print 'good'

                break

            else:
                geocoded = 0

        # if shitty
        if geocoded == 0:

            if row[5] == '0':
                row[5] = '1'

            # letters in address numbers
            if ' ' in row[5]:
                numnol = row[5].split(' ')[0]
                address_in = numnol + ' ' + row[6] + ' ' + row[7]
                for address in address_table:
                    if address_in == address[2]:
                        good += 1
                        geocoded = 1
                        # add in X, Y, and class to row
                        out_row = row + [address[3],address[4],address[5]]
                        address_out_good.append(out_row)
                        # print 'good'
                        break
                    else:
                        geocoded = 0


            # east west mall cases
            if 'MALL' in row[6] and geocoded == 0:

                address_in = row[5] + ' ' + row[6]

                for address in address_table:
                    if str(address_in) == address[2]:
                        good += 1
                        geocoded = 1

                        # add in X, Y, and class to row
                        out_row = row + [address[3],address[4],address[5]]
                        address_out_good.append(out_row)
                        # print 'good'
                        break

                    else:
                        geocoded = 0
                # for letters in add numbers
                if ' ' in row[5] and geocoded == 0:
                    numnol = row[5].split(' ')[0]
                    address_in = numnol + ' ' + row[6] + ' ' + row[7]
                    for address in address_table:
                        if address_in == address[2]:
                            good += 1
                            geocoded = 1
                            # add in X, Y, and class to row
                            out_row = row + [address[3],address[4],address[5]]
                            address_out_good.append(out_row)
                            # print 'good'
                            break
                        else:
                            geocoded = 0

            # anything with and E or W in the name
            if row[8] == 'E' or row[8] == 'W':
                address_in = row[5] + ' ' + row[6] + ' ' + row[7] + ' ' + row[8]
                for address in address_table:
                    if address_in == address[2]:
                        good += 1
                        geocoded = 1
                        # add in X, Y, and class to row
                        out_row = row + [address[3],address[4],address[5]]
                        address_out_good.append(out_row)
                        # print 'good'
                        break
                    else:
                        geocoded = 0
                # if letter in name
                if ' ' in row[5] and geocoded == 0:
                    numnol = row[5].split(' ')[0]
                    address_in = numnol + ' ' + row[6] + ' ' + row[7]
                    for address in address_table:
                        if address_in == address[2]:
                            good += 1
                            geocoded = 1
                            # add in X, Y, and class to row
                            out_row = row + [address[3],address[4],address[5]]
                            address_out_good.append(out_row)
                            # print 'good'
                            break
                        else:
                            geocoded = 0

            # queens sisters
            if 'QUEENSWAY' in row[6] or 'QUEENS QUAY' in row[6] or 'KINGSWAY' in row[6] or 'WESTWAY' in row[6]:
                address_in = row[5] + ' ' + row[6]
                for address in address_table:
                    if address_in == address[2]:
                        good += 1
                        geocoded = 1
                        # add in X, Y, and class to row
                        out_row = row + [address[3],address[4],address[5]]
                        address_out_good.append(out_row)
                        # print 'good'
                        break
                    else:
                        geocoded = 0
                # numbers in name
                if ' ' in row[5] and geocoded == 0:
                    numnol = row[5].split(' ')[0]
                    address_in = numnol + ' ' + row[6]
                    for address in address_table:
                        if address_in == address[2]:
                            good += 1
                            geocoded = 1
                            # add in X, Y, and class to row
                            out_row = row + [address[3],address[4],address[5]]
                            address_out_good.append(out_row)
                            # print 'good'
                            break
                        else:
                            geocoded = 0

            # if there is a dash in the number e.g. 10-18 xxx st
            if '-' in row[5] and geocoded == 0:
                # split it up
                try:
                    num1 = int(row[5].split('-')[0])
                    num2 = int(row[5].split('-')[1])
                    # compute the range, by 2s (same street side)
                    numr = range(num1,num2+2,2)
                    # loop over each, attempting to geocode
                    for num in numr:

                        if row[8] == 'E' or row[8] == 'W':
                            address_in = str(num) + ' ' + row[6] + ' ' + row[7] + ' ' + row[8]
                        elif 'MALL' in row[6]:
                            address_in = str(num) + ' ' + row[6]
                        else:
                            address_in = str(num) + ' ' + row[6] + ' ' + row[7]

                        for address in address_table:
                            if str(address_in) == address[2]:
                                good += 1
                                geocoded = 1

                                # add in X, Y, and class to row
                                out_row = row + [address[3],address[4],address[5]]
                                address_out_good.append(out_row)
                                # print 'good'
                                break

                            else:
                                geocoded = 0

                        if geocoded == 1:
                            break
                except:
                    geocoded = 0


        # finally, if bad, then append to bad table
        if geocoded == 0:
            if 'IBMS' in row[6] or row[6] == ' ' or row[6] == '':
                address_out_empty.append(row)
                empty += 1
            else:
                address_out_bad.append(row)

    q += 1
    print q

    #code in break if needed
    # if q == 500:
    #     break

# minimize the addresss
address_bad_min = []
for bad_add in address_out_bad:
    a_bad_row = [bad_add[5],bad_add[6],bad_add[7],bad_add[8]]
    if a_bad_row not in address_bad_min:
        address_bad_min.append(a_bad_row)


# write the results to tables
# those that geocoded properly
with open ('building_permits/geocode_2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(out_header)
    for ag in address_out_good:
        writer.writerow(ag)

# write any that failed to geocode
with open ('building_permits/still_2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for ag in address_out_bad:
        writer.writerow(ag)

# write any empty fields for future ref
with open ('building_permits/empty_addresses.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for ae in address_out_empty:
        writer.writerow(ae)

# write reduced table
with open ('building_permits/address_bad_min.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    for ae in address_bad_min:
        writer.writerow(ae)

print time.time() - start_time


# print how long everything took as well as basic stats
print good
print q - good
print float(good) / float(q)
print q
print empty
print len(address_out_bad)
print len(address_bad_min)
