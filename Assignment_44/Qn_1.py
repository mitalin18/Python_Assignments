'''
There is one data set of advertisement agency.
Consider below Dataset as
TV
radio
newspaper
sales

Dataset contains multiple records about the customers who invest in multiple advertisement
options.
Depends on that sales feature indicates the the increased amount in there sales

This data set contains 4 features as
TV
radio
newspaper
sales

Depends on the above three features Sales feature indicates the increased sale amount.

We have to design Machine Learning application which uses Classification
technique.

Design machine learning application which follows below steps as

Step 1:
Get Data
Load data from MarvellousAdvertising.csv file into python application.

Step 2:
Clean, Prepare and Manipulate data
As we want to use the above data into machine learning application we have prepare
that in the format which is accepted by the algorithms.

Step 3:
Train Data
Now we want to train our data for that we have to select the Machine learning algorithm.
For that we select Linear Regression algorithm from sykit learn library.
For training purpose divide the dataset into half part.
Use train method to train our dataset.

Step 4:
Test the data
Test data by passing the remaining half part of the data set.

Step 5:
Display predicted values of Linear regression algorithms as well as expected values
which are provided by the data set.

'''

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.model_selection import train_test_split



#Load dataset 
df = pd.read_csv("Advertising.csv")
print("First 5 rows of the dataset:")
print(df.head())
print("shape of dataset is :", df.shape)


#Remove unwanted columns

if 'Unnamed: 0' in df.columns:
    df = df.drop("Unnamed: 0", axis=1)

print("First 5 rows of the dataset after unwanted column removal:")
print(df.head())
print("shape of dataset after unwanted column removal is :", df.shape)

#Check missing values

print("Missing values count :", df.isnull().sum())


#Display statistical summary 

print(df.describe)


#Corelation between columns

print("Corelation matrix :")
print(df.corr())



#Split data into independent and dependent variables
X = df[['TV','radio','newspaper']]
Y = df['sales']

print("Shape of independent variables :", X.shape)
print("Shape of dependent variables is :",Y.shape)


#split the data into training and testing

X_train,X_test,Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("X_train shape", X_train.shape)
print("X_test shape", X_train.shape)
print("Y_train shape", X_train.shape)
print("Y_test shape", X_train.shape)

# create and train the model

model = LinearRegression()
model.fit(X_train,Y_train)

#Test model

Y_pred = model.predict(X_test)

#Evaluate the model

MSE = mean_squared_error(Y_test,Y_pred)
RMSE = np.sqrt(MSE)

R2 = r2_score(Y_test,Y_pred)

print("Mean Squared Error is :",MSE)
print("Root Mean Squared Error is :",RMSE)
print("R square value is :",R2)

#Calculate model  coefficient


for column, value in zip(X.columns,model.coef_):
    print(f"{column} : {value}")

print("Intercept :", model.intercept_)

#Compare actual and predicted values

comparison = pd.DataFrame({
     "Expected sales : ": Y_test.values,
     "Predicted sales :": Y_pred
})

print("Comparison of actual and predicted values :")
print(comparison.head())

#Visualization

plt.figure(figsize=(8,5))
plt.scatter(Y_test,Y_pred)
plt.plot([Y_test.min(), Y_test.max()],
         [Y_test.min(), Y_test.max()],
         color='red')
plt.xlabel("Actual sales")
plt.ylabel("Predicted sales")

plt.title("Actual sales vs predicted sales")
plt.grid(True)
plt.show()
