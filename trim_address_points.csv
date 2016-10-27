# takes a csv address file from city of toronto open data
# and trims it down so it can be used as a geocoder

import csv
import time

start_time = time.time()

# out array
# number, street, X, Y, class
address_array = []

# list of all unique land classes (for fun!)
type_test = []

# counter
c = 0

with open('address_points/address_points.csv','r') as address_csv:
    reader = csv.DictReader(address_csv)
    for row in reader:

        # c += 1
        # print row['ADDRESS']
        # if c > 110:
        #     break

        # get unique list of land/structure types
        if row['FCODE_DES'] not in type_test:
            type_test.append(row['FCODE_DES'])

        # addresses that have a single integer
        try:
            address_num = int(row['ADDRESS'])
            address_name = row['LFNAME']
            address_upper = row['ADDRESS'] + ' ' + UPPER(row['LFNAME'])
            address_X = float(row['lon'])
            address_Y = float(row['lat'])
            address_class = row['FCODE_DES']
            address_row = [address_num,address_name,address_upper,address_X,address_Y, address_class]
            address_array.append(address_row)

        # try parse other funky addresses
        except:
            # those with an address range
            if '-' in row['ADDRESS']:
                address_name = row['LFNAME']
                address_X = float(row['lon'])
                address_Y = float(row['lat'])
                add_high = int(row['HINUM'])
                add_low = int(row['LONUM'])
                add_range = add_high - add_low
                address_num = add_low
                while address_num <= add_high:
                    address_upper = str(address_num) + ' ' + (row['LFNAME']).upper()
                    address_row = [address_num,address_name,address_upper,address_X,address_Y, address_class]
                    address_array.append(address_row)
                    address_num += 2

            # those with letters - this could be improved somehow
            else:
                address_num = (row['ADDRESS'])
                address_name = row['LFNAME']
                address_upper = str(address_num) + ' ' + (row['LFNAME']).upper()
                address_X = float(row['lon'])
                address_Y = float(row['lat'])
                address_class = row['FCODE_DES']
                address_row = [address_num,address_name,address_upper,address_X,address_Y,address_class]
                address_array.append(address_row)

# write output to file
with open('address_points/address_trim.csv','w') as out_csv:
    writer = csv.writer(out_csv)
    writer.writerow(['number','street','upper','X','Y','class'])
    for row in address_array:
        writer.writerow(row)


print "+" * 14
print time.time() - start_time
