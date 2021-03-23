import pandas 
import urllib.request, urllib.parse
import json
import numpy

source_csv = pandas.read_csv("~/Downloads/ncvoter_statewide_latsandlons (copy).csv", sep="\t")

print((source_csv['geolocation_source'] == "bing").sum())

# source_csv["api_failed_to_resolve"] = ""
# source_csv["geolocation_source"] = ""

# source_csv.to_csv("~/Downloads/ncvoter_statewide_latsandlongs_copy.csv", mode='w', header=True, sep='\t', index=False)