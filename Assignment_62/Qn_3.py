'''
3: Write a Python program to show flattening.

Tasks:
Take a 2D matrix.
Convert it into a 1D vector.
Pass it to a fully connected layer.
Calculate final output manually.
Explain the role of flatten layer in CNN.

Input Matrix
matrix = [
[6, 4],
[8, 6]
]

Expected Flatten Output
flatten_output = [6, 4, 8, 6]
'''

# Input matrix
matrix = [
    [6, 4],
    [8, 6]
]

#flatten
flatten_output = []

for row in matrix:
    for val in row:
        flatten_output.append(val)

print("Flatten Output : ",flatten_output)

#fully connected layer 

weights = [0.2,0.3,0.4,0.1]
bias = 1

z = 0 
weights_cal=0

for i in range(len(flatten_output)):
    weights_cal += flatten_output[i] * weights[i]
z = weights_cal + bias
print("Final Output : ",z)