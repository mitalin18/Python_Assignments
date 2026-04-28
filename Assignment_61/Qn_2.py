'''
2 : Create a neural network model to predict loan approval.

Features:
Applicant income
Credit score
Loan amount
Existing EMI
Employment status

Output:
0 = Loan rejected
1 = Loan approved

Tasks:
Preprocess categorical values.
Apply scaling.
Train FNN model.
Evaluate model.
Predict approval for new applicant.

Dataset

X = [
[25000, 600, 200000, 10000, 0],
[40000, 700, 300000, 8000, 1],
[60000, 750, 500000, 12000, 1],
[20000, 550, 150000, 15000, 0],
[80000, 800, 700000, 10000, 1],
[35000, 650, 250000, 9000, 1],
[18000, 500, 100000, 12000, 0],
[90000, 850, 800000, 15000, 1],
[30000, 580, 200000, 14000, 0],
[70000, 780, 600000, 10000, 1]

]

y = [
0, 1, 1, 0, 1,1, 0, 1, 0, 1
]

Feature Meaning
[Income, Credit Score, Loan Amount, Existing EMI, Employment Status]

Employment Status:
0 = Not Stable
1 = Stable

Test Input
new_applicant = [[55000, 720, 400000, 10000, 1]]

Expected Output
Prediction: Loan Approved
'''

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Dataset

X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
])

y = np.array([0,1,1,0,1,1,0,1,0,1])

# Train test split
X_train, X_test, Y_train, Y_test = train_test_split(X, y , test_size=0.2,random_state=42)

#scaling

scalar = StandardScaler()
X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

# Train FNN
model = MLPClassifier(hidden_layer_sizes=(5,),activation='relu',max_iter=1000)
model.fit(X_train_scaled,Y_train)

#Evaluate
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(Y_test,y_pred)
print("Model Accuracy : ", accuracy)

#Predict new applicant
new_applicant = np.array([[55000,720,400000,10000,1]])
new_scaled = scalar.transform(new_applicant)

prediction = model.predict(new_scaled)

if prediction[0] == 1:
    print("Prediction : Loan Approved")
else:
    print("Prediction : Loan Rejected")

