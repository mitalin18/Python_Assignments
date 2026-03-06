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
k=3
neighbours = distances[:k]
print("\nNearest Neighbours : ")

votes = {}

for n in neighbours:
    name, dist, label = n
    print(name, "-Distance :", round(dist,2))

    if label in votes:
        votes [ label] +=1
    else:
        votes[label] = 1

#Majority voting

predicted_class = max(votes,key = votes.get)

print("\nPredicted Class : ",predicted_class)


