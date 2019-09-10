import pandas as pd
import numpy as np

print('*** Program Started ***')

df = pd.read_csv('rainfall-master.csv')

# ensuring only equity series is considered
# df = df.loc[df['Series'] == 'EQ']

# Converting date to pandas datetime format
df['Date'] = pd.to_datetime(df['Date'])
# Getting month number
df['Month_Number'] = df['Date'].dt.month
# Getting year. month is common across years (as if you dont know :) )to we need to create unique index by using year and month
df['Year'] = df['Date'].dt.year

# Grouping based on required values
df2 = df.groupby(['Year','Month_Number']).agg({'ET':'sum','EP':'sum','BSS':'sum','RF':'sum','WS':'sum','DT1':'sum','WT1':'sum','DT2':'sum','WT2':'sum','MAXT':'sum','MINT':'sum','RH11':'sum','RH22':'sum','VP11':'sum','VP11':'sum','CLOUDM':'sum','CLOUDE':'sum','SOIL1':'sum','SOIL2':'sum','SOIL3':'sum','SOIL4':'sum','SOIL5':'sum','SOIL6':'sum','MinTtest':'sum','MaxTtest1':'sum','MaxTtest2':'sum'})
#df2 = df.groupby(['Year','Week_Number']).agg({'ET':'sum','EP':'sum','BSS':'sum','RF':'sum','WS':'sum','DT1':'sum','WT1':'sum','DT2':'sum','WT2':'sum','MAXT':'sum','MINT':'sum','RH11':'sum','RH22':'sum','VP11':'sum','VP11':'sum','CLOUDM':'sum','CLOUDE':'sum','SOIL1':'sum','SOIL2':'sum','SOIL3':'sum','SOIL4':'sum','SOIL5':'sum','SOIL6':'sum','MinTtest':'sum','MaxTtest1':'sum','MaxTtest2':'sum'})
print(df2)
print('*** Program ended ***')