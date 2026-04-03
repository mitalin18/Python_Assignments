'''

'''


from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# STEP 1 : LOAD & COMBINE DATASETS
# ─────────────────────────────────────────────

fake = pd.read_csv('Fake.csv')
true = pd.read_csv('True.csv')

print("Fake news shape :", fake.shape)
print("True news shape :", true.shape)

#add label column
fake['label'] = 0
true['label'] =1

#combine both datasets
df = pd.concat([fake,true],ignore_index=True)

print("\nshape of combined dataset :", df.shape)
print("\n First 5 rows :")
print(df.head())
print("\n Last 5 rows :")
print(df.tail())

# ─────────────────────────────────────────────
# STEP 2 : DATA PREPROCESSING
# ─────────────────────────────────────────────

#Drop null values
df.dropna(inplace=True)
print("\n Null values after dropping :")
print(df.isnull().sum())

#Use title + text as a combined feature
df['content'] = df['title'] + ' ' + df['text']
print("\n Label distribution")
print(df['label'].value_counts())

#Plot - class distribution

plt.figure(figsize=(5,4))
df['label'].value_counts().plot(kind = 'bar',
                                color=['salmon','steelblue'],
                                edgecolor = 'black'
                                )

plt.title('Class Distribution (0 = fake,1 = Real)')
plt.xlabel('Label')
plt.ylabel('Count')
plt.xticks([0,1],['Fake','Real'],rotation=0)
plt.tight_layout()
plt.show()

# ─────────────────────────────────────────────
# STEP 3 : FEATURE EXTRACTION - TF-IDF
# ─────────────────────────────────────────────

X = df['content']
Y = df['label']

# Train test split BEFORE TF-IDF
X_train,X_test, Y_train, Y_test = train_test_split(
    X,Y,test_size=0.2,random_state=42, stratify=Y
)

print("\n Train size ",X_train.shape[0])
print("\n Test size ",X_test.shape[0])

# TF-IDF Vectorization
tfidf= TfidfVectorizer(max_features=5000,stop_words='english')
x_train_tfidf = tfidf.fit_transform(X_train)
x_test_tfidf = tfidf.fit_transform(X_test)

print("\n TF-IDF matrix shape (train) :",x_train_tfidf.shape)


# ─────────────────────────────────────────────
# STEP 4 : MODEL TRAINING
# ─────────────────────────────────────────────

lr = LogisticRegression(max_iter=1000,random_state=42)
dt = DecisionTreeClassifier(max_depth=10,random_state=42)

lr.fit(x_train_tfidf,Y_train)
dt.fit(x_train_tfidf,Y_train)

lr_pred = lr.predict(x_test_tfidf)
dt_pred = dt.predict(x_test_tfidf)

#Hard voting classifier
hard_voting = VotingClassifier(
    estimators=[('lr', LogisticRegression(max_iter=1000,random_state=42)),
                ('dt',DecisionTreeClassifier(max_depth=10,random_state=42))],
    voting= 'hard')

hard_voting.fit(x_train_tfidf,Y_train)
hard_pred = hard_voting.predict(x_test_tfidf)

#soft voting classifier

soft_voting = VotingClassifier(
    estimators=[('lr',LogisticRegression(max_iter=1000,random_state=42)),
                ('dt',DecisionTreeClassifier(max_depth=10,random_state=42))         
                ]
)

soft_voting.fit(x_train_tfidf,Y_train)
soft_pred = soft_voting.predict(x_test_tfidf)


# ─────────────────────────────────────────────
# STEP 5 : MODEL EVALUATION
# ─────────────────────────────────────────────


models = {
    'Logistic Regression' : lr_pred,
    'Decision Tree' : dt_pred,
    'Hard Voting' : hard_pred,
    'Soft Voting' : soft_pred
}

for name,pred in models.items():
    print(f"\n{'='*45}")
    print(f"  {name}")
    print(f"{'='*45}")

    print("Accuracy : ",accuracy_score(Y_test,pred))
    print("Classification report : ")
    print(classification_report(Y_test,pred,
                                target_names=['Fake','Real']))
    

#Confusion matrix
fig,axes = plt.subplots(1,4,figsize=(20,4))

for ax,(name,pred) in zip(axes,models.items()):
    sns.heatmap(confusion_matrix(Y_test,pred),
                annot=True, fmt='d',cmap='Blues',ax=ax,
                xticklabels=['Fake','Real'],
                yticklabels=['Fake','Real'])
    ax.set_title(f"{name}\n Accuracy : {accuracy_score(Y_test,pred)}")
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')

plt.show()

#Accuracy comparison bar chart
plt.figure(figsize =(7,4))
names = list(models.keys())
accs = [accuracy_score(Y_test,pred) for pred in models.values()]
bars = plt.bar(names,accs,color=['steelblue','salmon','green','orange'],
               edgecolor='black')

for bar, acc in zip(bars,accs):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.002,
             f'{acc:.3f}',ha = 'center',fontsize=10)
    
plt.title("Model accuracy comparison")
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.ylim(0,1.1)
plt.show()

#Hard vs soft voting comparison
plt.figure(figsize=(5, 4))
voting_names = ['Hard Voting', 'Soft Voting']
voting_accs  = [accuracy_score(Y_test, hard_pred),
                accuracy_score(Y_test, soft_pred)]
bars = plt.bar(voting_names, voting_accs,
               color=['steelblue', 'salmon'], edgecolor='black')
for bar, acc in zip(bars, voting_accs):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.002,
             f'{acc:.3f}', ha='center', fontsize=11)
plt.title('Hard Voting vs Soft Voting')
plt.ylabel('Accuracy')
plt.ylim(0, 1.1)
plt.tight_layout()
plt.show()


# ─────────────────────────────────────────────
# STEP 6 : FINAL OUTPUT - PREDICTIONS
# ─────────────────────────────────────────────

results_df = pd.DataFrame({
    'text'  :X_test.values,
    'Actual' :Y_test.values,
    'LR_Predicted' : lr_pred,
    'DT_Predicted': dt_pred,
    'Hard_Predicted' : hard_pred,
    'Soft_Predicted' : soft_pred,   

})

results_df['Actual_Label']      = results_df['Actual'].map({0:'Fake', 1:'Real'})
results_df['Soft_Voting_Label'] = results_df['Soft_Predicted'].map({0:'Fake', 1:'Real'})
 
print("\nSample Predictions :")
print(results_df[['Actual_Label', 'Soft_Voting_Label']].head(10))
 
results_df.to_csv('fakenews_predictions.csv', index=False)
print(f"\nSaved to fakenews_predictions.csv ({len(results_df)} rows)")