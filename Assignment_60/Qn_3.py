'''
3: Write a Python program to calculate loss manually.

Tasks:

Implement Mean Squared Error.
Implement Binary Cross Entropy.
Take actual and predicted values.
Display the calculated loss.
Explain which loss function is used for regression and classification.
'''

import numpy as np

#Example values

y_true = np.array([1,0,1,1])
y_pred = np.array([0.9,0.2,0.8,0.7])

#MSE  (ytrue​−ypred​)**2

def mse(y_true,y_pred):
    return np.mean((y_true-y_pred) ** 2)

#Binary Cross Entropy

def binary_cross_entropy(y_true,y_pred):
    epsilon = 1e-10 #to avoid log(0)
    y_pred = np.clip(y_pred,epsilon,1-epsilon)
    return -np.mean(
        y_true * np.log(y_pred) + (1-y_true) * np.log(1-y_pred)
    )

#calculate loss
mse_loss = mse(y_true,y_pred)
bce_loss = binary_cross_entropy(y_true,y_pred)

#display results
print("MSE loss : ",mse_loss)
print("Binary Cross Entropy Loss : ",bce_loss)