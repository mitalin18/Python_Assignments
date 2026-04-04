''' 
Cluster students into different academic performance groups based on features like:
Final grades
Study time
Failures
Absences
This helps identify:
. Top Performers
. Average Students
. Struggling Students
Dataset Details:
Dataset Name: Student Performance Data Set
.
Selected Features:
Use these numerical features for clustering:
. G1, G2, G3 -> First, second, final grades
. studytime -> Weekly study hours
. failures - Number of past class failures
. absences - Number of school absences

You should create below clusters as
Top Performers (Cluster 0):
High grades and low failure count
High study time and few absences
Average Students (Cluster 1):
Moderate scores and study time
Some failures or absences
Struggling Students (Cluster 2):
Low grades, high failure and absence rate
Low study time
'''

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


'''
---------------------------------------
Load Dataset
---------------------------------------
'''

df = pd.read_csv("student-mat.csv",sep =";")

print("Dataset Shape : ",df.shape)
print("\nFirst 5 rows : ")
print(df.head())

'''
---------------------------------------
Step 2 : Feature Selection
---------------------------------------
'''

features = ['G1','G2','G3','studytime','failures','absences']
X = df[features]

print("Selected Features :\n", features)
print("Basic statistics : \n", X.describe())


'''
---------------------------------------
Step 3 : Feature Scaling
---------------------------------------
'''

scalar = StandardScaler()
X_scaled = scalar.fit_transform(X)
print("Features scaled using StandardScaler")

'''
---------------------------------------
Step 4 : Elbow method - find optimal K
---------------------------------------
'''

inertia = []
K_range = range(1,11)

for k in K_range:
    km = KMeans(n_clusters = k,random_state=42,n_init=10)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

'''
---------------------------------------
Step 5 : Apply K-Means with K = 3
---------------------------------------
'''

kmeans = KMeans(n_clusters=3,random_state=42,n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

#map custers to correct labels based on average G3 score
cluster_g3_mean = df.groupby('Cluster')['G3'].mean().sort_values(ascending=False)
label_map = {
    cluster_g3_mean.index[0] : 0,   # Highest G3 = Top Performers
    cluster_g3_mean.index[1] : 1,
    cluster_g3_mean.index[2] : 2    
}

df['Cluster'] = df['Cluster'].map(label_map)

cluster_names = {
    0 : 'Top performers',
    1: 'Average Students',
    2: 'Struggling Students'   
}

df['Cluster_Label'] = df['Cluster'].map(cluster_names)

print("Cluster counts :\n")
print(df['Cluster_Label'].value_counts())

'''
---------------------------------------
Step 6 : Cluster Analysis
---------------------------------------
'''

summary = df.groupby('Cluster')[features].mean().round(2)
summary.index=[cluster_names[i] for i in summary.index]
summary.index.name = 'Cluster'

print("\n" + "="*55)
print(" CLUSTER SUMMARY — Mean Feature Values")
print("="*55)
print(summary.to_string())
print("="*55)


'''
---------------------------------------
Step 7 : PCA for 2d Visualization
---------------------------------------
'''

pca = PCA(n_components=2,random_state=42)
X_pca = pca.fit_transform(X_scaled)
df['PCA1'] = X_pca[:, 0]
df['PCA2'] = X_pca[:, 1]


palette = {
    'Top Performers':     'green',
    'Average Students':   'steelblue',
    'Struggling Students':'red'
}

'''
---------------------------------------
Step 8 : Plots
---------------------------------------
'''
'''
---------------------------------------
Elbow method
---------------------------------------
'''
plt.figure(figsize=(7,4))
sns.lineplot(x=range(1,11),y=inertia,marker='o',color='steelblue')
plt.axvline(3,color='red',linestyle='--',label='K=3')
plt.title('Elbow Method')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Inertia')
plt.legend()
plt.show()



'''
---------------------------------------
Average Final Grade (G3) per Cluster
---------------------------------------
'''
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Cluster_Label', y='G3')
plt.title('Average Final Grade (G3) per Cluster')
plt.xlabel('Cluster')
plt.ylabel('Average G3')
plt.show()


'''
---------------------------------------
Average Absences per Cluster
---------------------------------------
'''
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Cluster_Label', y='absences')
plt.title('Average Absences per Cluster')
plt.xlabel('Cluster')
plt.ylabel('Absences')
plt.show()


'''
---------------------------------------
Average Failures per Cluster
---------------------------------------
'''
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Cluster_Label', y='failures')
plt.title('Average Failures per Cluster')
plt.xlabel('Cluster')
plt.ylabel('Failures')
plt.show()

'''
---------------------------------------
Feature Heatmap
---------------------------------------
'''
plt.figure(figsize=(8,3))
sns.heatmap(summary,annot=True,fmt='.2f',linewidths=0.5)
plt.title("Cluster feature Heatmap (Mean Values)")
plt.show()
