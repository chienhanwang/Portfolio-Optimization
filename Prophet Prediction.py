# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 20:27:00 2022

@author: samuel
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader as pdr
import pandas as pd
import requests, json
import datetime as dt
df_2303 = pd.read_excel('2303.xlsx')
df_2330 = pd.read_excel('2330.xlsx')
df_2344 = pd.read_excel('2344.xlsx')
df_2379 = pd.read_excel('2379.xlsx')
df_2408 = pd.read_excel('2408.xlsx')
df_2454 = pd.read_excel('2454.xlsx')
df_3105 = pd.read_excel('3105.xlsx')
df_3711 = pd.read_excel('3711.xlsx')
df_5483 = pd.read_excel('5483.xlsx')
df_6488 = pd.read_excel('6488.xlsx')
# Create a copy to avoid the SettingWarning .loc issue 
amzn_df_2303 = df_2303.copy()
amzn_df_2303.info()
amzn_df_2330 = df_2330.copy()
amzn_df_2330.info()
amzn_df_2344 = df_2344.copy()
amzn_df_2344.info()
amzn_df_2379 = df_2379.copy()
amzn_df_2379.info()
amzn_df_2408 = df_2408.copy()
amzn_df_2408.info()
amzn_df_2454 = df_2454.copy()
amzn_df_2454.info()
amzn_df_3105 = df_3105.copy()
amzn_df_3105.info()
amzn_df_3711 = df_3711.copy()
amzn_df_3711.info()
amzn_df_5483 = df_5483.copy()
amzn_df_5483.info()
amzn_df_6488 = df_6488.copy()
amzn_df_6488.info()

df1_2303 = amzn_df_2303.drop(['High', 'Low', 'Open','Volume', 'Adj Close'], axis=1)
df1_2303.rename(columns={'Close': 'y', 'Date': 'ds'}, inplace=True)
df1_2330 = amzn_df_2330.drop(['High', 'Low', 'Open','Volume', 'Adj Close'], axis=1)
df1_2330.rename(columns={'Close': 'y', 'Date': 'ds'}, inplace=True)
df1_2344 = amzn_df_2344.drop(['High', 'Low', 'Open','Volume', 'Adj Close'], axis=1)
df1_2344.rename(columns={'Close': 'y', 'Date': 'ds'}, inplace=True)
df1_2379 = amzn_df_2379.drop(['High', 'Low', 'Open','Volume', 'Adj Close'], axis=1)
df1_2379.rename(columns={'Close': 'y', 'Date': 'ds'}, inplace=True)
df1_2408 = amzn_df_2408.drop(['High', 'Low', 'Open','Volume', 'Adj Close'], axis=1)
df1_2408.rename(columns={'Close': 'y', 'Date': 'ds'}, inplace=True)
df1_2454 = amzn_df_2454.drop(['High', 'Low', 'Open','Volume', 'Adj Close'], axis=1)
df1_2454.rename(columns={'Close': 'y', 'Date': 'ds'}, inplace=True)
df1_3105 = amzn_df_3105.drop(['High', 'Low', 'Open','Volume', 'Adj Close'], axis=1)
df1_3105.rename(columns={'Close': 'y', 'Date': 'ds'}, inplace=True)
df1_3711 = amzn_df_3711.drop(['High', 'Low', 'Open','Volume', 'Adj Close'], axis=1)
df1_3711.rename(columns={'Close': 'y', 'Date': 'ds'}, inplace=True)
df1_5483 = amzn_df_5483.drop(['High', 'Low', 'Open','Volume', 'Adj Close'], axis=1)
df1_5483.rename(columns={'Close': 'y', 'Date': 'ds'}, inplace=True)
df1_6488 = amzn_df_6488.drop(['High', 'Low', 'Open','Volume', 'Adj Close'], axis=1)
df1_6488.rename(columns={'Close': 'y', 'Date': 'ds'}, inplace=True)

df1_2303.loc[:, 'ds'] = pd.to_datetime(df_2303.loc[:,'Date'], format="%Y/%m/%d")
df1_2330.loc[:, 'ds'] = pd.to_datetime(df_2330.loc[:,'Date'], format="%Y/%m/%d")
df1_2344.loc[:, 'ds'] = pd.to_datetime(df_2344.loc[:,'Date'], format="%Y/%m/%d")
df1_2379.loc[:, 'ds'] = pd.to_datetime(df_2379.loc[:,'Date'], format="%Y/%m/%d")
df1_2408.loc[:, 'ds'] = pd.to_datetime(df_2408.loc[:,'Date'], format="%Y/%m/%d")
df1_2454.loc[:, 'ds'] = pd.to_datetime(df_2454.loc[:,'Date'], format="%Y/%m/%d")
df1_3105.loc[:, 'ds'] = pd.to_datetime(df_3105.loc[:,'Date'], format="%Y/%m/%d")
df1_3711.loc[:, 'ds'] = pd.to_datetime(df_3711.loc[:,'Date'], format="%Y/%m/%d")
df1_5483.loc[:, 'ds'] = pd.to_datetime(df_5483.loc[:,'Date'], format="%Y/%m/%d")
df1_6488.loc[:, 'ds'] = pd.to_datetime(df_6488.loc[:,'Date'], format="%Y/%m/%d")

