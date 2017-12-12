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

#%% View Data
#doge.plot(x = "date", y = "open")
#doge.plot(x = "date", y = "volume")

btc.plot(x = "date", y = "open")
btc.plot(x = "date", y = "volume")
#%%
help(poloniex.poloniex)


#%%
import datetime

print("Start date")
print(datetime.datetime.fromtimestamp(btc["date"][0]))
print("End date")
print(datetime.datetime.fromtimestamp(btc["date"][len(btc)-1]))

#%%
#doge2 = doge

#for i in range(len(doge)):
#   doge2["date"][i] = datetime.datetime.fromtimestamp(doge["date"][i])

# doge2["date"][1415] = datetime.datetime.fromtimestamp(doge["date"][1415])

btc2 = btc

for i in range(len(btc2)):
   btc2["date"][i] = datetime.datetime.fromtimestamp(btc["date"][i])

#%%
print(btc2["date"])

#%%
btc2.plot(x = "date", y = "open")

#%%
btc


#%%






