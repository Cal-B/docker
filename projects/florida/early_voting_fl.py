import pandas 
from matplotlib import pyplot
import numpy

def division(n, d):
    return n / d if d else 0

early_voting = pandas.read_csv('~/Downloads/fl_early_polling_statewide_latsandlongs.csv', sep='\t')
early_voting = early_voting.sort_values(by=['county'])
current_county = ''
current_county_found = 0
current_county_missing = 0

county_stats = []

for index, row in early_voting.iterrows():
    if (str(row['county']) != current_county):
        county_stats.append((current_county, current_county_found, current_county_missing, (division(current_county_missing, current_county_found) * 100)))
        current_county = str(row['county'])
        current_county_found = 0
        current_county_missing = 0
    
    current_county_found += 1
    if (pandas.isna(row['latitude'])):
        current_county_missing += 1

# county_stats = sorted(county_stats, key = lambda tup: tup[3])
# for county in county_stats:
#     print('{:<40}: {:<1}/{:<1}, {:<2}% missing'.format(county[0], str(county[2]), str(county[1]), str(county[3])))


[float('nan') if x==0 else x for x in county_stats[2]]
chart = pyplot.figure(figsize =(10, 7))
fig1, ax1 = pyplot.subplots()
pyplot.pie([x[2] for x in county_stats],autopct='%1.1f%%', startangle=90, labels = [x[0] for x in county_stats])

pyplot.show()