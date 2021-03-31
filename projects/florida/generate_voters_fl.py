import argparse
#from pathlib import Path
import os
import urllib, json
from json_extract import flatten_json
import csv
import pandas 
import math

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--input", required=True, help="Input folder directory, directory full of csvs")
arg_parser.add_argument("-o", "--output", required=False, help="Output folder directory, default location is inside the input folder")
args = vars(arg_parser.parse_args())

src = args['input']
output = args['output']

url_header = "http://localhost:4000/v1/autocomplete?text="

counter = 0
total = 0
public_records_exemption = 0

parsed_data = pandas.DataFrame(columns = ['voter_name_last', 'voter_name_suffix', 'voter_name_first', 'voter_name_middle', 'res_street_address_line_1', 'res_street_address_line_2', 'res_city', 'res_state', 'res_zipcode', 'race'])

print("Reading files into dataframe...")
filenames = (f for f in os.listdir(src) if f.endswith('.txt'))
for pos, file in enumerate(filenames):
    print("Loading " + os.path.join(src,file) + "...")
    extracted_data = pandas.read_csv(os.path.join(src,file), usecols=[2, 3, 4, 5, 7, 8, 9, 10, 11, 20], names = ['voter_name_last', 'voter_name_suffix', 'voter_name_first', 'voter_name_middle', 'res_street_address_line_1', 'res_street_address_line_2', 'res_city', 'res_state', 'res_zipcode', 'race'], sep='\t', header=None)
    parsed_data = parsed_data.append(extracted_data, ignore_index = True)
print("Done")
print("Frame has " + str(len(parsed_data.index)) + " entries")

latitudes = []
longitudes = []
for index, row in parsed_data.iterrows():
    if total % 10000 == 0:
        print(str(total) + " processed")
    if (row['res_street_address_line_1'] == "*"):
        latitudes.append("")
        longitudes.append("")
        # print(full_location + " has no available coordinates, maybe its an address on a highway?")
        public_records_exemption = public_records_exemption + 1
        total = total + 1
        continue
    full_location_dirty = str(row['res_street_address_line_1']) + " " + str(row['res_street_address_line_2']) + ", " + str(row['res_city']) + ", FL " + str(row['res_zipcode'])
    full_location = ' '.join(full_location_dirty.split())
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


parsed_data['latitude'] = pandas.Series(latitudes)
parsed_data['longitude'] = pandas.Series(longitudes)
parsed_data.to_csv("~/Downloads/flvoter_statewide_latsandlongs.csv", mode='w', header=True, sep='\t', index=False)
print(str(counter) + " / " + str(total) + " had missing latitude/longitude")
print(str(public_records_exemption) + " were exempt from providing addresses")


