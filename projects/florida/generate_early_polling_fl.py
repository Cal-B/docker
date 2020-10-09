import argparse
#from pathlib import Path
import os
import urllib, json
from json_extract import flatten_json
import csv
import pandas 
import math
import xlrd

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--input", required=True, help="Input folder directory")
arg_parser.add_argument("-o", "--output", required=False, help="Output folder directory, default location is inside the input folder")
args = vars(arg_parser.parse_args())

src = args['input']
output = args['output']

url_header = "http://localhost:4000/v1/autocomplete?text="

counter = 0
total = 0
public_records_exemption = 0

parsed_data = pandas.DataFrame(columns = ['location_name', 'location_type', 'address'])
refined_data = pandas.DataFrame(columns = ['location_name', 'location_type', 'address', 'latitude', 'longitude'])

print("Reading files into dataframe...")
filenames = (f for f in os.listdir(src) if f.endswith('.csv'))
for pos, file in enumerate(filenames):
    print("Loading " + os.path.join(src,file) + "...")
    extracted_data = pandas.read_csv(os.path.join(src,file), usecols = [0, 1, 2], names = ['location_name', 'location_type', 'address'])
    parsed_data = parsed_data.append(extracted_data, ignore_index = True)       # TODO Should switch to concat at some point
    
print("Done")
print("Frame has " + str(len(parsed_data.index)) + " entries")


latitudes = []
longitudes = []
check_for_address = False
for index, row in parsed_data.iterrows():
    if (str(row['address']) == 'Address'):  # our next row is an address
        check_for_address = True
        continue
    if check_for_address:
        refined_data = refined_data.append({'location_name': row['location_name'], 'location_type' : row['location_type'], 'address' : row['address']},  ignore_index=True)
        check_for_address = False

print(refined_data.head(10))
for index, row in refined_data.iterrows():
    if total % 10000 == 0:
        print(str(total) + " processed")
    if (str(row['address']).find(" FL ") == -1):
        full_location = str(row['address']) + ", FL"
    else:
        full_location = str(row['address'])
    #print(full_location)
    response = urllib.urlopen(url_header + full_location)
    json_data = json.loads(response.read())
    coords = flatten_json(json_data)
    try:
        latitudes.append(coords['features_0_geometry_coordinates_1'])
        longitudes.append(coords['features_0_geometry_coordinates_0'])
        # print("found coords: " + str(coords['features_0_geometry_coordinates_1']) + ", " +str(coords['features_0_geometry_coordinates_0']))
    except KeyError:
        counter = counter + 1 
        latitudes.append("")
        longitudes.append("")
        # print("no coords")
        # print(full_location + " has no available coordinates, maybe its an address on a highway?")
    total = total + 1


refined_data['latitude'] = pandas.Series(latitudes)
refined_data['longitude'] = pandas.Series(longitudes)
refined_data.to_csv("~/Downloads/fl_early_polling_statewide_latsandlongs.csv", mode='w', header=True, sep='\t', index=False)
print(str(counter) + " / " + str(total) + " had missing latitude/longitude")


