import pandas 
from tabulate import tabulate
import math 
import numpy

# def division(n, d):
#     return n / d if d else 0

voter_data = pandas.read_csv("~/Downloads/ncvoter_statewide_latsandlongs_corrected.csv", usecols = ['race_code', 'ethnic_code', 'removed', 'latitude'], sep='\t')

# # print(voter_data.race_code.unique())
# # print(voter_data.ethnic_code.unique())
voter_data['latlong_found'] = voter_data['latitude']
voter_data['latlong_found'] = numpy.where(pandas.isna(voter_data.latitude),'N', 'Y')

voter_data.to_csv("~/Downloads/ncvoters_statewide_latsandlongs_found.csv", mode='w', header=True, sep='\t', index=False)
print(tabulate(voter_data.groupby(['race_code', 'ethnic_code', 'latlong_found', 'removed']).size().reset_index().rename(columns={0:'count'}), headers='keys', tablefmt='psql', showindex=False))

# nc_voter_w = 0
# nc_voter_b = 0
# nc_voter_u = 0
# nc_voter_o = 0
# nc_voter_a = 0
# nc_voter_m = 0
# nc_voter_i = 0
# nc_voter_empty = 0
# nc_voter_nan = 0

# nc_voter_w_missing = 0
# nc_voter_b_missing = 0
# nc_voter_u_missing = 0
# nc_voter_o_missing = 0
# nc_voter_a_missing = 0
# nc_voter_m_missing = 0
# nc_voter_i_missing = 0
# nc_voter_empty_missing = 0
# nc_voter_nan_missing = 0

# nc_voter_nl = 0
# nc_voter_un = 0
# nc_voter_hl = 0
# nc_voter_eth_nan = 0

# nc_voter_nl_missing = 0
# nc_voter_un_missing = 0
# nc_voter_hl_missing = 0
# nc_voter_eth_nan_missing = 0

# # Combination Race and ethnicity values 

# w_nl = w_un = w_hl = w_eth_nan = 0
# w_nl_missing= w_un_missing= w_hl_missing= w_eth_nan_missing = 0

# b_nl = b_un= b_hl= b_eth_nan = 0
# b_nl_missing= b_un_missing= b_hl_missing= b_eth_nan_missing = 0

# u_nl= u_un= u_hl= u_eth_nan = 0
# u_nl_missing= u_un_missing= u_hl_missing= u_eth_nan_missing = 0

# o_nl= o_un= o_hl= o_eth_nan = 0
# o_nl_missing= o_un_missing= o_hl_missing= o_eth_nan_missing = 0

# a_nl= a_un= a_hl= a_eth_nan = 0
# a_nl_missing= a_un_missing= a_hl_missing= a_eth_nan_missing = 0

# m_nl= m_un= m_hl= m_eth_nan = 0
# m_nl_missing= m_un_missing= m_hl_missing= m_eth_nan_missing = 0

# i_nl= i_un= i_hl= i_eth_nan = 0
# i_nl_missing= i_un_missing= i_hl_missing= i_eth_nan_missing = 0

# empty_nl= empty_un= empty_hl= empty_eth_nan = 0
# empty_nl_missing= empty_un_missing= empty_hl_missing= empty_eth_nan_missing = 0

# nan_nl= nan_un= nan_hl= nan_eth_nan = 0
# nan_nl_missing= nan_un_missing= nan_hl_missing= nan_eth_nan_missing = 0




# for index, row in voter_data.iterrows():
#     if index % 500000 == 0 and index != 0:
#         print(str((index / 8058334) * 100) + "% processed")
#     race = row['race_code']
#     eth = row['ethnic_code']

#     if (race == "W"):
#         nc_voter_w += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_w_missing += 1
        
#         if (eth == 'NL'):
#             w_nl += 1
#             if pandas.isna(row['latitude']):
#                 w_nl_missing += 1
#         elif (eth == 'UN'):
#             w_un += 1
#             if pandas.isna(row['latitude']):
#                 w_un_missing += 1
#         elif (eth == 'HL'):
#             w_un += 1
#             if pandas.isna(row['latitude']):
#                 w_hl_missing += 1
#         elif (pandas.isna(eth)):
#             w_nan += 1
#             if pandas.isna(row['latitude']):
#                 w_eth_nan_missing += 1
        
#     elif (race == 'B'):
#         nc_voter_b += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_b_missing += 1
        
#         if (eth == 'NL'):
#             b_nl += 1
#             if pandas.isna(row['latitude']):
#                 b_nl_missing += 1
#         elif (eth == 'UN'):
#             b_un += 1
#             if pandas.isna(row['latitude']):
#                 b_un_missing += 1
#         elif (eth == 'HL'):
#             b_un += 1
#             if pandas.isna(row['latitude']):
#                 b_hl_missing += 1
#         elif (pandas.isna(eth)):
#             b_nan += 1
#             if pandas.isna(row['latitude']):
#                 b_eth_nan_missing += 1

