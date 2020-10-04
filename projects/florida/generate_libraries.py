import argparse
import os
import urllib, json
from json_extract import flatten_json
import csv
import pandas 
import math

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--input", required=True, help="Input file")
args = vars(arg_parser.parse_args())

src = args['input']


url_header = "http://localhost:4000/v1/autocomplete?text="

counter = 0
total = 0

print("Reading in name columns from the CSV...")
parsed_data = pandas.read_csv(src, names = ['city', 'library', 'address', 'zipcode', 'phone'], sep='\t')
print("Done")
latandlong = pandas.DataFrame(columns=['latitude', 'longitude'])

latitudes = []
longitudes = []
for index, row in parsed_data.iterrows():
    if total % 10000 == 0:
        print(str(total) + " processed")
    if (str(row['zipcode']) == 'nan'):
        full_location_dirty = str(row['address']) + ", " + str(row['city']) + ", FL"
    else:
        full_location_dirty = str(row['address']) + ", " + str(row['city']) + ", FL " + str(int(row['zipcode']))
    full_location = ' '.join(full_location_dirty.split())
    print(full_location)
    response = urllib.urlopen(url_header + full_location)
    json_data = json.loads(response.read())
    coords = flatten_json(json_data)
    try:
        latitudes.append(coords['features_0_geometry_coordinates_1'])
        longitudes.append(coords['features_0_geometry_coordinates_0'])
    except KeyError:
        counter = counter + 1 
        latitudes.append("")
        longitudes.append("")
        # print(full_location + " has no available coordinates, maybe its an address on a highway?")
    total = total + 1


parsed_data['latitude'] = pandas.Series(latitudes)
parsed_data['longitude'] = pandas.Series(longitudes)
parsed_data.to_csv("~/Downloads/fl_schools_latsandlongs.csv", mode='w', header=True, sep='\t', index=False)
print(str(counter) + " / " + str(total) + " had missing latitude/longitude")
