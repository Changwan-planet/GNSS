import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import csv
import os

#path and input
path = os.path.dirname(os.path.realpath(__file__))
filename = input('Enter your filename \n')
input_path = path + "/" + filename +".gga"
 


data=np.loadtxt(input_path)

col_name = ['Index','Lat', 'Long', 'Elp_H', 'Geoid_H']
data_2 = pd.DataFrame(data, columns = col_name)

#print(data_2.head)

str_lat, str_long = [], []
str_lat, str_long = [0] * len(data_2), [0] * len(data_2)

str_sum =[]
str_sum = [0] * len(data_2)

str_sum2 =[]
str_sum2 = [0] * len(data_2)


d_lat_1, d_lat_2, d_lat_3 = [], [], []
d_lat_1, d_lat_2, d_lat_3 = [0] * len(data_2), [0] * len(data_2), [0] * len(data_2)

d_long_1, d_long_2, d_long_3 = [], [], []
d_long_1, d_long_2, d_long_3 = [0] * len(data_2), [0] * len(data_2), [0] * len(data_2)

degree_lat, degree_long = [], []
degree_lat, degree_long = [0] * len(data_2), [0] * len(data_2)


#print(rows)

for row in range(len(data_2)):
 str_lat[row] = str(data_2.iloc[row]['Lat'])
 str_long[row] = str(data_2.iloc[row]['Long'])
# print(str_lat[row], str_long[row])


for row in range(len(data_2)):

 str_sum[row] = str_lat[row][5:7] + "." + str_lat[row][7:]
 str_sum2[row] = str_long[row][6:8] + "." + str_long[row][8:]


 #DEGREE
 d_lat_1[row] = float(str_lat[row][0:2])
 d_lat_2[row] = float(str_lat[row][3:5])
 d_lat_3[row] = float(str_sum[row])
 
 d_long_1[row] = float(str_long[row][0:3])
 d_long_2[row] = float(str_long[row][4:6])
 d_long_3[row] = float(str_sum2[row])


 degree_lat[row] = d_lat_1[row] + d_lat_2[row]/60.0 + d_lat_3[row]/3600.0
# degree_lat[row] = round(degree_lat[row],6)
  
 degree_long[row] = d_long_1[row] + d_long_2[row]/60.0 + d_long_3[row]/3600.0
# degree_long[row] = round(degree_long[row],12)


#MEAN
#"""
mdgr_lat = []
mdgr_lat = [0] * int(len(data_2)/2)

mdgr_long = []
mdgr_long = [0] * int(len(data_2)/2)


row2 = 0
mdgr_lat[row2] = (degree_lat[row2] + degree_lat[row2+1]) / 2.0
mdgr_long[row2] = (degree_long[row2] + degree_long[row2+1]) / 2.0

for row2 in range(1,int(len(data_2)/2.0),1):
    print(row2, row2+1, row2+2)
    mdgr_lat[row2] = (degree_lat[2*row2] + degree_lat[2*row2+1]) / 2.0
    mdgr_long[row2] = (degree_long[2*row2] + degree_long[2*row2+1]) / 2.0


td = { 
      'lat_degree': mdgr_lat,
      'long_degree': mdgr_long
}
#"""


#DATAFRAM FROM TOW LISTS
"""
td = { 
      'lat_degree': degree_lat,
      'long_degree':degree_long
}    
"""
dgr_lat_long = pd.DataFrame(td)

print(dgr_lat_long)
#CSV
filename_out = filename + "_dgr" + '.csv'
dgr_lat_long.to_csv(filename_out,sep=',',na_rep='NaN') 

