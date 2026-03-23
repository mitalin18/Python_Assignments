'''
Machine Learning Assignment

There is one data set of wine which classify the wines according to its contents into three
classes.

Consider below Wine Dataset as

Class Alcohol Malic acid Ash Alcalinity of ash Magnesium Total phenols Flavanoids Nonflavanoid phenols Proanthocyanins Color intensity Hue 00280/OD315 of diluted wines Proline

These data are the results of a chemical analysis of wines grown in the same region in Italy
but derived from three different cultivars. The analysis determined the quantities of 13
constituents found in each of the three types of wines.

Wine data set contains 13 features as

1) Alcohol
2) Malic acid
3) Ash
4) Alcalinity of ash
5) Magnesium
6) Total phenols
7) Flavanoids
8) Nonflavanoid phenols
9) Proanthocyanins
10)Color intensity
11)Hue
12)OD280/OD315 of diluted wines
13)Proline

According to the above features wine can be classified as
. Class 1
. Class 2
. Class 3

We have to design Machine Learning application which uses Classification
technique.

Get Data
 Clean, Prepare & Manipulate Data 
Train Model 
Test Data 
Improve


Design machine learning application which follows below steps as

Step 1:
Get Data

Step 2:
Clean, Prepare and Manipulate data

Step 3:
Train Data

Step 4:
Test Data

Step 5:
Calculate Accuracy


'''
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from  sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

def WineClassifier(DataPath):
    border = "-"*40

    #Step 1 : Load the dataset from csv file
    print(border)
    print("Step 1 : Load the dataset from csv file")
    print(border)

    df = pd.read_csv(DataPath)
    print(border)
    print("Some entries from dataset :")
    print(df.head())
    print(border)

    #Step 2 : clean the dataset by removing empty rows

    print(border)
    print("Step 2 : clean the daraset by removing empty rows")
    print(border)

    df.dropna(inplace = True) #remove row if missing any cell
    print("Total records : ", df.shape[0])
    print("Total columns : ", df.shape[1])
    print(border)

    print(border)
    print("Step 3 : Seperate independent and dependent variables")
    print(border)

    X = df.drop(columns = ['Class']) #except class
    Y = df['Class']

    print("Shape of X : ", X.shape)
    print("Shape of Y :", Y.shape)

    print(border)
    print("Input columns : ", X.columns.tolist())
    print("Output column : Class")

    # Step 4 : Split the dataset for training and testing
    print(border)
    print("Step 4 : Split the dataset for training and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify = Y)

    print(border)
    print("Information of training and testing data")
    print("X_train shape :", X_train.shape)
    print("X_train shape :", X_test.shape)
    print("X_train shape :", Y_train.shape)
    print("X_train shape :", Y_test.shape)
    print(border)

    # Step 5 : Feature Scaling
    print(border)
    print("Step 5 : Feature Scaling")
    print(border)

    scalar = StandardScaler()
    #Independent variable scaling
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Feature scaling is done")

    #Step 6 : Explore the multiple values of k
    # Hyperparameter tuning (K)

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)  #(n_neighbours = k) k = 5 default value if we dont specify 
        model.fit(X_train_scaled, Y_train)
        Y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test,Y_pred) 
        accuracy_scores.append(accuracy)

    print(border)
    print("Accuracy report of all K values from 1 to 20")

    for value in accuracy_scores:
        print(value)
    print(border)

    #Step 7: plot graph of K vs Accuracy

    print(border)
    print("Step 7: plot graph of K vs Accuracy")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker = 'o')
    plt.title("K values vs Accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid("True")
    plt.xticks(list(K_values))
    plt.show()

    #Step 8 : Find the best value of k 

    print(border)
    print("Step 8 : Find the best value of k")
    print(border)

    best_k = list(K_values) [accuracy_scores.index(max(accuracy_scores))]
    print("Best value of K is :", best_k)

    #Step 9: Build final model using best value of k 

    print(border)
    print("Step 9: Build final model using best value of k ")
    print(border)

    final_model = KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(X_train_scaled,Y_train)
    Y_pred = final_model.predict(X_test_scaled)

    #Step 10 : Calculate final accuracy 

    print(border)
    print("Step 10 : Calculate final accuracy ")
    print(border)

    accuracuy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is : ", accuracuy*100)

    #Step 11 : Display confusion matrix

    print(border)
    print("Step 11 : Display confusion matrix ")
    print(border)

    cm = confusion_matrix(Y_test,Y_pred)
    print(cm)

    #Step 12 : Display classification report 

    print(border)
    print("Step 12 : Display classification report")
    print(border)

    print(classification_report(Y_test,Y_pred))



def main():
    border = "-"*40
    print(border)
    print("Wine classifier using KNN")
    print(border)

    WineClassifier("WinePredictor.csv")



if __name__ == "__main__":
    main()