# ------------------------------------------------------
# Student Performance Prediction using Decision Tree
# ------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# ----------------------------
# Load Dataset
# ----------------------------

df= pd.read_csv("student_performance_ml.csv")

print(df.head())
print("Shape : ",df.shape)

# ----------------------------
# Data Visualization
# ----------------------------

sns.histplot(df['StudyHours'])
plt.title("StudyHours Distribution")
plt.show()

# ----------------------------
# Prepare Data
# ----------------------------

x= df.drop("FinalResult",axis = 1)
y = df["FinalResult"]

X_train,X_test, Y_train, Y_test = train_test_split(
    x,y,test_size=0.2, random_state=42
)

# ----------------------------
# Train Model
# ----------------------------

model = DecisionTreeClassifier()
model.fit(X_train,Y_train)

# ----------------------------
# Prediction
# ----------------------------

Y_pred = model.predict(X_test)

print("Predicted values :", Y_pred)
print("Actual values : ",Y_test.values)

# ----------------------------
# Accuracy
# ----------------------------

accuracy = accuracy_score(Y_test,Y_pred)
print("Testing accuracy is :", accuracy * 100, "%")



train_pred = model.predict(X_train)

train_accuracy = accuracy_score(Y_train,train_pred)
test_accuracy = accuracy_score(Y_test,Y_pred)

print("Training Accuracy :", train_accuracy * 100 , "%")
print("Testing Accuracy :", test_accuracy * 100 , "%")

# ----------------------------
# Confusion Matrix
# ----------------------------

cm = confusion_matrix(Y_test,Y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()




depts = [1,3,None]

for d in depts:
    model = DecisionTreeClassifier(max_depth=d,random_state=42)
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)
    acc = accuracy_score(Y_test,Y_pred)

    print("max_depth = ", d, "Testing Accuracy = {:.2f}%".format(acc * 100))



new_student = pd.DataFrame([[6,85,66,7,7]],
                            columns=x.columns)

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("The student will pass")

else:
    print("The student will fail")




