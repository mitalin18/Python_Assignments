# ------------------------------------------------------
# Student Performance Prediction using Decision Tree
# ------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
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



# ----------------------------
# Feature Importance
# ----------------------------

importances = model.feature_importances_

for feature, score in zip(X_train.columns,importances):
    print(feature,": ", score )


# ----------------------------
# Remove SleepHours and Retrain
# ----------------------------


X_no_sleep = df.drop(["FinalResult","SleepHours"], axis = 1)
y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(X_no_sleep,y,test_size=0.2,random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)
print("Accuracy after Removing SleepHours and Retrain :", accuracy_score(Y_test,Y_pred)* 100)

'''Removing SleepHours does not significantly affect performance, which means sleep hours 
are not a strong predictor in this dataset.'''

# ------------------------------------------------
# Train Model Using Only StudyHours and Attendance
# ------------------------------------------------

X_small = df[["StudyHours", "Attendance"]]
y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X_small,y,test_size=0.2,random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train,Y_train)

Y_pred= model.predict(X_test)
print("Accuracy after Training Model Using Only StudyHours and Attendance",accuracy_score(Y_test,Y_pred)*100)

# ------------------------------------------------
# Predict Results for 5 New Students
# ------------------------------------------------

new_students = pd.DataFrame({
    "StudyHours":[6,3,5,7,2],
    "Attendance":[85,60,75,90,50]
})
predictions = model.predict(new_students)

new_students ["Prediction"] = predictions
print("Results for 5 New Students :",new_students)

# ------------------------------------------------
# Manually Calculate Accuracy
# ------------------------------------------------

correct_preds = sum(Y_test == Y_pred)
total = len(Y_test)

manual_accuracy = correct_preds / total

print("Manual accuracy :", manual_accuracy*100)


# ------------------------------------------------
# Misclassified Students
# ------------------------------------------------

misclassified = X_test[Y_test != Y_pred]
print("Misclassified students :", misclassified)
print("Total misclassified :",len(misclassified))


'''Observation
Misclassified students are those where prediction does not match actual result.

Pattern
Often these students have borderline values, such as:
Medium study hours
Medium attendance
Average previous scores
So the model finds them harder to classify.'''

# ------------------------------------------------
# Compare Different random_state Values
# ------------------------------------------------

states = [0,10,42]

for s in states:
    X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2, random_state=s)

    model = DecisionTreeClassifier()
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    acc= accuracy_score(Y_test,Y_pred)

    print("Random state = ", s,"Accuracy =" , acc*100)

    '''
    Accuracy may change slightly because the training and testing data split changes.
    However, with small datasets results may still remain similar.
    '''

# ------------------------------------------------
# Decision Tree Visualization
# ------------------------------------------------

plt.figure(figsize=(12,6))
plot_tree(model,
          feature_names= x.columns,
          class_names = ["Fail","Pass"],
          filled= True
          )
plt.show()

'''Root node feature: Usually StudyHours.
Why?
Because it has the highest feature importance and best separates pass vs fail students.'''

# ------------------------------------------------
# Create PerformanceIndex Feature
# ------------------------------------------------

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

X = df.drop("FinalResult",axis=1)
y = df["FinalResult"]

X_train, X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

print("Accuracy :", accuracy_score(Y_test,Y_pred)*100)

'''Observation
Accuracy may remain the same or slightly improve.
Explanation
The new feature combines study effort and attendance, which may help the model identify performance patterns.'''

# ------------------------------------------------
# Overfitting explaination
# ------------------------------------------------

model = DecisionTreeClassifier(max_depth=None)
model.fit(X_train,Y_train)

train_acc = accuracy_score(Y_train,model.predict(X_train))
test_acc = accuracy_score(Y_test,model.predict(X_test))
print("Training Accuracy :", train_acc * 100)
print("Testing Accuracy :", test_acc * 100)

'''This happens because the model memorizes training data too well.
The tree becomes very deep and learns noise instead of general patterns.
This is called overfitting.
A simpler tree (smaller max_depth) can prevent overfitting.'''

