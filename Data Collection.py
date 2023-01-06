# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 15:55:22 2023

@author: chloe
"""

import numpy as np
import pandas as pd

# get data
import pandas_datareader as pdr

# visual
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

#time
import datetime as datetime
start = datetime.datetime(2019,1,5)
end =datetime.datetime(2022,1,5)
df_2330 = pdr.DataReader('2330.TW', 'yahoo', start=start,end=end)
df_2330['week_return']=df_2330['Close'].pct_change(5)
df_2454 = pdr.DataReader('2454.TW', 'yahoo', start=start,end=end)
df_2454['week_return']=df_2454['Close'].pct_change(5)
df_2303 = pdr.DataReader('2303.TW', 'yahoo', start=start,end=end)
df_2303['week_return']=df_2303['Close'].pct_change(5)
df_3711 = pdr.DataReader('3711.TW', 'yahoo', start=start,end=end)
df_3711['week_return']=df_3711['Close'].pct_change(5)
df_2379 = pdr.DataReader('2379.TW', 'yahoo', start=start,end=end)
df_2379['week_return']=df_2379['Close'].pct_change(5)
df_6488 = pdr.DataReader('6488.TWO', 'yahoo', start=start,end=end)
df_6488['week_return']=df_6488['Close'].pct_change(5)
df_5483 = pdr.DataReader('5483.TWO', 'yahoo', start=start,end=end)
df_5483['week_return']=df_5483['Close'].pct_change(5)
df_3105 = pdr.DataReader('3105.TWO', 'yahoo', start=start,end=end)
df_3105['week_return']=df_3105['Close'].pct_change(5)
df_2344 = pdr.DataReader('2344.TW', 'yahoo', start=start,end=end)
df_2344['week_return']=df_2344['Close'].pct_change(5)
df_2408 = pdr.DataReader('2408.TW', 'yahoo', start=start,end=end)
df_2408['week_return']=df_2408['Close'].pct_change(5)
# Specify the name of the excel file
file_name = 'C:/Users/chloe/Desktop/data/2330.xlsx'
file_name1 = 'C:/Users/chloe/Desktop/data/2454.xlsx'
file_name2 = 'C:/Users/chloe/Desktop/data/2303.xlsx'
file_name3 = 'C:/Users/chloe/Desktop/data/3711.xlsx'
file_name4 = 'C:/Users/chloe/Desktop/data/2379.xlsx'
file_name5 = 'C:/Users/chloe/Desktop/data/6488.xlsx'
file_name6 = 'C:/Users/chloe/Desktop/data/5483.xlsx'
file_name7 = 'C:/Users/chloe/Desktop/data/3105.xlsx'
file_name8 = 'C:/Users/chloe/Desktop/data/2344.xlsx'
file_name9 = 'C:/Users/chloe/Desktop/data/2408.xlsx'
  
# saving the excelsheet
df_2330.to_excel(file_name)
df_2454.to_excel(file_name1)
df_2303.to_excel(file_name2)
df_3711.to_excel(file_name3)
df_2379.to_excel(file_name4)
df_6488.to_excel(file_name5)
df_5483.to_excel(file_name6)
df_3105.to_excel(file_name7)
df_2344.to_excel(file_name8)
df_2408.to_excel(file_name9)


for stock in [df_2330, df_2454, df_2303, df_3711, df_2379, df_6488, df_5483, df_3105, df_2344, df_2408, ]:
    stock['normalized_price']=stock['Adj Close']/stock['Adj Close'].iloc[0]
for stock, weight in zip([df_2330, df_2454, df_2303, df_3711, df_2379, df_6488, df_5483, df_3105, df_2344, df_2408, ],[0.25562, 0.15222, 0.12092, 0.10692, 0.08092, 0.07322, 0.05712, 0.05282, 0.05052, 0.04972]):
    stock['weighted daily return']=stock['normalized_price']*weight
df_total=pd.concat([df_2330['weighted daily return'], df_2454['weighted daily return'], df_2303['weighted daily return'], df_3711['weighted daily return'],df_2379['weighted daily return'],df_6488['weighted daily return'],df_5483['weighted daily return'],df_3105['weighted daily return'],df_2344['weighted daily return'],df_2408['weighted daily return']],axis=1)
df_total.columns=['2330', '2454', '2303', '3711', '2379', '6488', '5483', '3105', '2344', '2408']    
df_total_money = df_total* 100000
df_total_money['Total Pos']=df_total_money.sum(axis=1)
df_total_money.head()
fig = plt.figure(figsize=(10, 6))
plt.plot(df_total_money['Total Pos'], '-' , label="total revenue")
plt.plot(df_total_money['2330'], '-' , label="2330")
plt.plot(df_total_money['2454'], '-' , label="2454")
plt.plot(df_total_money['2303'], '-' , label="2303")
plt.plot(df_total_money['3711'], '-' , label="3711")
plt.plot(df_total_money['2379'], '-' , label="2379")
plt.plot(df_total_money['6488'], '-' , label="6488")
plt.plot(df_total_money['5483'], '-' , label="5483")
plt.plot(df_total_money['3105'], '-' , label="3105")
plt.plot(df_total_money['2344'], '-' , label="2344")
plt.plot(df_total_money['2408'], '-' , label="2408")

plt.title('收益曲線',loc='right')

plt.xlabel('日期')
plt.ylabel('金額')
plt.grid(True, axis='y')
plt.legend(loc="upper right")
df_total_money['daily return']=df_total_money['Total Pos'].pct_change()
print("累積收益率",df_total_money['Total Pos'].iloc[-1]/df_total_money['Total Pos'].iloc[0]-1)
print("平均收益率：",df_total_money['daily return'].mean())
print("收益率標準差：",df_total_money['daily return'].std())
plt.rcParams['axes.unicode_minus']=False
fig = plt.figure(figsize=(10, 6))
sns.distplot(df_total_money['daily return'].dropna(),bins=100, label="總收益率")
plt.legend()
SR=df_total_money['daily return'].mean()/df_total_money['daily return'].std()
print("夏普指數",SR)
ASR=np.sqrt(252)*SR