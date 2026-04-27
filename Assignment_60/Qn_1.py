'''
1: Write a Python program to simulate a single artificial neuron.
Input:
x1 = 2
x2 = 3
w1 =0.4
w2=0.6
bias = 0.5

Tasks:
1. Calculate weighted sum.
2. Apply sigmoid activation function.
3. Display final output.
4. Explain whether output is close to 0 or 1.

'''

import math

#Inputs
x1= 2
x2=3
w1=0.4
w2=0.6
bias=0.5

#Calculate weighted sum
weighted_sum = (x1*w1) + (x2*w2) + bias

#Applying sigmoid activation function.

def sigmoid(x):
    return 1/(1+ math.exp(-x))

output = sigmoid(weighted_sum)

# Display final output
print("Weighted sum :", weighted_sum)
print("Output after sigmoid :", output)

#Explaination
if(output > 0.5):
    print("Output is closer to 1")
else:
    print("Output is closer to 0")
