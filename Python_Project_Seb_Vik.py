#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:43:35 2017

@author: Sebastien
"""

#%% Importing from API
# To import poloniex we need to install the package in the console using:
# pip install poloniex
import poloniex
import pandas
#help(poloniex.poloniex)

# We are using the public data so no keys are needed
polo = poloniex.Poloniex()
# Transform data into a dataframe
# "period" (candlestick period in seconds; valid values
#     |      are 300, 900, 1800, 7200, 14400, and 86400), "start", and "end".
#     |      "Start" and "end" are given in UNIX timestamp format and used to
#     |      specify the date range for the data returned.
# 86400 = 24 hours

#doge = pandas.DataFrame(polo.returnChartData("BTC_DOGE", 86400))
btc = pandas.DataFrame(polo.returnChartData("USDT_BTC", 86400))

#%%
import datetime

print("Start date")
print(datetime.datetime.fromtimestamp(btc["date"][0]))
print("End date")
print(datetime.datetime.fromtimestamp(btc["date"][len(btc)-1]))

btc2 = btc

for i in range(len(btc2)):
   btc2["date"][i] = datetime.datetime.fromtimestamp(btc["date"][i])

#%%
btc2.columns

#%%
btc2.describe()

#%%
btc.dtypes

#%%
import sys
sys.getsizeof(btc2)

#%% View Data
import matplotlib.pyplot as plt

fig = plt.figure()

axes1 = fig.add_axes([0.05, 0.2, 1.2, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.6, 0.3]) # inset axes

# main figure
axes1.plot(btc2["date"], btc2["volume"]/btc2["volume"].max(), "#0CC88F")
axes1.plot(btc2["date"], btc2["close"]/btc2["close"].max(), '#EBA911')

axes1.legend(loc=2)
axes1.set_xlabel('date')
axes1.set_ylabel('Max')
axes1.set_title('Last Three Years')

# insert
axes2.plot(btc2["date"][-30:], btc2["volume"][-30:]/btc2["volume"][-30:].max(), '#0CC88F')
axes2.plot(btc2["date"][-30:], btc2["close"][-30:]/btc2["close"][-30:].max(), '#EBA911')

axes2.set_xlabel('date')
axes2.set_ylabel('Max')
axes2.set_title('Last 30 Days');
#%%








#%% GOOGLE TRENDS
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)


#%%
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
import matplotlib.pyplot as plt

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




