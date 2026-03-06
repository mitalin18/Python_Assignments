import math

#Dataset 

data = [
    ("A", 1,2, "Red"),
    ("B", 2,3, "Red"),
    ("C", 3,1, "Blue"),
    ("D", 6,5, "Blue")
]


#input
x= float(input("Enter X coordinate : "))
y = float(input("Enter Y coordinate: "))

#Store distances
distances = []

#Calculate euclidean distance
for point in data:
    name, px,py,label = point
    distance = math.sqrt((x-px)**2 + (y- py)**2)
    distances.append((name,distance,label))

#sort distances
distances.sort(key = lambda d: d[1])

#select K nearest neighbours
def predict(k):
    neighbours = distances[:k]
    votes = {}

    for n in neighbours:
        label = n[2]

        if label in votes:
            votes [ label] +=1
        else:
            votes[label] = 1

    return max(votes,key = votes.get)
 

print("Predicted results \n")

print("K = 1 -> ", predict(1))
print("K = 3 -> ", predict(3))
print("K = 4 -> ", predict(4))

'''When K is small (K = 1)
The algorithm considers only the closest neighbor.
The prediction may be sensitive to noise or outliers.

When K increases (K = 3 or 4)
The algorithm considers more neighbors.
The prediction becomes more stable and generalized.

However, if K becomes too large:
Points from other classes may dominate.
This can change the prediction.'''





