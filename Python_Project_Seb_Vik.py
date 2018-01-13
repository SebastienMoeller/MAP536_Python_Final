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
from matplotlib.finance import candlestick2_ohlc
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
#for i in range(len(btc86400)):
#   btc86400["date"][i] = datetime.datetime.fromtimestamp(btc86400["date"][i])
#%%
btc300.columns
#%%
btc300.describe()
#%%
btc300.dtypes
#%%
def multiPlot(data, x, y, factor):
    fig = plt.figure()
    
    axes1 = fig.add_axes([0.05, 0.2, 1.2, 0.8]) # main axes
    axes2 = fig.add_axes([0.2, 0.5, 0.6, 0.3]) # inset axes

    # main figure
    for i in range(len(y)):
        axes1.plot(data[x], data[y[i]]/data[y[i]].max())

    axes1.legend(loc=2)
    axes1.set_xlabel(x)
    axes1.set_ylabel('Max')

    # insert
    for i in range(len(y)):
        axes2.plot(data[x][-30*factor:], data[y[i]][-30*factor:]/data[y[i]][-30*factor:].max())

    axes2.set_xlabel(x)
    axes2.set_ylabel('Max');
#%%
# View Data 5 minutes
multiPlot(btc300, 'date', ('volume','close'), 12*24)
# View Data daily
multiPlot(btc86400, 'date', ('volume','close'), 1)
#%% Representing the data as daily japanese candles sticks
fig, ax = plt.subplots()
candlestick2_ohlc(ax,btc86400['open'][-30:],btc86400['high'][-30:],btc86400['low'][-30:],btc86400['close'][-30:],width=0.6)
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





#%% Function to retrieve trends with maximum available accuracy from Google, of a list of 
# terms to look up, concatenated into one matrix containing a date column
def payload(strings):
    pytrends = TrendReq(hl='en-US', tz=360)
    
    trend = []
    
    for i in range(len(strings)):
        pytrends.build_payload([strings[i]])
        trend.append(pytrends.interest_over_time().drop('isPartial', axis = 1))
    
    trend = pd.concat(trend, axis = 1)
    trend.reset_index(inplace = True)
    return trend
#%% Reconstruct trends but with more accuracy
terms = ('Blockchain', 'BTC', 'BitCoin')
trends = payload(terms)
#%%
multiPlot(trends, 'date', terms, 1)
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
price["pct_change"] = price.close.pct_change()
price["log_return"] = np.log(price.close) - np.log(price.close.shift(1))
price["log_return"].plot()
price.describe()
#%%







#%%






#%%
datetime.datetime.fromtimestamp(btc86400["date"][len(btc86400)-1-8])
#%%
data = btc86400
#%% # dummy filler of correct length
data["tBitCoin"] = btc86400["close"]
data["tBTC"] = btc86400["close"]
data["tBlockchain"] = btc86400["close"]

day = datetime.datetime.now().day
data = data[:-day]
#%% Trends are weekly so they are repeated 7 times in the daily data
for i in range(4, len(data)+4):
    data["tBitCoin"][i-4] = trends["BitCoin"][int(109+(i/7))]
    data["tBTC"][i-4] = trends["BTC"][int(109+(i/7))]
    data["tBlockchain"][i-4] = trends["Blockchain"][int(109+(i/7))]

#%%
data["delta"] = data["open"] - data["close"]
#%%
#data.to_csv("C:\\Users\\Sebastien\\Desktop\\MAP536_Python_Final-master\\data.csv")
#%%
data = pd.read_csv("C:\\Users\\Sebastien\\Desktop\\MAP536_Python_Final-master\\data.csv")
data = data.drop('Unnamed: 0', 1)
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




