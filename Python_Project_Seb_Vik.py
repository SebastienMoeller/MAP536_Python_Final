#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:43:35 2017

@author: Sebastien
"""

#%% All libraries
import poloniex
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from pytrends.request import TrendReq
import numpy as np

#%% Importing from API
# To import poloniex we need to install the package in the console using:
# pip install poloniex
# help(poloniex.poloniex)

# We are using the public data so no keys are needed
polo = poloniex.Poloniex()
# Transform data into a dataframe
# "period" (candlestick period in seconds; valid values
#     |      are 300, 900, 1800, 7200, 14400, and 86400), "start", and "end".
#     |      "Start" and "end" are given in UNIX timestamp format and used to
#     |      specify the date range for the data returned.
# 86400 = 24 hours
# 300 = 5 minutes
#doge = pandas.DataFrame(polo.returnChartData("BTC_DOGE", 86400))
btc300 = pd.DataFrame(polo.returnChartData("USDT_BTC", 300))
btc86400 = pd.DataFrame(polo.returnChartData("USDT_BTC", 86400))

#%%
print("Start date 5 minute")
print(datetime.datetime.fromtimestamp(btc300["date"][0]))
print("End date 5 minute")
print(datetime.datetime.fromtimestamp(btc300["date"][len(btc300)-1]))


print("Start date daily")
print(datetime.datetime.fromtimestamp(btc86400["date"][0]))
print("End date daily")
print(datetime.datetime.fromtimestamp(btc86400["date"][len(btc86400)-1]))

# ["date"][(4+i)*12-2], i is the hour

# Convert datetime from timestamp to a recognizable format
#for i in range(len(btc300)):
#   btc300["date"][i] = datetime.datetime.fromtimestamp(btc300["date"][i])

#%%
btc300.columns

#%%
btc300.describe()

#%%
btc300.dtypes

#%% View Data 5 minutes
fig = plt.figure()

axes1 = fig.add_axes([0.05, 0.2, 1.2, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.6, 0.3]) # inset axes

# main figure
axes1.plot(btc300["date"], btc300["volume"]/btc300["volume"].max(), "#0CC88F")
axes1.plot(btc300["date"], btc300["close"]/btc300["close"].max(), '#EBA911')

axes1.legend(loc=2)
axes1.set_xlabel('date')
axes1.set_ylabel('Max')
axes1.set_title('Last Three Years')

# insert
axes2.plot(btc300["date"][-30*12*24:], btc300["volume"][-30*12*24:]/btc300["volume"][-30*12*24:].max(), '#0CC88F')
axes2.plot(btc300["date"][-30*12*24:], btc300["close"][-30*12*24:]/btc300["close"][-30*12*24:].max(), '#EBA911')

axes2.set_xlabel('date')
axes2.set_ylabel('Max')
axes2.set_title('Last 30 Days');
#%%

#%% View Data daily
fig = plt.figure()

axes1 = fig.add_axes([0.05, 0.2, 1.2, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.6, 0.3]) # inset axes

# main figure
axes1.plot(btc86400["date"], btc86400["volume"]/btc86400["volume"].max(), "#0CC88F")
axes1.plot(btc86400["date"], btc86400["close"]/btc86400["close"].max(), '#EBA911')

axes1.legend(loc=2)
axes1.set_xlabel('date')
axes1.set_ylabel('Max')
axes1.set_title('Last Three Years')

# insert
axes2.plot(btc86400["date"][-30:], btc86400["volume"][-30:]/btc86400["volume"][-30:].max(), '#0CC88F')
axes2.plot(btc86400["date"][-30:], btc86400["close"][-30:]/btc86400["close"][-30:].max(), '#EBA911')

axes2.set_xlabel('date')
axes2.set_ylabel('Max')
axes2.set_title('Last 30 Days');
#%%





#%% GOOGLE TRENDS
pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["Blockchain", "BTC", "BitCoin"]
pytrends.build_payload(kw_list)
#%%
trends = pytrends.interest_over_time()
#%%
trends.columns
#%%
trends.describe()
#%%
trends.dtypes
#%%
pytrends = TrendReq(hl='en-US', tz=360)

pytrends.build_payload(["Blockchain"])
tblockchain = pytrends.interest_over_time()
pytrends.build_payload(["BTC"])
tbtc = pytrends.interest_over_time()
pytrends.build_payload(["BitCoin"])
tbitcoin = pytrends.interest_over_time()
#%%
fig = plt.figure()

axes1 = fig.add_axes([0.05, 0.2, 1.2, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.6, 0.3]) # inset axes

# main figure
axes1.plot(tbitcoin["BitCoin"]/tbitcoin["BitCoin"].max())
axes1.plot(tblockchain["Blockchain"]/tblockchain["Blockchain"].max())
axes1.plot(tbtc["BTC"]/tbtc["BTC"].max())

axes1.legend(loc=2)
axes1.set_xlabel('date')
axes1.set_ylabel('Max')
axes1.set_title('Last Five Years')

# insert
axes2.plot(tbitcoin["BitCoin"][-30:]/tbitcoin["BitCoin"][-30:].max())
axes2.plot(tblockchain["Blockchain"][-30:]/tblockchain["Blockchain"][-30:].max())
axes2.plot(tbtc["BTC"][-30:]/tbtc["BTC"][-30:].max())

axes2.set_xlabel('date')
axes2.set_ylabel('Max')
axes2.set_title('Last 30 Days');
#%%





#%% Does the daily change follow a normal distribution?
closeDiff = pd.DataFrame(np.diff(btc86400["close"]))
#%%
closeDiff.plot()
#%%
closeDiff[0:650].plot()
#%%
closeDiff[650:1000].plot()
#%%
closeDiff[1000:].plot()
#%%
plt.hist(closeDiff[850:], bins = 30)
#%%





#%%
price = pd.DataFrame(btc86400["close"])
#%%
price["pct_change"] = price.close.pct_change()
#%%
price["log_return"] = np.log(price.close) - np.log(price.close.shift(1))
#%%
price["log_return"].plot()
#%%
price.describe()
#%%






#%% Representing the data as daily japanese candles sticks

# NOTHING WORKS!!! 


import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Candlestick(x=btc86400, open=btc86400['open'], high=btc86400['high'], low=btc86400['low'], 
                       close=btc86400['close'],
                       increasing=dict(line=dict(color= '#17BECF')),
                       decreasing=dict(line=dict(color= '#7F7F7F')))
                                                 
data = [trace]

fig = dict(data=data)
py.iplot(fig, filename='styled_candlestick')
#%%
import pandas_datareader.data as web

web.DataReader("aapl")
#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%




