import argparse
from pathlib import Path
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

output_csv = open(src, "a")
output_csv_writer = csv.writer(output_csv)

missing_latsandlongs = os.path.join(str(Path(src).parent), os.path.splitext(os.path.basename(src))[0] + '_missing_latandlong.csv')
output_csv_missing_latandlong = open(missing_latsandlongs, "a")

url_header = "http://localhost:4000/v1/autocomplete?text="

counter = 0
total = 0

print("Reading in name columns from the CSV...")
parsed_data = pandas.read_csv(src, usecols=["res_street_address", "res_city_desc", "state_cd", "zip_code", "last_name", "first_name", "middle_name", "ethnic_code", "race_code"], sep='\t')
print("Done")
latandlong = pandas.DataFrame(columns=['latitude', 'longitude'])
test_append_csv = os.path.join(str(Path(src).parent), 'nc_statewide_earlyvotinglocations_latsandlongs.csv')

latitudes = []
longitudes = []
for index, row in parsed_data.iterrows():
    if total % 10000 == 0:
        print(str(total) + " processed")
    if row['res_street_address'] == "REMOVED":
        latitudes.append("")
        longitudes.append("")
        # print(full_location + " has no available coordinates, maybe its an address on a highway?")
        total = total + 1
        continue
    if math.isnan(row['zip_code']):
        latitudes.append("")
        longitudes.append("")
        # print(full_location + " has no available coordinates, maybe its an address on a highway?")
        total = total + 1
        continue
    full_location_dirty = str(row['res_street_address']) + ", " + str(row['res_city_desc']) + ", " + str(row['state_cd']) + " " + str(int(row['zip_code']))
    full_location = ' '.join(full_location_dirty.split())
    # print(full_location)
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
parsed_data.to_csv("~/Downloads/ncvoter_statewide_latsandlongs.csv", mode='w', header=True, sep='\t', index=False)
print(str(counter) + " / " + str(total) + " had missing latitude/longitude")
