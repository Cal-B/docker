import argparse
from pathlib import Path
import os
import urllib, json
from json_extract import flatten_json
import csv
import pandas 

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--input", required=True, help="Input file")
arg_parser.add_argument("-o", "--output", required=True, help="Output file directory and name")
args = vars(arg_parser.parse_args())

src = args['input']
output = args['output']

if output is None:
    output = os.path.join(str(Path(src).parent), os.path.splitext(os.path.basename(src))[0] + '_latsandlongs.csv')
    output_file = open(output, 'w')
    print("Creating file " + os.path.splitext(os.path.basename(src))[0] + "_latsandlongs.csv at: " + output)
else:
    output_file = open(output, 'w')

output_csv = open(output, "w")
output_csv_writer = csv.writer(output_csv)

new_row = ['Library System', 'Branch Name', 'Library Type', 'Street Address', 'City', 'ZIP Code', 'County', 'Website', 'Phone Number', 'Director','Director Email', 'Branch Head', 'Email Address', 'Building Square Feet', 'FTE Staff', 'Hours', 'Latitude', 'Longitude']
output_csv_writer.writerow(new_row)

url_header = "http://localhost:4000/v1/autocomplete?text="

counter = 0
total = 0

parsed_data = pandas.read_csv(src)

for index, row in parsed_data.iterrows():
    full_location = str(row['Street Address']) + ", " + str(row['City']) + ", NC " + str(row['ZIP Code'])
    print(full_location)
    response = urllib.urlopen(url_header + full_location)
    json_data = json.loads(response.read())
    coords = flatten_json(json_data)
    try:
        latitude = coords['features_0_geometry_coordinates_1']
        longitude = coords['features_0_geometry_coordinates_0']
    except KeyError:
        counter = counter + 1 
        latitude = ""
        longitude = ""
        print(full_location + " has no available coordinates, maybe its an address on a highway?")
    new_row = [row['Library System'], row['Branch Name'], row['Library Type'], row['Street Address'], row['City'], row['ZIP Code'], row['County'], row['Website'], row['Phone Number'], row['Director'], row['Director Email'], row['Branch Head'], row['Email Address'], row['Building Square Feet'], row['FTE Staff'], row['Hours'], latitude, longitude]
    output_csv_writer.writerow(new_row)
    total = total + 1

print(str(counter) + " / " + str(total) + " had missing latitude/longitude")

        


    
    



