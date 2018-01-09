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
import random
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

# 80% training and 20% testing

data.reset_index(inplace = True)

#%%
N = len(data)

randomized_indices = np.arange(N)
# random.sample(randomized_indices, int(4 * N / 5))
np.random.shuffle(randomized_indices)

shuffled_data = data[randomized_indices] #dataset after index randomization

### Split the dataset into two subsets ###

## Build training set ##
#training_data = data.sample(int(4 * N / 5), replace = 'True')

## Build testing set ##
#testing_data = data.drop(training_data.index, axis = 0)


#%%
### Neural network training ###
Classifier = nn.MLPClassifier(hidden_layer_sizes = (50), activation = 'relu', solver = 'lbfgs',  max_iter = 10000000)
Classifier.fit(training_features, training_targets)

#NOTA: Here we realized that with two layers we obtain way better scores for (10,50) than for (50,10)

### Neural network testing ###
score_train = Classifier.score(training_features, training_targets)
score_test = Classifier.score(testing_features, testing_targets)
print ('Score on the training set : ', score_train)
print ('Score on the testing set : ', score_test)
