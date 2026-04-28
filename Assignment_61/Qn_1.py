'''
1 : Create a neural network model to predict whether a customer will leave a service.
Features:
Age
Monthly charges
Tenure
Number of complaints
Customer support calls

X=[
[25, 500, 12, 1, 2],
[30,700, 24,0, 1],
[45, 1200, 6, 5, 8],
[50, 1500, 5,6, 10],
[28,600, 18, 1, 1],
[35,800, 30,0,0],
[48, 1400,4, 7,9],
[52, 1600,3,8, 12],
[27,550, 20,0, 1],
[42, 1300, 8, 4, 7]
]

y=[
0,0,1,1,0,0,1,1,0,1
]

Output:
0 = Customer will stay
1 = Customer will leave

Tasks:
Load or create dataset.
Clean the dataset.
Apply StandardScaler.
Train FNN model.
Evaluate accuracy.

Feature Meaning
[Age, Monthly Charges, Tenure, Complaints, Support Calls]

Output Meaning
0 = Customer will stay
1 = Customer will leave

Test Input
new_customer = [[46, 1450, 5, 6, 9]]

Expected Output
Prediction: Customer may leave


'''

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

#1 Create dataset

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

y = np.array([0,0,1,1,0,0,1,1,0,1])

# 2 train test split

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2,random_state=42)

# Apply StandardScalar
scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test= scalar.transform(X_test)

#Train FNN
model = MLPClassifier(hidden_layer_sizes=(5,),activation='relu',max_iter=1000)
model.fit(X_train,Y_train)

#Evaluate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test,y_pred)
print("Model accuracy : ",accuracy)

#test new customer
new_customer = np.array([[46,1450,5,6,9]])
new_customer_scaled = scalar.transform(new_customer)

prediction= model.predict(new_customer_scaled)

if prediction[0] == 1:
    print("Prediction : Customer may leave")
else:
        print("Prediction : Customer will stay")
    