#     elif (race == 'U'):
#         nc_voter_u += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_u_missing += 1
        
#         if (eth == 'NL'):
#             u_nl += 1
#             if pandas.isna(row['latitude']):
#                 u_nl_missing += 1
#         elif (eth == 'UN'):
#             u_un += 1
#             if pandas.isna(row['latitude']):
#                 u_un_missing += 1
#         elif (eth == 'HL'):
#             u_un += 1
#             if pandas.isna(row['latitude']):
#                 u_hl_missing += 1
#         elif (pandas.isna(eth)):
#             u_nan += 1
#             if pandas.isna(row['latitude']):
#                 u_eth_nan_missing += 1

#     elif (race == 'O'):
#         nc_voter_o += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_o_missing += 1

#         if (eth == 'NL'):
#             o_nl += 1
#             if pandas.isna(row['latitude']):
#                 o_nl_missing += 1
#         elif (eth == 'UN'):
#             o_un += 1
#             if pandas.isna(row['latitude']):
#                 o_un_missing += 1
#         elif (eth == 'HL'):
#             o_un += 1
#             if pandas.isna(row['latitude']):
#                 w_hl_missing += 1
#         elif (pandas.isna(eth)):
#             o_nan += 1
#             if pandas.isna(row['latitude']):
#                 o_eth_nan_missing += 1

#     elif (race == 'A'):
#         nc_voter_a += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_a_missing += 1
        
#         if (eth == 'NL'):
#             a_nl += 1
#             if pandas.isna(row['latitude']):
#                 a_nl_missing += 1
#         elif (eth == 'UN'):
#             a_un += 1
#             if pandas.isna(row['latitude']):
#                 a_un_missing += 1
#         elif (eth == 'HL'):
#             a_un += 1
#             if pandas.isna(row['latitude']):
#                 a_hl_missing += 1
#         elif (pandas.isna(eth)):
#             a_nan += 1
#             if pandas.isna(row['latitude']):
#                 a_eth_nan_missing += 1
#     elif (race == 'M'):
#         nc_voter_m += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_m_missing += 1
        
#         if (eth == 'NL'):
#             m_nl += 1
#             if pandas.isna(row['latitude']):
#                 m_nl_missing += 1
#         elif (eth == 'UN'):
#             m_un += 1
#             if pandas.isna(row['latitude']):
#                 m_un_missing += 1
#         elif (eth == 'HL'):
#             m_un += 1
#             if pandas.isna(row['latitude']):
#                 m_hl_missing += 1
#         elif (pandas.isna(eth)):
#             m_nan += 1
#             if pandas.isna(row['latitude']):
#                 m_eth_nan_missing += 1

#     elif (race == 'I'):
#         nc_voter_i += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_i_missing += 1
        
#         if (eth == 'NL'):
#             i_nl += 1
#             if pandas.isna(row['latitude']):
#                 i_nl_missing += 1
#         elif (eth == 'UN'):
#             i_un += 1
#             if pandas.isna(row['latitude']):
#                 i_un_missing += 1
#         elif (eth == 'HL'):
#             i_un += 1
#             if pandas.isna(row['latitude']):
#                 i_hl_missing += 1
#         elif (pandas.isna(eth)):
#             i_nan += 1
#             if pandas.isna(row['latitude']):
#                 i_eth_nan_missing += 1
#     elif (race == ' '):
#         nc_voter_empty += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_empty_missing += 1

#         if (eth == 'NL'):
#             empty_nl += 1
#             if pandas.isna(row['latitude']):
#                 empty_nl_missing += 1
#         elif (eth == 'UN'):
#             empty_un += 1
#             if pandas.isna(row['latitude']):
#                 empty_un_missing += 1
#         elif (eth == 'HL'):
#             empty_un += 1
#             if pandas.isna(row['latitude']):
#                 empty_hl_missing += 1
#         elif (pandas.isna(eth)):
#             empty_nan += 1
#             if pandas.isna(row['latitude']):
#                 empty_eth_nan_missing += 1

#     elif (pandas.isna(row['race_code'])):
#         nc_voter_b += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_b_missing += 1
        
