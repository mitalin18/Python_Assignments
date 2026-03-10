'''
There is one data set of wether conditions. That dataset contains information as wether and we have to 
decides whether to play not. 
Data set contains the target variable as Play which indicates whether to play or not. 
Consider below Marvellous Infosystems Play Predictor 
Dataset as Marvellous Infosystems Play Predictor 
   wether Temperature Play 
 1 sunny hot no 
 2 sunny hot no 
 3 Overcast Hot Yes 
 4 rainy mild yes 
 5 rainy cool yes 
 6 rainy cool no 
 7 overcast cool yes 
 8 sunny mild no 
 9 sunny cool yes 
 10 rainy mild yes 
 
 According to above dataset there are two features as 
 1. Wether 2. Temperature 
 We have two labels as 1.Yes 2.No 
 There are three types of different entries under Wether as 
 1.Sunny 2.Overcast 3.Rainy There are three types of different entries 
 under Temperature as 1.Hot 2.Cold 3.Mild We have to design Machine 
 Learning application which uses Classification technique. 
 Get Data Clean, Prepare & Manipulate Data Train Model Test Data 
 Improve Design machine learning application which follows below 
 steps as 
 Step 1: Get Data Load data from MarvellousInfosystems_PlayPredictor.csv 
 file into python application. 
 Step 2: Clean, Prepare and Manipulate data As we want to use the above 
 data into machine learning application we have prepare that in the 
 format which is accepted by the algorithms. As our dataset contains two 
 features as Wether and Temperature. We have to replace each string 
 field into numeric constants by using LabelEncoder from processing 
 module of sklearn. 
 Step 3: Train Data Now we want to train our data for that we have to 
 select the Machine learning algorithm. For that we select K Nearest 
 Neighbour algorithm. use fit method for training purpose. 
 For training use whole dataset. Step 4: Test Data After successful 
 training now we can test our trained data by passing some value of 
 wether and temperature. As we are using KNN algorithm use value of K 
 as 3. After providing the values check the result and display on 
 screen. Result may be Yes or No. 
 Step 5: Calculate Accuracy Write one function as CheckAccuracy() 
 which calculate the accuracy of our algorithm. For calculating the 
 accuracy divide the dataset into two equal parts as Training data 
 and Testing data. Calculate Accuracy by changing value of K.
'''


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#Step 1 - get data 
data = pd.read_csv("PlayPredictor.csv")
data = data.drop("Unnamed: 0", axis=1)
print(data.head())

#step 2 - clean, prepare and manipulate data
le = LabelEncoder()

data["Whether"] = le.fit_transform(data["Whether"])
data["Temperature"] = le.fit_transform(data["Temperature"])
data["Play"] = le.fit_transform(data["Play"])
'''
fit() -Finds all unique values- Sunny, Rainy, Overcast
transform()- Converts them to numbers
'''

X = data[["Whether","Temperature"]]
Y = data["Play"]

#Step 3 - Train model (KNN)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,Y)

#step 5 - test data

result = model.predict(pd.DataFrame([[2,0]], columns = ["Whether","Temperature"]))
print(result)

if result[0] == 1:
    print("Yes")
else:
    print("No")

# Step 5 - calculate accuracy

X_train, X_test, Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy :", accuracy *100)








