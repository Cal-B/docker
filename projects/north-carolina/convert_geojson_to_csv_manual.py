import argparse
from pathlib import Path
import os
import urllib, json
from json_extract import flatten_json
import csv
import json_extract

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--input", required=True, help="Input file directory")
arg_parser.add_argument("-o", "--output", required=False, help="Output file directory and name, default location is inside the folder under /csvs")
args = vars(arg_parser.parse_args())

src = args['input']
output = args['output']

if output is None:
    output = os.path.join(src, 'csvs')
if not os.path.exists(output):
    os.mkdir(output)

print("Source directory set to: " + src)
print("Output directory set to: " + output)

filenames = (f for f in os.listdir(src) if f.endswith('.geojson'))
for file in filenames:
    file_path = os.path.join(src, file)
    filename_pruned = file.split('-')[0]
    filename_no_extension = os.path.splitext(filename_pruned)[0]
    filename_output = os.path.join(output, filename_no_extension + ".csv")

    current_geojson_path = os.path.join(src, file)

    output_csv = open(filename_output, "w")
    output_csv_writer = csv.writer(output_csv)

    header_row = ['LON', 'LAT', 'NUMBER', 'STREET', 'UNIT', 'CITY', 'DISTRICT', 'REGION', 'POSTCODE', 'ID', 'HASH']
    output_csv_writer.writerow(header_row)

    print('Outputting ' + filename_output + ' from ' + file_path)

    with open(current_geojson_path, 'r') as geojson:
        for line in geojson:
            json_data = json.loads(line)
            coords = flatten_json(json_data)
            longitude = coords['geometry_coordinates_0']
            latitude = coords['geometry_coordinates_1']
            number = coords['properties_number']
            street = coords['properties_street']
            unit = coords['properties_unit']
            city = coords['properties_city']
            district = coords['properties_district']
            region = coords['properties_region']
            postcode = coords['properties_postcode']
            prop_id = coords['properties_id']
            prop_hash = coords['properties_hash']

            new_row = [longitude, latitude, number, street, unit, city, district, region, postcode, prop_id, prop_hash]
            output_csv_writer.writerow(new_row)

            