#         if (eth == 'NL'):
#             nan_nl += 1
#             if pandas.isna(row['latitude']):
#                 nan_nl_missing += 1
#         elif (eth == 'UN'):
#             nan_un += 1
#             if pandas.isna(row['latitude']):
#                 nan_un_missing += 1
#         elif (eth == 'HL'):
#             nan_un += 1
#             if pandas.isna(row['latitude']):
#                 nan_hl_missing += 1
#         elif (pandas.isna(eth)):
#             nan_eth_nan += 1
#             if pandas.isna(row['latitude']):
#                 nan_eth_nan_missing += 1

#     if (eth == "NL"):
#         nc_voter_nl += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_nl_missing += 1
#     elif (eth == 'UN'):
#         nc_voter_un += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_un_missing += 1
#     elif (eth == 'HL'):
#         nc_voter_hl += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_hl_missing += 1
#     elif (pandas.isna(row['ethnic_code'])):
#         nc_voter_un += 1
#         if pandas.isna(row['latitude']):
#             nc_voter_eth_nan_missing += 1


# print("W: " + str(nc_voter_w_missing) + " / " + str(nc_voter_w) + "   " + str(division(nc_voter_w_missing, nc_voter_w)* 100) + "% missing")
# print("B: " + str(nc_voter_b_missing) + " / " + str(nc_voter_b) + "   " + str(division(nc_voter_b_missing, nc_voter_b)* 100) + "% missing")
# print("U: " + str(nc_voter_u_missing) + " / " + str(nc_voter_u) + "   " + str(division(nc_voter_u_missing, nc_voter_u)* 100) + "% missing")
# print("O: " + str(nc_voter_o_missing) + " / " + str(nc_voter_o) + "   " + str(division(nc_voter_o_missing, nc_voter_o)* 100) + "% missing")
# print("A: " + str(nc_voter_a_missing) + " / " + str(nc_voter_a) + "   " + str(division(nc_voter_a_missing, nc_voter_a)* 100) + "% missing")
# print("M: " + str(nc_voter_m_missing) + " / " + str(nc_voter_m) + "   " + str(division(nc_voter_m_missing, nc_voter_m)* 100) + "% missing")
# print("I: " + str(nc_voter_i_missing) + " / " + str(nc_voter_i) + "   " + str(division(nc_voter_i_missing, nc_voter_i)* 100) + "% missing")
# print("\' \': " + str(nc_voter_empty_missing) + " / " + str(nc_voter_empty) + "   " + str(division(nc_voter_empty_missing, nc_voter_empty)* 100) + "% missing")
# print("nan: " + str(nc_voter_nan_missing) + " / " + str(nc_voter_nan) + "   " + str(division(nc_voter_nan_missing, nc_voter_nan)* 100) + "% missing")

# print("NL: " + str(nc_voter_nl_missing) + " / " + str(nc_voter_w) + "   " + str(division(nc_voter_w_missing, nc_voter_w)* 100) + "% missing")
# print("UN: " + str(nc_voter_un_missing) + " / " + str(nc_voter_b) + "   " + str(division(nc_voter_b_missing, nc_voter_b)* 100) + "% missing")
# print("HL: " + str(nc_voter_hl_missing) + " / " + str(nc_voter_u) + "   " + str(division(nc_voter_u_missing, nc_voter_u)* 100) + "% missing")
# print("eth nan: " + str(nc_voter_eth_nan_missing) + " / " + str(nc_voter_eth_nan) + "   " + str(division(nc_voter_eth_nan_missing, nc_voter_eth_nan)* 100) + "% missing")

# print("W NL: " + str(w_nl) + " / " + str(w_nl_missing) + "   " + str(division(w_nl_missing, w_nl)* 100) + "% missing")
# print("W UN: " + str(w_un) + " / " + str(w_un_missing) + "   " + str(division(w_un_missing, w_un)* 100) + "% missing")
# print("W HL: " + str(w_hl) + " / " + str(w_hl_missing) + "   " + str(division(w_hl_missing, w_hl)* 100) + "% missing")
# print("W nan: " + str(w_eth_nan) + " / " + str(w_eth_nan_missing) + "   " + str(division(w_eth_nan_missing, w_eth_nan)* 100) + "% missing")

# print("B NL: " + str(b_nl) + " / " + str(b_nl_missing) + "   " + str(division(b_nl_missing, b_nl)* 100) + "% missing")
# print("B UN: " + str(b_un) + " / " + str(b_un_missing) + "   " + str(division(b_un_missing, b_un)* 100) + "% missing")
# print("B HL: " + str(b_hl) + " / " + str(b_hl_missing) + "   " + str(division(b_hl_missing, b_hl)* 100) + "% missing")
# print("B nan: " + str(b_eth_nan) + " / " + str(b_eth_nan_missing) + "   " + str(division(b_eth_nan_missing, b_eth_nan)* 100) + "% missing")

