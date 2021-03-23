import pandas 

fl_voter_1 = 0
fl_voter_2 = 0
fl_voter_3 = 0
fl_voter_4 = 0
fl_voter_5 = 0
fl_voter_6 = 0
fl_voter_7 = 0
fl_voter_9 = 0

fl_voter_1_missing = 0
fl_voter_2_missing = 0
fl_voter_3_missing = 0
fl_voter_4_missing = 0
fl_voter_5_missing = 0
fl_voter_6_missing = 0
fl_voter_7_missing = 0
fl_voter_9_missing = 0


voter_data = pandas.read_csv("~/Downloads/flvoter_statewide_latsandlongs.csv", usecols = ['race', 'latitude', 'longitude'], sep='\t')

for index, row in voter_data.iterrows():
    if index % 500000 == 0 and index != 0:
        print(str(index / 14826104) + "% processed")
    number = int(row['race'])
    if (number == 1):
        fl_voter_1 += 1
        if pandas.isna(row['latitude']):
            fl_voter_1_missing += 1
    elif (number == 2):
        fl_voter_2 += 1
        if pandas.isna(row['latitude']):
            fl_voter_2_missing += 1
    elif (number == 3):
        fl_voter_3 += 1
        if pandas.isna(row['latitude']):
            fl_voter_3_missing += 1
    elif (number == 4):
        fl_voter_4 += 1
        if pandas.isna(row['latitude']):
            fl_voter_4_missing += 1
    elif (number == 5):
        fl_voter_5 += 1
        if pandas.isna(row['latitude']):
            fl_voter_5_missing += 1
    elif (number == 6):
        fl_voter_6 += 1
        if pandas.isna(row['latitude']):
            fl_voter_6_missing += 1
    elif (number == 7):
        fl_voter_7 += 1
        if pandas.isna(row['latitude']):
            fl_voter_7_missing += 1
    elif (number == 9):
        fl_voter_9 += 1
        if pandas.isna(row['latitude']):
            fl_voter_9_missing += 1


print("1: " + str(fl_voter_1_missing) + " / " + str(fl_voter_1) + "   " + str(fl_voter_1_missing / fl_voter_1) + "% missing")
print("2: " + str(fl_voter_2_missing) + " / " + str(fl_voter_2) + "   " + str(fl_voter_2_missing / fl_voter_2) + "% missing")
print("3: " + str(fl_voter_3_missing) + " / " + str(fl_voter_3) + "   " + str(fl_voter_3_missing / fl_voter_3) + "% missing")
print("4: " + str(fl_voter_4_missing) + " / " + str(fl_voter_4) + "   " + str(fl_voter_4_missing / fl_voter_4) + "% missing")
print("5: " + str(fl_voter_5_missing) + " / " + str(fl_voter_5) + "   " + str(fl_voter_5_missing / fl_voter_5) + "% missing")
print("6: " + str(fl_voter_6_missing) + " / " + str(fl_voter_6) + "   " + str(fl_voter_6_missing / fl_voter_6) + "% missing")
print("7: " + str(fl_voter_7_missing) + " / " + str(fl_voter_7) + "   " + str(fl_voter_7_missing / fl_voter_7) + "% missing")
print("9: " + str(fl_voter_9_missing) + " / " + str(fl_voter_9) + "   " + str(fl_voter_9_missing / fl_voter_9) + "% missing")