!pip install pystan~=2.14
!pip install fbprophet
from fbprophet import Prophet
df1_2303.daily_seasonality = True
m1 = Prophet()
m1.fit(df1_2303)
df1_2330.daily_seasonality = True
m2 = Prophet()
m2.fit(df1_2330)
df1_2344.daily_seasonality = True
m3 = Prophet()
m3.fit(df1_2344)
df1_2379.daily_seasonality = True
m4 = Prophet()
m4.fit(df1_2379)
df1_2408.daily_seasonality = True
m5 = Prophet()
m5.fit(df1_2408)
df1_2454.daily_seasonality = True
m6 = Prophet()
m6.fit(df1_2454)
df1_3105.daily_seasonality = True
m7 = Prophet()
m7.fit(df1_3105)
df1_3711.daily_seasonality = True
m8 = Prophet()
m8.fit(df1_3711)
df1_5483.daily_seasonality = True
m9 = Prophet()
m9.fit(df1_5483)
df1_6488.daily_seasonality = True
m10 = Prophet()
m10.fit(df1_6488)

# Create Future dates
future_prices = m1.make_future_dataframe(periods=5, freq='B')

# Predict Prices
forecast = m1.predict(future_prices)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

import matplotlib.dates as mdates

# Learn more Prophet tomorrow and plot the forecast for amazon.
fig = m1.plot(forecast)
ax1 = fig.add_subplot(111)
ax1.set_title("2303 Stock Price Forecast", fontsize=16)
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Close Price", fontsize=12)

plt.show()

# Create Future dates
future_prices = m2.make_future_dataframe(periods=5, freq='B')

# Predict Prices
forecast = m2.predict(future_prices)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

import matplotlib.dates as mdates

# Learn more Prophet tomorrow and plot the forecast for amazon.
fig = m2.plot(forecast)
ax1 = fig.add_subplot(111)
ax1.set_title("2330 Stock Price Forecast", fontsize=16)
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Close Price", fontsize=12)

plt.show()

# Create Future dates
future_prices = m3.make_future_dataframe(periods=5, freq='B')

# Predict Prices
forecast = m3.predict(future_prices)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

import matplotlib.dates as mdates

# Learn more Prophet tomorrow and plot the forecast for amazon.
fig = m3.plot(forecast)
ax1 = fig.add_subplot(111)
ax1.set_title("2344 Stock Price Forecast", fontsize=16)
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Close Price", fontsize=12)

plt.show()
# Create Future dates
future_prices = m4.make_future_dataframe(periods=5, freq='B')

# Predict Prices
forecast = m4.predict(future_prices)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

import matplotlib.dates as mdates

# Learn more Prophet tomorrow and plot the forecast for amazon.
fig = m4.plot(forecast)
ax1 = fig.add_subplot(111)
ax1.set_title("2379 Stock Price Forecast", fontsize=16)
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Close Price", fontsize=12)

plt.show()
# Create Future dates
future_prices = m5.make_future_dataframe(periods=5, freq='B')

# Predict Prices
forecast = m5.predict(future_prices)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

import matplotlib.dates as mdates

# Learn more Prophet tomorrow and plot the forecast for amazon.
fig = m5.plot(forecast)
ax1 = fig.add_subplot(111)
ax1.set_title("2408 Stock Price Forecast", fontsize=16)
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Close Price", fontsize=12)

plt.show()

# Create Future dates
future_prices = m6.make_future_dataframe(periods=5, freq='B')

# Predict Prices
forecast = m6.predict(future_prices)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

import matplotlib.dates as mdates

# Learn more Prophet tomorrow and plot the forecast for amazon.
fig = m6.plot(forecast)
ax1 = fig.add_subplot(111)
ax1.set_title("2454 Stock Price Forecast", fontsize=16)
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Close Price", fontsize=12)

plt.show()

# Create Future dates
future_prices = m7.make_future_dataframe(periods=5, freq='B')

# Predict Prices
forecast = m7.predict(future_prices)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

import matplotlib.dates as mdates

# Learn more Prophet tomorrow and plot the forecast for amazon.
fig = m7.plot(forecast)
ax1 = fig.add_subplot(111)
ax1.set_title("3105 Stock Price Forecast", fontsize=16)
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Close Price", fontsize=12)

plt.show()

# Create Future dates
future_prices = m8.make_future_dataframe(periods=5, freq='B')

# Predict Prices
forecast = m8.predict(future_prices)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

import matplotlib.dates as mdates

# Learn more Prophet tomorrow and plot the forecast for amazon.
fig = m8.plot(forecast)
ax1 = fig.add_subplot(111)
ax1.set_title("3711 Stock Price Forecast", fontsize=16)
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Close Price", fontsize=12)

plt.show()

# Create Future dates
future_prices = m9.make_future_dataframe(periods=5, freq='B')

# Predict Prices
forecast = m9.predict(future_prices)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

import matplotlib.dates as mdates

# Learn more Prophet tomorrow and plot the forecast for amazon.
fig = m9.plot(forecast)
ax1 = fig.add_subplot(111)
ax1.set_title("5483 Stock Price Forecast", fontsize=16)
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Close Price", fontsize=12)

plt.show()

# Create Future dates
future_prices = m10.make_future_dataframe(periods=5, freq='B')

# Predict Prices
forecast = m10.predict(future_prices)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

import matplotlib.dates as mdates

# Learn more Prophet tomorrow and plot the forecast for amazon.
fig = m10.plot(forecast)
ax1 = fig.add_subplot(111)
ax1.set_title("6488 Stock Price Forecast", fontsize=16)
ax1.set_xlabel("Date", fontsize=12)
ax1.set_ylabel("Close Price", fontsize=12)

plt.show()





















































