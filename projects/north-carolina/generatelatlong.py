import argparse
from pathlib import Path
import os
import urllib, json
from json_extract import flatten_json
import csv

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--input", required=True, help="Input file")
arg_parser.add_argument("-o", "--output", required=False, help="Output file directory and name, default location is inside the input folder under latsandlongs.txt")
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


url_header = "http://localhost:4000/v1/autocomplete?text="

previous_location = ""
counter = 0
total = 0
with open(src, 'r') as polling_data:
    for line in polling_data:
        total = total + 1
        tokenized_data = line.split('\t')
        full_location = tokenized_data[4] + ', ' + tokenized_data[5]
        if full_location != previous_location:
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
            
            new_row = [tokenized_data[0], tokenized_data[1], tokenized_data[2], tokenized_data[3], tokenized_data[4], tokenized_data[5], latitude, longitude]
            output_csv_writer.writerow(new_row)
            previous_location = full_location

print(str(counter) + " / " + str(total) + " had missing latitude/longitude")

        


    
    



