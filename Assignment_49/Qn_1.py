'''
Machine Learning Assignment
Consider below Dataset as
Pregnancies Glucose BloodPressure SkinThickness Insulin BMI DiabetesPedigreeFunction Age Outcome

Objective:
Build a Machine Learning model to predict whether a patient is diabetic (1) or not (0) based on medical
attributes.
.
Task Instructions:
You must complete the following steps
1. Exploratory Data Analysis (EDA):
Load the dataset using pandas.
. Display the first 5 rows.
Show column info and check for null values.
. Display basic statistics using .describe ().
. Plot the distribution of the target variable (Outcome).
. Use graphs like hist, boxplot, or pairplot to identify patterns or outliers.


2. Data Preprocessing:
. Check and handle missing or zero values in columns like Glucose, BloodPressure, etc.
. Apply feature scaling using StandardScaler or MinMaxScaler.
. Split the dataset into features (X) and target (y).
3. Model Building:
Train at least 2 different algorithms on the dataset:
. Logistic Regression
. K-Nearest Neighbors (KNN)
Decision Tree
Use train_test_split to divide the data.

4. Model Evaluation:
Print accuracy score, confusion matrix, precision, recall, and F1 score.
Use matplotlib or seaborn to visualize confusion matrix.

5. Final Output:
Predict whether a patient is diabetic based on test data.
Display predictions on screen and save them in a CSV file.
'''

from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix,
                              classification_report)


def DiabetesPred(DataPath):
    border = "-"*40

    '''
    Step 1 : Exploratory Data Analysis
    '''

    print(border)
    print("Step 1 : Exploratory Data Analysis")
    print(border)

    df = pd.read_csv(DataPath)
    print("First 5 records of the dataset are : \n", df.head())
    print("The shape of dataset is : ",df.shape)
    print("Column info :\n", df.info())
    print("Null Values count :\n", df.isnull().sum())
    print("Statistics : \n", df.describe())
    print("Outcome Distribution :\n",df['Outcome'].value_counts())

    #Outcome of the distribution
    plt.figure(figsize=(8,5))
    df['Outcome'].value_counts().plot(kind='bar')
    plt.title("Outcome Distribution")
    plt.xlabel("Outcome (0 : No Diabetes, 1 : Diabetes)")
    plt.ylabel("Count")
    plt.show()

    # Histogram of all features
    df.hist(figsize=(8,5))
    plt.suptitle("Feature Distribution")
    plt.show()

    #Boxplot
    sns.boxplot(data =df.drop('Outcome', axis=1) )
    plt.title("Boxplot- Feature outliars")
    plt.show()

    #pairplot

    sns.pairplot(df[['Glucose','BMI','Age','Insulin','Outcome']])
    plt.suptitle("Pairplot")
    plt.show()


    '''
    Step 2 : Data Pre-Processing
    '''
    print(border)
    print("Step 2 : Data Pre-Processing")
    print(border)

    zero_cols = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
    df[zero_cols] = df[zero_cols].replace(0,np.nan)
    df[zero_cols] = df[zero_cols].fillna(df[zero_cols].median())
    print("Missing Values after replacing zeros:",df.isnull().sum())

    #Split features and target 

    X = df.drop('Outcome',axis=1)
    Y = df['Outcome']

    #Feature scaling
    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    #Train test split 
    X_train,X_test,Y_train,Y_test = train_test_split(X_scaled,Y,test_size=0.2,random_state=42,stratify=Y)
    print("Train size :",X_train.shape)
    print("Test size :", X_test.shape)


    '''
    Step 3 : Model building
    '''
    print(border)
    print("Step 3 : Model building")
    print(border)

    knn = KNeighborsClassifier(n_neighbors=7)
    dt = DecisionTreeClassifier(max_depth=5,random_state=42)

    knn.fit(X_train,Y_train)
    dt.fit(X_train,Y_train)

    knn_pred = knn.predict(X_test)
    dt_pred = dt.predict(X_test)

    '''
    Step 4 : Model Evaluation
    '''
    print(border)
    print("Step 4 : Model Evaluation")
    print(border)

    print("---------KNN-------------")
    knn_Accuracy = accuracy_score(Y_test,knn_pred)
    print("Accuracy of KNN :", knn_Accuracy)
    print("Classifiction report of KNN:\n", classification_report(Y_test,knn_pred))

    print("---------DT-------------")
    dt_Accuracy = accuracy_score(Y_test,dt_pred)
    print("Accuracy of DT :", dt_Accuracy)
    print("Classifiction report of DT :\n", classification_report(Y_test,knn_pred))

    #Confusion matrix print and plot

    print("KNN Confusion matrix : \n")
    cm_knn = confusion_matrix(Y_test,knn_pred)
    print(cm_knn)

    plt.figure(figsize=(8,5))
    sns.heatmap(confusion_matrix(Y_test, knn_pred),
                annot=True, fmt='d', cmap='Blues',
                xticklabels=['Non-Diabetic', 'Diabetic'],
                yticklabels=['Non-Diabetic', 'Diabetic'])
    plt.title('KNN- Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()


    print("DT Confusion matrix : \n")
    cm_dt = confusion_matrix(Y_test,dt_pred)
    print(cm_dt)

    plt.figure(figsize=(8,5))
    sns.heatmap(confusion_matrix(Y_test, dt_pred),
                annot=True, fmt='d', cmap='Blues',
                xticklabels=['Non-Diabetic', 'Diabetic'],
                yticklabels=['Non-Diabetic', 'Diabetic'])
    plt.title('Decision Tree - Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()


    '''
    Step 5 : Final Predictions
    '''
    print(border)
    print("Step 5 : Final Predictions")
    print(border)

    X_test_df = pd.DataFrame(
        scalar.inverse_transform(X_test),
        columns = df.drop('Outcome',axis=1).columns).round(2)

    X_test_df['Actual'] = Y_test.values
    X_test_df['KNN_Pred'] = knn_pred
    X_test_df['DT_Pred'] = dt_pred

    print("Sample predictions : \n")
    print(X_test_df[['Glucose','BMI','Age','Actual','KNN_Pred','DT_Pred']].head(10))

    X_test_df.to_csv('diabetes_predictions.csv',index = False)
    print("Saved to diabetes_predictions.csv")


def main():
    border = "-"*40
    print(border)
    print("diabetes prediction")
    print(border)

    DiabetesPred("diabetes.csv")



if __name__ == "__main__":
    main()