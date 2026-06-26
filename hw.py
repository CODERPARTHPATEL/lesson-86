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