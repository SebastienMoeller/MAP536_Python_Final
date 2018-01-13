# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 20:23:40 2018

@author: DataScience
"""

#%% All libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
#%% 
data = pd.read_csv("C:\\Users\\Sebastien\\Desktop\\MAP536_Python_Final-master\\data.csv")
#data = data.drop('Unnamed: 0', 1)
#%%
del data['test']
del data['Unnamed: 0']
#%%
data.set_index('date', inplace = True)
##data.index
#%%
#data.reset_index(inplace = True)
#%%
##del extra['test']
#%%



#%%
data.keys()

#%%
plt.scatter(data["close"], data["open"])

#%%
plt.scatter(data["close"], data["tBitCoin"])

#%%
plt.scatter(data["close"], data["tBTC"])

#%%
plt.scatter(data["close"], data["tBlockchain"])

#%%
plt.scatter(data["close"], data["high"])

#%%
plt.scatter(data["close"], data["low"])

#%%
plt.scatter(data["close"], data["quoteVolume"])

#%%
plt.scatter(data["close"], data["volume"])

#%%
plt.scatter(data["close"], data["weightedAverage"])
#%%





#%%
## WE SEE HERE THAT IT KIND OF LOOKS LIKE A POLYNOMIAL FUNCTION. Degree 3?

## Let's define these functions:

def polynomial_model(param, x):
    return param[0] + param[1]*x + param[2]*x**2 + param[3]*x**3

def polynomial_err(param, x, y):
    return y - polynomial_model(param, x)

#%%
x_data = data['close']
y_data = data['tBlockchain']    

param0 = [1, 1, 1, 1] ## Initialisation of the iterations

param1, meta_res = scipy.optimize.leastsq(polynomial_err, param0[:], args = (x_data, y_data))
#%%
y_model = polynomial_model(param1, x_data) 
plt.scatter(x_data,y_data,label='Data')
plt.plot(x_data,y_model,label='Estimated', color = 'Red')
plt.legend(loc='best', title='Series')
plt.show()

print("Initial parameters :", param0)
print("Estimated parameters :", param1)

print(meta_res)

#%%

# WE SEE THAT THE DATA NEEDS TO BE "SORTED" FOR THE X VARIABLE. OTHERWISE THE ESTIMATED CURVE DOES NOT LOOK GOOD

data = data.sort_values('tBlockchain', ascending=True)

#%%
## WE SEE HERE THAT IT KIND OF LOOKS LIKE A POLYNOMIAL FUNCTION. Degree 3?

## Let's define these functions:

def polynomial_model(param, x):
    return param[0] + param[1]*x + param[2]*x**2 + param[3]*x**3

def polynomial_err(param, x, y):
    return y - polynomial_model(param, x)

#%%
x_data = data['tBlockchain'] 
y_data = data['close']   

param0 = [1, 1, 1, 1] ## Initialisation of the iterations

param1, meta_res = scipy.optimize.leastsq(polynomial_err, param0[:], args = (x_data, y_data))
#%%
y_model = polynomial_model(param1, x_data) 
plt.scatter(x_data,y_data,label='Data')
plt.plot(x_data,y_model,label='Estimated', color = 'Red')
plt.legend(loc='best', title='Series')
plt.show()

print("Initial parameters :", param0)
print("Estimated parameters :", param1)

print(meta_res)
#%%





#%%
def meanSquareError(true, predicted):
    delta = true - predicted
    return sum(delta**2)/len(delta)

def polynomialModelN(n, param, x):
    temp = 0
    for i in range(n):
        temp = temp + param[i]*x**(i)
    return temp

def polynomialError(param, x, y):
    return y - polynomialModelN(len(param), param, x)
#%%

# WE SEE THAT MAYBE DEGREE THREE FITS BETTER THAN DEGREE 2. HOWEVER, THIS IS NORMAL: THE ERROR WILL ALWAYS DECREASE WITH MORE COMPLEX MODEL
## LET'S THEN TRY TO DO CROSS VALIDATION TO DECREASE THE TESTING AND TRAINING ERROR

data.reset_index(inplace = True)

# 80% training and 20% testing
def shuff(data, ratio = 0.3):    
    N = len(data)

    randomized_indices = np.arange(N)
    np.random.shuffle(randomized_indices)
 
    #dataset after index randomization
    shuffled_data = data.iloc[randomized_indices,:] 

    ### Split the dataset into two subsets ###

    ## Build training set ##
    training_data = shuffled_data[:int((1-ratio)*N)]

    ## Build testing set ##
    testing_data = shuffled_data[int((1-ratio)*N):]
    
    return training_data, testing_data
#%%
training_data, testing_data = shuff(data)

training_data = training_data.sort_values('tBlockchain', ascending=True)    
testing_data = testing_data.sort_values('tBlockchain', ascending=True)  

x_data = training_data['tBlockchain'] 
y_data = training_data['close']   

x_test = testing_data['tBlockchain'] 
y_test = testing_data['close']

#%%
def magic(n, x_data = x_data, x_test = x_test, y_data = y_data, y_test = y_test):
    n = n+1
    param0 = np.ones(n)
    param1, meta_res = scipy.optimize.leastsq(polynomialError, param0[:], args = (x_data, y_data))
    
    plt.scatter(x_data,y_data,label='Training Data', color = '#EBA911')
    plt.scatter(x_test,y_test,label='Testing Data', color = '#0CC88F' )
    
    smooth_x = np.linspace(0,max(x_data),1000)
    
    plt.plot(smooth_x,polynomialModelN(n, param1, smooth_x),label='Estimated', color = 'Red')
    plt.legend(loc='best', title='Series')
    plt.show()

    #print("Initial parameters :", param0)
    #print("Estimated parameters :", param1)

    #print(meta_res)
    
    mseTrain = meanSquareError(y_data, polynomialModelN(n, param1, x_data))
    mseTest = meanSquareError(y_test, polynomialModelN(n, param1, x_test))
    
    #print("Training Error :", mseTrain)
    #print("Testing Error :", mseTest)
    return int(mseTrain), int(mseTest)

def trainTestError(n):
    error = []
    for i in range(n):
        error.append(magic(i+1))
    
    plt.plot(error)
    plt.xticks(list(range(0,n)),list(range(1,n+1)))
    
    return error
#%%
trainTestError(10)
#%%
#Here we see that the testing error changes a lot according to the "shuffle" of the data, and changes the optimal degree of the polynome.
#It would thus be clever to run a large nu;ber of simulations to find the "real" optimum (Monte Carlo simulation?) 
