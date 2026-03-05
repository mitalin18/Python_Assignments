import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Loading and exploring data
#loading dataset
df = pd.read_csv("student_performance_ml.csv")

#First 5 records
print("First 5 records :")
print(df.head())

#Last 5 records
print("\n Last 5 records :")
print(df.tail())

#Total number of rows and column
print("Total number of rows and column (Shape): ")
print(df.shape)

#List of column names
print("List of column names :")
print(df.columns)

#Data type of column
print("\n Data types")
print(df.dtypes)


# Count students, pass, fail

#total students
total_students = len(df)
print("Total students : ", total_students)

#Count pass
pass_count = (df['FinalResult']==1).sum()
print("Total Passed : ", pass_count)

#Count fail
fail_count = (df['FinalResult']==0).sum()
print("Total Failed : ", fail_count)


#Calculate statistical measures
print("Average StudyHours :",df['StudyHours'].mean())
print("Average Attendance : ",df['Attendance'].mean())
print("Maximum PreviousScore :",df['PreviousScore'].max())
print("Minimum SleepHours :",df['SleepHours'].min())


#Distribution of FinalResult

result_counts = df['FinalResult'].value_counts()
print(result_counts)

#percentage calculation
percentage = df['FinalResult'].value_counts(normalize=True) * 100
print("\n Percentage Calculation :")
print(percentage)

'''
Is Dataset Balanced?
If Pass = Fail (close to 50%-50%) → Balanced
If one class > 70% → Imbalanced
Example Justification:
If Pass = 60% and Fail = 40%, the dataset is moderately balanced but slightly biased toward Pass.
'''

#Observations/ analyze
print(df.groupby('FinalResult')['StudyHours'].mean())
print(df.groupby('FinalResult')['Attendance'].mean())

'''
Students who passed generally have higher average StudyHours.
Higher Attendance percentage correlates with better FinalResult.
Students who failed tend to have lower StudyHours and irregular attendance.
Academic consistency (attendance + study) appears strongly linked to success.
'''


#Histogram of StudyHours
sns.histplot(df['StudyHours'])
plt.title("Distribution of Study Hours")
plt.show()

'''
This shows how study hours are distributed.
If most students are in the middle range, it means average study time is common.
If very few students study extremely high hours, the graph will show fewer bars on the right side.
'''

#Scatter Plot StudyHours vs PreviousScore

sns.scatterplot(x='StudyHours',
                y = 'PreviousScore',
                hue = 'FinalResult',
                data = df
                )
plt.title("StudyHours vs PreviousScore")
plt.show()

'''
This shows the relationship between study hours and previous score.
Different colors represent Pass (1) and Fail (0).
If pass students are mostly at higher study hours and higher scores, then study hours positively affect performance.
'''
#Boxplot for Attendance
sns.boxplot(y = df['Attendance'])
plt.title("Attendance Boxplot")
plt.show()

'''
The box shows the middle 50% of attendance values.
Points outside the box lines are outliers (very low or very high attendance).
'''

#AssignmentsCompleted vs FinalResult

sns.boxplot(x='FinalResult',
            y = 'AssignmentsCompleted',
            data = df
            )
plt.title("AssignmentsCompleted vs FinalResult")
plt.show()

'''
If students who passed have a higher median number of assignments 
completed, then completing assignments increases chances of passing.
'''

#SleepHours vs FinalResult

sns.boxplot(x = 'FinalResult',
            y = 'SleepHours',
            data = df
            )
plt.title("SleepHours vs FinalResult")
plt.show()

'''
This shows how sleep hours differ between Pass and Fail students.
If both groups have similar medians, sleep alone does not guarantee success.
Balanced sleep helps, but study habits matter more.
'''


