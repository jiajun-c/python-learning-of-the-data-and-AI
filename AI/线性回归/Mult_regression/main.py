import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('./Fish.csv')
df = data.copy()
df.sample(10)

"""
    Species  Weight  Length1  Length2  Length3   Height   Width
137       Pike   500.0     42.0     45.0     48.0   6.9600  4.8960
67      Parkki   170.0     19.0     20.7     23.2   9.3960  3.4104
113      Perch   700.0     34.0     36.0     38.3  10.6091  6.7408
10       Bream   475.0     28.4     31.0     36.2  14.2628  5.1042
28       Bream   850.0     32.8     36.0     41.6  16.8896  6.1984
60   Whitefish  1000.0     37.3     40.0     43.5  12.3540  6.5250
89       Perch   135.0     20.0     22.0     23.5   5.8750  3.5250
74       Perch    40.0     13.8     15.0     16.0   3.8240  2.4320
79       Perch    80.0     17.2     19.0     20.2   5.6358  3.0502
65      Parkki   150.0     18.4     20.0     22.4   8.8928  3.2928

"""
df.rename(columns={'Length1': 'LengthVer', 'Length2': 'LengthDia', 'Length3': 'LengthCro'}, inplace=True)
df.head()
"""
  Species  Weight  LengthVer  LengthDia  LengthCro   Height   Width
0   Bream   242.0       23.2       25.4       30.0  11.5200  4.0200
1   Bream   290.0       24.0       26.3       31.2  12.4800  4.3056
2   Bream   340.0       23.9       26.5       31.1  12.3778  4.6961
3   Bream   363.0       26.3       29.0       33.5  12.7300  4.4555
4   Bream   430.0       26.5       29.0       34.0  12.4440  5.1340
"""
# using the value counts in the sp you will get the statistic in this column
sp = df['Species'].value_counts()
sp = pd.DataFrame(sp)

# it draw the picture of the 
plt.xlabel('species')
plt.ylabel('count of the species')
num = sp['Species']
plt.bar(sp.index, num)
plt.savefig("./img/Species_num.png")


