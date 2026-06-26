import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#import dataset
data = pd.read_csv('Titanic Dataset.csv')

#box plot

plt.boxplot(data['SibSp'])
plt.title('SibSp')
plt.show()

plt.boxplot(data['Survived'])
plt.title('survived')
plt.show()

survived_q1 = np.quantile(data['survived'],0.25)
survived_q2 = np.quantile(data['survived'],0.50)
survived_q3 = np.quantile(data['surevived'],0.75)
print('Age Quartiles')

print('Q1 -', survived_q1)
print('Q2 -', survived_q2)
print('Q3 -', survived_q3)

IQR_age = age_q3 - age_q1
print('Interquartile Range :',IQR_age)

#plot histogram
plt.hist(data['Age'])
plt.ylabel('count of passengers')
plt.xlabel('Age')
plt.show()

#quartiles for feature fare
Fare_q1 = np.quantile(data['Fare'],0.25)
Fare_q2 = np.quantile(data['Fare'],0.50)
Fare_q3 = np.quantile(data['Fare'],0.75)

print('Fare Quartiles -')
print('Q1 -',Fare_q1)
print('Q2 -',Fare_q2)
print('Q3 -',Fare_q3)

IQR_fare = Fare_q3 - Fare_q1
print('Interquartile Range:', IQR_fare)

###plot histogram 2
bins = np.arange(0,250,20)
plt.hist(data['Fare'],bins=np.arange(1,250,20))
plt.ylabel('count of passengers')
plt.xlabel('Fare')
plt.xticks(bins)

plt.show()