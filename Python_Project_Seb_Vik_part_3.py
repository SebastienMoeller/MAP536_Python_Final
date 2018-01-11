# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:35:17 2018

@author: Sebastien
"""
#%% All libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
#%% 
data = pd.read_csv("C:\\Users\\Sebastien\\Desktop\\MAP536_Python_Final-master\\data.csv")
#data = data.drop('Unnamed: 0', 1)

del data['test']
del data['Unnamed: 0']
data.set_index('date', inplace = True)

def meanSquareError(true, predicted):
    delta = true - predicted
    return sum(delta**2)/len(delta)

def linReg(X, y, test_ratio = 0.2):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_ratio)
    
    lm = linear_model.LinearRegression()

    model = lm.fit(X_train, y_train)
    predictions = lm.predict(X_test)
    
    plt.scatter(y_test, predictions, color = '#EBA911')
    
    print("Score:", model.score(X_test, y_test))
    print("Mean Square Error: ", meanSquareError(y_test, predictions))
    return model
#%%






#%%
y = data['close']
X = data[['tBitCoin', 'tBTC','tBlockchain']]

test = linReg(X, y)
#%%

#%% Lets try to predict the delta instead
y = data['delta']
X = data[data.columns.difference(['delta', 'close', 'open'])]

test = linReg(X, y)
#%%

#%%
import numpy as np
y = np.sign(data['delta'])
#%%

#%%

#%%

#%%

#%%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    
lm = linear_model.LinearRegression()

model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)
#%%
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, predictions)
#%%
meanSquareError(y_test, predictions)
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







































