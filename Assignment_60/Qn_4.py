'''
4: Write a Python program to show how weights are updated in ANN.

Tasks:

Take input, weight, bias, target output, and learning rate.
Calculate prediction.
Calculate error.
Update weight using gradient descent logic.
Display old weight and updated weight.
'''

import numpy as np

#inputs
x=np.array([2])
w=np.array([0.5])
b=0.1
target =1
learning_rate = 0.1

#sigmoid function
def sigmoid(x):
    return 1/(1+np.exp(-x))

#prediction
z= x*w + b
prediction = sigmoid(z)

#Error (simple diff)
error = target - prediction

#Gradient (Derivative for sigmoid)
gradient = prediction * (1-prediction)

#Update weight
old_weight = w
n_w = w + learning_rate * error * gradient * x

#Results

print("Prediction : ", prediction)
print("Error : ", error)
print("Old Weight : ",old_weight)
print("Updated weight : ", n_w)
