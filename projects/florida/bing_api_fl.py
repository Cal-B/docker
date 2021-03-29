from json_extract import flatten_json
import requests
from tabulate import tabulate
import math 
import numpy
import pandas 
import urllib.request, urllib.parse
import json

source_csv = pandas.read_csv("~/Downloads/flvoters_statewide_latsandlongs_found_copy.csv", sep="\t")

count = 0
missing = 0
successful = 0

source_csv['latlong_found'] = source_csv['latitude']
source_csv['latlong_found'] = numpy.where(pandas.isna(source_csv.latitude),'N', 'Y')

print(tabulate(source_csv.groupby(['latlong_found', 'removed']).size().reset_index().rename(columns={0:'count'}), headers='keys', tablefmt='psql', showindex=False))

print("processing...")
for index, row in source_csv.iterrows():
    if str(row['api_failed_to_resolve']) == "Y":
        continue    # we have previously tried to request this and it was unable to be resolved 
    if count == 49950:
        break   # reached our daily limit
    if (str(row['removed']) == 'N' and pandas.isna(row['latitude'])):
        adminDistrict = "FL"
           
        postalCode = str(int(row['res_zipcode'])) if not pandas.isna(row['res_zipcode']) else '-'

        locality = str(row['res_city']) if not pandas.isna(row['res_city']) else '-'

        address = str(row['res_street_address_line_1']) + " " + str(row['res_street_address_line_2'])
        addressLine = address if address else '-'

        maxResults = 1

        BingMapsAPIKey = ""
         
        

        # You can substitute a hyphen (-) for any structured URL parameter when there is no value.
        
        url_header = f'http://dev.virtualearth.net/REST/v1/Locations/?countryRegion=US&adminDistrict={adminDistrict}&locality={locality}&postalCode={postalCode}&addressLine={addressLine}&maxResults={maxResults}&key={BingMapsAPIKey}'

        # url_header_encoded = urllib.parse.quote(url_header)
        #  print(url_header)
        
        response = requests.get(url_header)
        count += 1

        if response.status_code == 200:
            successful += 1
            coords = flatten_json(response.json())
            latitude = coords['resourceSets_0_resources_0_point_coordinates_0']
            longitude = coords['resourceSets_0_resources_0_point_coordinates_1']
            # print(str(latitude) + ", " + str(longitude))
            source_csv.loc[index, 'latitude'] = latitude
            source_csv.loc[index, 'longitude'] = longitude
            source_csv.loc[index, 'api_failed_to_resolve'] = "N"
            source_csv.loc[index, 'geolocation_source'] = "bing"
        else:
            missing += 1
            source_csv.loc[index, 'api_failed_to_resolve'] = "Y"

source_csv['latlong_found_after'] = source_csv['latitude']
source_csv['latlong_found_after'] = numpy.where(pandas.isna(source_csv.latitude),'N', 'Y')

print(tabulate(source_csv.groupby(['latlong_found', 'latlong_found_after', 'removed']).size().reset_index().rename(columns={0:'count'}), headers='keys', tablefmt='psql', showindex=False))

if successful == 0:
    # We have finished all the missing entries for this sheet
    print("Finished all possible entries in sheet")

source_csv.to_csv("~/Downloads/ncvoter_statewide_latsandlons (copy).csv", mode='w', header=True, sep='\t', index=False)

