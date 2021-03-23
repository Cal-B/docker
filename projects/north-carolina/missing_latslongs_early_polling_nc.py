import pandas 

def division(n, d):
    return n / d if d else 0

early_voting = pandas.read_csv("~/Downloads/nc_statewide_earlyvotinglocations_latsandlongs.csv", usecols=[1, 6, 7], names=['county', 'latitude', 'longitude'])

current_county = ''
current_county_found = 0
current_county_missing = 0

county_stats = []


# ['ALAMANCE' 'ALEXANDER' 'ALLEGHANY' 'BEAUFORT' 'BRUNSWICK' 'BUNCOMBE'
#  'BURKE' 'CALDWELL' 'CAMDEN' 'CARTERET' 'CHOWAN' 'CLEVELAND' 'CRAVEN'
#  'CUMBERLAND' 'CURRITUCK' 'DARE' 'DAVIDSON' 'DAVIE' 'DURHAM' 'EDGECOMBE'
#  'FRANKLIN' 'GASTON' 'GRANVILLE' 'HALIFAX' 'HARNETT' 'HAYWOOD' 'HERTFORD'
#  'HYDE' 'JACKSON' 'JOHNSTON' 'JONES' 'MACON' 'MADISON' 'MCDOWELL' 'MOORE'
#  'NEW HANOVER' 'PAMLICO' 'PASQUOTANK' 'PENDER' 'PERSON' 'PITT' 'POLK'
#  'RICHMOND' 'ROWAN' 'RUTHERFORD' 'SAMPSON' 'SCOTLAND' 'STANLY' 'SWAIN'
#  'VANCE' 'WAKE' 'WARREN' 'WATAUGA' 'WAYNE' 'WILKES' 'YANCEY']

# print(early_voting.county.unique())

for index, row in early_voting.iterrows():
    if (str(row['county']) != current_county):
        county_stats.append((current_county, current_county_found, current_county_missing, (division(current_county_missing, current_county_found) * 100)))
        current_county = str(row['county'])
        current_county_found = 0
        current_county_missing = 0
    
    current_county_found += 1
    if (pandas.isna(row['latitude'])):
        current_county_missing += 1

for county in county_stats:
   print('{:<40}: {:<1}/{:<1}, {:<2}% missing'.format(county[0], str(county[2]), str(county[1]), str(county[3])))


