'''
Bank Term Deposit Subscription Prediction Domain: Banking, Marketing Problem Statement: A Portuguese bank conducted marketing campaigns to promote term deposit subscriptions. The goal is to predict whether a client will subscribe (yes or no) to a term deposit based on their profile and campaign interaction details. Dataset Overview: You will use the Bank Marketing Dataset from UCI repository. Target Column: Y (yes = client subscribed to term deposit, no = did not subscribe) Feature Description age job marital education default balance housing loan contact day month duration campaign previous poutcome age of the client job type (admin., technician, etc.) marital status education level has credit in default? average yearly account balance has housing loan? has personal loan? contact communication type last contact day of the month last contact month of year last contact duration number of contacts during campaign number of contacts before this campaign outcome of previous campaign Assignment Tasks:
1. Load and Explore the Dataset Handle missing or unknown values (e.g., unknown in categorical features). Display basic stats and visualize class distribution. Preprocess the Data Convert categorical variables using Label Encoding or One-Hot Encoding. Scale numeric features (e.g., using StandardScaler). Split the Data Use 80% data for training and 20% for testing. Apply train_test_split().
2. Train Classification Models Train the following models: Logistic Regression K-Nearest Neighbors Random Forest Classifier
3. Evaluate the Models Compare using: Accuracy Confusion Matrix . Classification Report . ROC-AUC score Visualize Results Plot confusion matrix and ROC curves.
'''

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,roc_auc_score,roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder



'''
Step 1 : Exploratory Data Analysis
'''
print("="*40)
print("Step 1 : Exploratory Data Analysis")
print("="*40)

df = pd.read_csv("bank-full.csv",sep=';') # In dataset, seperater used is ;
print("First 5 records of the dataset : \n", df.head())
print("Shape of the dataset : ", df.shape)
print("Column Info : \n",df.info())
print("Basic statistics : \n",df.describe())
print("Null values count : \n",df.isnull().sum())

# Handle 'unknown' values, replace with NaN then fill with mode

df.replace('unknown',np.nan,inplace = True)
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0],inplace=True)

print("After handling unknows- null values :")
print(df.isnull().sum())

#plot 1 - Target class distribution
plt.figure(figsize=(8,5))
df['y'].value_counts().plot(kind='bar', color=['steelblue','salmon'])
plt.title("Target class distribution (Y)")
plt.show()


'''
Step 2 : Preprocessing
'''
print("="*40)
print("Step 2 : Preprocessing")
print("="*40)

#Encoding
le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col].astype(str))

print("After Label Encoding :\n", df.head())

#Split features and target

X = df.drop('y', axis = 1)
Y = df['y']

#Scale numeric features

scaler =StandardScaler()
X_scaled = scaler.fit_transform(X)

#Train test split

X_train,X_test,Y_train,Y_test = train_test_split(X_scaled,Y,test_size=0.2,random_state=42,stratify=Y)

print("Train size : ",X_train.shape[0])
print("Test size : ",X_test.shape[0])


'''
Step 3 : Model building
'''

print("="*40)
print("Step 3 : Model building")
print("="*40)

lr= LogisticRegression (max_iter=1000,random_state=42)
knn= KNeighborsClassifier(n_neighbors=7)
rf = RandomForestClassifier(n_estimators=100,random_state=42)

lr.fit(X_train,Y_train)
knn.fit(X_train,Y_train)
rf.fit(X_train,Y_train)

lr_pred = lr.predict(X_test)
knn_pred = knn.predict(X_test)
rf_pred = rf.predict(X_test)

lr_prob = lr.predict_proba(X_test)[:,1]
knn_prob = knn.predict_proba(X_test)[:,1]
rf_prob = rf.predict_proba(X_test)[:,1]

'''
Step 4 : Model Evaluation
'''

print("="*40)
print("Step 4 : Model Evaluation")
print("="*40)

models = {
    'Logistic Regression' : (lr_pred,lr_prob),
    'KNN' : (knn_pred,knn_prob),
    'Random Forest' : (rf_pred,rf_prob)
}

for name,(pred,prob) in models.items():
    print(f"\n{'='*45}")
    print(f"  {name}")
    print(f"{'='*45}")

    print(f"Accuracy : {accuracy_score(Y_test,pred):.4f}")
    print(f"ROC-AUC : {roc_auc_score(Y_test,prob):.4f}")

    print("Classification Report :\n")
    print(classification_report(Y_test,pred,target_names=['No','Yes']))

    #Confusion Metrices

fig, axes = plt.subplots(1,3,figsize=(15,4))

for ax,(name,(pred, _)) in zip(axes,models.items()):
    sns.heatmap(confusion_matrix(Y_test,pred),
                annot = True,fmt='d',cmap='Blues',ax=ax,
                xticklabels=['No','Yes'],
                yticklabels=['No','Yes'])
    ax.set_title(f"{name}\n Accuracy : {accuracy_score(Y_test,pred):.3f}")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
plt.tight_layout()
plt.show()
        
#ROC Curves

plt.figure(figsize=(7,5))
colors =['steelblue','salmon','green']

for (name,(pred,prob)),color in zip(models.items(),colors):
     fpr,tpr,_ = roc_curve(Y_test,prob)
     auc = roc_auc_score(Y_test,prob)
     plt.plot(fpr,tpr,color=color,
              label=f"{name} (AUC = {auc:.3f})",linewidth=2)
     
plt.plot([0,1],[0,1],'k--',linewidth=1,label= "Random Classifier")
plt.title("ROC Curves - all models")
plt.xlabel("Flase Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()

'''
Step 5 : Final output
'''

print("="*40)
print("Step 5 : Final output")
print("="*40)

X_test_df = pd.DataFrame(
     scaler.inverse_transform(X_test),
     columns = df.drop('y',axis=1).columns).round(2)

X_test_df['Actual'] = Y_test.values
X_test_df['LR_Predicted'] = lr_pred
X_test_df['KNN_Predicted'] = knn_pred
X_test_df['RF_Predicted'] = rf_pred

print("Sample predictions \n")
print(X_test_df[['age','balance','duration','Actual','LR_Predicted','KNN_Predicted','RF_Predicted']].head(10))

X_test_df.to_csv('bank_predictions.csv')
print("Saved to  bank_predictions.csv")