# print("U NL: " + str(u_nl) + " / " + str(u_nl_missing) + "   " + str(division(u_nl_missing, u_nl)* 100) + "% missing")
# print("U UN: " + str(u_un) + " / " + str(u_un_missing) + "   " + str(division(u_un_missing, u_un)* 100) + "% missing")
# print("U HL: " + str(u_hl) + " / " + str(u_hl_missing) + "   " + str(division(u_hl_missing, u_hl)* 100) + "% missing")
# print("U nan: " + str(u_eth_nan) + " / " + str(u_eth_nan_missing) + "   " + str(division(u_eth_nan_missing, u_eth_nan)* 100) + "% missing")

# print("O NL: " + str(o_nl) + " / " + str(o_nl_missing) + "   " + str(division(o_nl_missing, o_nl)* 100) + "% missing")
# print("O UN: " + str(o_un) + " / " + str(o_un_missing) + "   " + str(division(o_un_missing, o_un)* 100) + "% missing")
# print("O HL: " + str(o_hl) + " / " + str(o_hl_missing) + "   " + str(division(o_hl_missing, o_hl)* 100) + "% missing")
# print("O nan: " + str(o_eth_nan) + " / " + str(o_eth_nan_missing) + "   " + str(division(o_eth_nan_missing, o_eth_nan)* 100) + "% missing")

# print("A NL: " + str(a_nl) + " / " + str(a_nl_missing) + "   " + str(division(a_nl_missing, a_nl)* 100) + "% missing")
# print("A UN: " + str(a_un) + " / " + str(a_un_missing) + "   " + str(division(a_un_missing, a_un)* 100) + "% missing")
# print("A HL: " + str(a_hl) + " / " + str(a_hl_missing) + "   " + str(division(a_hl_missing, a_hl)* 100) + "% missing")
# print("A nan: " + str(a_eth_nan) + " / " + str(a_eth_nan_missing) + "   " + str(division(a_eth_nan_missing, a_eth_nan)* 100) + "% missing")

# print("M NL: " + str(m_nl) + " / " + str(m_nl_missing) + "   " + str(division(m_nl_missing, m_nl)* 100) + "% missing")
# print("M UN: " + str(m_un) + " / " + str(m_un_missing) + "   " + str(division(m_un_missing, m_un)* 100) + "% missing")
# print("M HL: " + str(m_hl) + " / " + str(m_hl_missing) + "   " + str(division(m_hl_missing, m_hl)* 100) + "% missing")
# print("M nan: " + str(m_eth_nan) + " / " + str(m_eth_nan_missing) + "   " + str(division(m_eth_nan_missing, m_eth_nan)* 100) + "% missing")

# print("I NL: " + str(i_nl) + " / " + str(i_nl_missing) + "   " + str(division(i_nl_missing, i_nl)* 100) + "% missing")
# print("I UN: " + str(i_un) + " / " + str(i_un_missing) + "   " + str(division(i_un_missing, i_un)* 100) + "% missing")
# print("I HL: " + str(i_hl) + " / " + str(i_hl_missing) + "   " + str(division(i_hl_missing, i_hl)* 100) + "% missing")
# print("I nan: " + str(i_eth_nan) + " / " + str(i_eth_nan_missing) + "   " + str(division(i_eth_nan_missing, i_eth_nan)* 100) + "% missing")

# print("empty NL: " + str(empty_nl) + " / " + str(empty_nl_missing) + "   " + str(division(empty_nl_missing, empty_nl)* 100) + "% missing")
# print("empty UN: " + str(empty_un) + " / " + str(empty_un_missing) + "   " + str(division(empty_un_missing, empty_un)* 100) + "% missing")
# print("empty HL: " + str(empty_hl) + " / " + str(empty_hl_missing) + "   " + str(division(empty_hl_missing, empty_hl)* 100) + "% missing")
# print("empty nan: " + str(empty_eth_nan) + " / " + str(empty_eth_nan_missing) + "   " + str(division(empty_eth_nan_missing, empty_eth_nan)* 100) + "% missing")

# print("nan NL: " + str(nan_nl) + " / " + str(nan_nl_missing) + "   " + str(division(nan_nl_missing, nan_nl)* 100) + "% missing")
# print("nan UN: " + str(nan_un) + " / " + str(nan_un_missing) + "   " + str(division(nan_un_missing, nan_un)* 100) + "% missing")
# print("nan HL: " + str(nan_hl) + " / " + str(nan_hl_missing) + "   " + str(division(nan_hl_missing, nan_hl)* 100) + "% missing")
# print("nan nan: " + str(nan_eth_nan) + " / " + str(nan_eth_nan_missing) + "   " + str(division(nan_eth_nan_missing, nan_eth_nan)* 100) + "% missing")