import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Opening a file using Absolute path
yt = pd.read_csv(r'C:\Users\mar.urbano\Desktop\Desktop 2\Python\PortfolioProjects\Youtube Channel Project\top-5000-youtube-channels.csv')

#Asking Pandas to display all columns of the DataSet
pd.options.display.max_columns=None

#Displaying column names
print(yt.columns)

# 1 - Display All Rows Except the Last 5 rows Using the Head Method
yt.head()

# 2 - Display All Rows Except the First 5 Rows Using the Tail Method
yt.tail()

# 3 - Find Shape of Our Dataset (Number of Rows And Number of Columns)
yt.shape

# 4 - Get Information About Our Dataset 
yt.info()

# 5 - Get Overall Statistics About The Dataframe
yt.describe()

# 6 - Data Cleaning  (Replace '--'  to NaN)
yt=yt.replace('--',np.nan,regex=True)

# 7 - Check Null Values In The Dataset
nans=yt.isnull().sum().sum()
print(nans)

# Percentage of mising values
total_values=(yt.count().sum())+(yt.isnull().sum().sum())

total_values

nans/total_values*100

sns.heatmap(yt.isnull())
plt.show()

yt.dropna(inplace=True)
sns.heatmap(yt.isnull())
plt.show()
print(yt.shape)

# 8 - Data Cleaning [ Rank Column ]
yt.dtypes
yt['Rank']=yt['Rank'].str[:-2]
yt['Rank']=yt['Rank'].str.replace(',','').astype('int')

yt['Rank'].dtype

# 9 - Data Cleaning [ Video Uploads & Subscribers ]
yt.dtypes
yt['Video Uploads']=yt['Video Uploads'].astype('int')
yt['Subscribers']=yt['Subscribers'].astype('int')

yt.dtypes

# 10 - Data Cleaning [ Grade Column ]
yt.Grade.unique()
yt.Grade = yt.Grade.map({'A++ ':5,'A+ ':4,'A ':3,'A- ':2,'B+ ':1})

yt.dtypes

# 11 - Find Average Views For Each Channel
yt['Avg_views'] = yt['Video views']/yt['Video Uploads']
yt.head()

# 12 - Find Out Top Five Channels With Maximum Number of Video Uploads
yt.nlargest(5,['Video Uploads'])
# or
yt.sort_values(by='Video Uploads',ascending=False).head()

# 13 - Find Correlation Matrix
yt.corr()

# 14 - Which Grade Has A Maximum Number of Video Uploads?
sns.barplot(x='Grade',y='Video Uploads',data=yt)
plt.show()

# 15 - Which Grade Has The Highest Average Views?
sns.barplot(x='Grade',y='Avg_views',data=yt)
plt.show()

# 16 - Which Grade Has The Highest Number of Subscribers?
sns.barplot(x='Grade',y='Subscribers',data=yt)
plt.show()

# 17 - Which Grade Has The Highest Video Views?
yt.groupby('Grade')['Video views'].mean().sort_values(ascending=False)
sns.barplot(x='Grade',y='Video views',data=yt)
plt.show()

# 18 - Order the number os times each grade appears in the dataset
yt['Grade'].value_counts().sort_values(ascending=False)
