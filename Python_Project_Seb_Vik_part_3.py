# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:35:17 2018

@author: Sebastien
"""
#%% All libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
#%% 
#data = pd.read_csv("C:\\Users\\Sebastien\\Desktop\\MAP536_Python_Final-master\\data.csv")
data = pd.read_csv("/Users/Sebastien/Documents/Documents/University/Polytechnique & HEC/Year 1/MAP536 R Python/Final Project/data.csv")
#data = data.drop('Unnamed: 0', 1)

del data['test']
del data['Unnamed: 0']
data.set_index('date', inplace = True)
#%%
def meanSquareError(true, predicted):
    delta = true - predicted
    return sum(delta**2)/len(delta)

def linReg(X, y, test_ratio = 0.2):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_ratio)
    
    lm = linear_model.LinearRegression()

    model = lm.fit(X_train, y_train)
    predictions = lm.predict(X_test)
    
    plt.scatter(y_test, predictions, color = '#EBA911')
    
    print("R-Square: ", model.score(X_test, y_test))
    print("Mean Square Error: ", meanSquareError(y_test, predictions))
    
    return model

def logReg(X, y, test_ratio = 0.2):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    
    logm = linear_model.LogisticRegression()
    
    model = logm.fit(X_train, y_train)
    predictions = logm.predict(X_test)
    
    print("Confusion Matrix:") 
    print(confusion_matrix(y_test, predictions))
    print("Model Score: ", model.score(X_test, y_test))
    
    return model

#%%

#%% Predict close price only using google trends
y = data['close']
X = data[['tBitCoin', 'tBTC','tBlockchain']]

test = linReg(X, y)
#%% Predict close price using all available information
y = data['close']
X = data[data.columns.difference(['delta', 'close'])]

test = linReg(X, y)
#%% Predict close price using all available information without open price
y = data['close']
X = data[data.columns.difference(['delta', 'close', 'open', 'logReturn'])]

test = linReg(X, y)
#%% Predict close price using all available information without open price
y = data['close']
X = data[data.columns.difference(['delta', 'close', 'open', 'weightedAverage', 'logReturn'])]

test = linReg(X, y)
#%%
y = data['close']
X = data[data.columns.difference(['delta', 'close', 'open', 'weightedAverage', 'high', 'low', 'volume', 'logReturn'])]

test = linReg(X, y)
#%%





#%% Lets try to predict the delta instead
y = data['delta']
X = data[data.columns.difference(['delta', 'close', 'open', 'logReturn'])]

test = linReg(X, y)
#%%





#%% Logistic Regression: Predict price increase or decrease
y = np.sign(data['delta'])
y = [1 if y>=0 else 0 for y in y]
X = data[data.columns.difference(['delta', 'close', 'open', 'logReturn'])]

test = logReg(X, y)
#%%





#%% Lets try the logarithmic returns instead

y = data['logReturn'][1:]
X = data[data.columns.difference(['delta', 'close', 'open', 'logReturn'])][1:]

test = linReg(X, y)

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
