'''
1: Write a Python program to manually perform convolution.

Input:
A 5x5 matrix representing grayscale image.

Kernel:
A 3x3 edge detection filter.
tasks-
Move kernel over image.
Perform multiplication and addition.
Generate feature map.
Print each region calculation.

Input Image Matrix
image = [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0],
[0, 0,0, 0, 0]
]
Kernel Matrix

kernel = [
[-1, -1, -1],
[ 0, 0, 0],
[ 1, 1, 1]
]


First Region Calculation

Region:
000
000
111

Kernel:
-1 -1 -1
0 0 0
1 1 1

Calculation:
0 *- 1 + 0 *- 1 + 0 *- 1 +
0*0 + 0*0 + 0*0 +
1*1 + 1*1 + 1*1

Output = 3

Expected Feature Map

feature_map = [
[3, 3, 3],
[0, 0, 0],
[-3, -3, -3]
]
'''

#input image 
image=[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Kernel
kernel = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

#output feature map
feature_map = []

#convulation
for i in range(3): #rows
    row = []
    for j in range(3): #columns

        print(f"\n Region at position ({i},{j}): ")

        total = 0
    
        for ki in range(3):
            for kj in range(3):
                val = image[i+ki][j+kj]
                k_val = kernel[ki][kj]

                print(f"{val} * {k_val}", end=" ")
                total += val*k_val

        print("\nSum =",total)
        row.append(total)
    feature_map.append(row)

    #final output

print("\nFeature Map :")
for r in feature_map:
    print(r)
