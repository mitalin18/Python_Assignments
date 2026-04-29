'''
2: Write a Python program to demonstrate ReLU and Max Pooling.

Tasks:
Create a feature map with positive and negative values.
Apply ReLU.
Apply 2x2 max pooling.
Display output after each step.
Explain why pooling reduces size.
Input Feature Map

feature_map = [
[3, 3, 3],
[0, 0, 0],
[-3, -3, -3]
]

ReLU Rule
If value < 0, convert it to 0
If value >= 0, keep it same

Expected Output
relu_output = [
[3, 3, 3],
[0, 0, 0],
[0, 0, 0]
]

'''

#input feature map
feature_map = [
[3, 3, 3],
[0, 0, 0],
[-3, -3, -3]
]

#apply relu

relu_output=[]

for row in feature_map:
    new_row = []
    for val in row:
        if val < 0:
            new_row.append(0)
        else:
            new_row.append(val)
    relu_output.append(new_row)

print("After ReLU :")
for r in relu_output:
    print(r)


#max pooling

pool_output = []

rows=len(relu_output)
cols = len(relu_output[0])

for i in range(0,rows -1,2):
    row = []
    for j in range(0,cols-1,2):

        #2*2 region
        region = [
            relu_output[i][j],
            relu_output[i][j+1],
            relu_output[i+1][j],
            relu_output[i+1][j+1]
        ]

        max_val = max(region)
        row.append(max_val)
    
    pool_output.append(row)

print("\n After Max Pooling : ")
for r in pool_output:
    print(r)