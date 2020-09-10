import argparse
from pathlib import Path
import os
import urllib, json
from json_extract import flatten_json
import csv
import pandas 

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

counter = 0
total = 0

parsed_data = pandas.read_csv(src)

for index, row in parsed_data.iterrows():
    if index == 0:
        title_row = "Primary_Key","School Number","School Year","School Name","Official School Name","LEA Number","LEA Name","Name Prefix Description","Principal First Name","Principal Middle Name","Principal Last Name","Principal Name Suffix","Principal Email","Address Line1","Address Line2","City","State","Zip Code 5","Zip Code 4","Phone Office Area","Phone Office Exch","Phone Office Line","Phone Fax Area","Phone Fax Exch","Phone Fax Line ","Mailing Address Line1","Mailing Address Line2","Mailing City","Mailing State","Mailing Zip Code 5","Mailing Zip Code 4","URL School Address","Sch Operational Status","Sch Operational Status Desc","Opening Effective Date","Closing Date","School Type","School Type Desc","School Program Type","School Program Type Desc","Grade Level Current","Grade Level Approved","Grade Level First Year","Title I","School Calendar Type","School Calendar Description","Extended Hours","School Schedule Type","School Schedule Type Desc","School Designation Type","School Designation Desc","Virtual Status","SBE Region","SBE Region Names","Accreditation Status","Accreditation Status Desc","Federal School Number","College Board Number","School Membership","School Year For Sch Membership","School Teacher Count","School Year For Teachers","Cooperative Innovative HS","Cooperative MMYYYY SBE Approve","First Yr Est ADM","First Yr Est Paid Teacher FTE","Newly Constructed Facility","Occupancy Date","What Facility Will Sch Occupy","Share Space","Share Space Describe","New Sch Population From","List Of Closing Schools","County Code","County Description","Opening In School Year","Locale Type","Locale Type Desc","School Closings?","School Systartstatus","Record Created Timestamp","Record Created By","Last Changed Timestamp","Last Changed By", 'Latitude', 'Longitude'
        output_csv_writer.writerow(title_row)
        continue
    full_location = str(row['Address Line1']) + ", " + str(row['City']) + ", " + str(row['State']) + " " + str(row['Zip Code 5'])
    #print(full_location)
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
        #print(full_location + " has no available coordinates, maybe its an address on a highway?")
    new_row = row["Primary_Key"],row["School Number"],row["School Year"],row["School Name"],row["Official School Name"],row["LEA Number"],row["LEA Name"],row["Name Prefix Description"],row["Principal First Name"],row["Principal Middle Name"],row["Principal Last Name"],row["Principal Name Suffix"],row["Principal Email"],row["Address Line1"],row["Address Line2"],row["City"],row["State"],row["Zip Code 5"],row["Zip Code 4"],row["Phone Office Area"],row["Phone Office Exch"],row["Phone Office Line"],row["Phone Fax Area"],row["Phone Fax Exch"],row["Phone Fax Line "],row["Mailing Address Line1"],row["Mailing Address Line2"],row["Mailing City"],row["Mailing State"],row["Mailing Zip Code 5"],row["Mailing Zip Code 4"],row["URL School Address"],row["Sch Operational Status"],row["Sch Operational Status Desc"],row["Opening Effective Date"],row["Closing Date"],row["School Type"],row["School Type Desc"],row["School Program Type"],row["School Program Type Desc"],row["Grade Level Current"],row["Grade Level Approved"],row["Grade Level First Year"],row["Title I"],row["School Calendar Type"],row["School Calendar Description"],row["Extended Hours"],row["School Schedule Type"],row["School Schedule Type Desc"],row["School Designation Type"],row["School Designation Desc"],row["Virtual Status"],row["SBE Region"],row["SBE Region Names"],row["Accreditation Status"],row["Accreditation Status Desc"],row["Federal School Number"],row["College Board Number"],row["School Membership"],row["School Year For Sch Membership"],row["School Teacher Count"],row["School Year For Teachers"],row["Cooperative Innovative HS"],row["Cooperative MMYYYY SBE Approve"],row["First Yr Est ADM"],row["First Yr Est Paid Teacher FTE"],row["Newly Constructed Facility"],row["Occupancy Date"],row["What Facility Will Sch Occupy"],row["Share Space"],row["Share Space Describe"],row["New Sch Population From"],row["List Of Closing Schools"],row["County Code"],row["County Description"],row["Opening In School Year"],row["Locale Type"],row["Locale Type Desc"],row["School Closings?"],row["School Systartstatus"],row["Record Created Timestamp"],row["Record Created By"],row["Last Changed Timestamp"],row["Last Changed By"], latitude, longitude
    output_csv_writer.writerow(new_row)
    total = total + 1

print(str(counter) + " / " + str(total) + " had missing latitude/longitude")

        


    
    



