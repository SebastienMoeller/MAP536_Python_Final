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
data = pd.read_csv("C:\\Users\\DataScience\\Desktop\\Python Course\\MAP536_Python_Final-master\\data.csv")
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
plt.scatter(data['close'],data['tBlockchain'])


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
## LET'S TRY WITH A DEGREE 2 POLYNOME

## Let's define these functions:

def polynomial_model(param, x):
    return param[0] + param[1]*x + param[2]*x**2

def polynomial_err(param, x, y):
    return y - polynomial_model(param, x)

#%%
x_data = data['tBlockchain'] 
y_data = data['close']   

param0 = [1, 1, 1] ## Initialisation of the iterations

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

# WE SEE THAT MAYBE DEGREE THREE FITS BETTER THAN DEGREE 2. HOWEVER, THIS IS NORMAL: THE ERROR WILL ALWAYS DECREASE WITH MORE COMPLEX MODEL
## LET'S THEN TRY TO DO CROSS VALIDATION TO DECREASE THE TESTING AND TRAINING ERROR