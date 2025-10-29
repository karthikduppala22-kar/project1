import os
import numpy as np
import pandas as pd
df=pd.read_csv('stock_file.txt')
print(df)
print(df.columns)


df['Date']=pd.to_datetime(df['Date'])
df['Date']=df['Date'].dt.strftime('%Y%m%d').astype(int)


coln=['Open','High','Low','Close','Volume']
df[coln]=df[coln].replace(['zero','NaN','Null','-','missing'],pd.NA)

for x in coln :
    if df[x].dtype=='object':
       df[x]=pd.to_numeric(df[x],errors='coerce')

    df[x]=df[x].fillna(df[x].mean().round(2))


df[coln]=df[coln].astype(float).round(2)
print(df.head())
#karthik mike

