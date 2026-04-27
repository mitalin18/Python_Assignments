'''
2: Write a Python program to demonstrate different activation functions.

Functions to implement:

1. sigmoid
2. reLU
3. tanh

Tasks:

1. Accept input values from -10 to 10.
2. Plot all activation functions using Matplotlib.
3. Explain the use of each activation function.

'''

import numpy as np
import matplotlib.pyplot as plt

#define activation function
def sigmoid(x):
    return 1/ (1+np.exp(-x))

def relu(x):
    return np.maximum(0,x)

def tanh(x):
    return np.tanh(x)


#input values from-10 to 10
x= np.linspace(-10,10,100)

#output
y_sigmoid=sigmoid(x)
y_relu = relu(x)
y_tanh = tanh(x)

#plotting
plt.figure()

plt.plot(x,y_sigmoid,label='Sigmoid')
plt.plot(x,y_relu,label='ReLU')
plt.plot(x,y_tanh,label='Tanh')

plt.title("Activation functions")
plt.xlabel("Input")
plt.ylabel("Output")

plt.legend()
plt.grid()
plt.show()


'''
Use -

1. Sigmoid
Binary classification output layer
Output range: (0, 1)
Smooth S-shaped curve

2. ReLU (Rectified Linear Unit)
Hidden layers in most modern neural networks
Output:
0 for negative inputs
Linear for positive inputs

3. Tanh
Better than sigmoid for hidden layers
Output range: (-1, 1)
Centered around zero (unlike sigmoid)



'''