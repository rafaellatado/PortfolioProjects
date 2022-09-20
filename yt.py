import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

yt = pd.read_csv(r'C:\Users\mar.urbano\Desktop\Desktop 2\Python\PortfolioProjects\Youtube Channel Project\top-5000-youtube-channels.csv')

#Asking Pandas to display all columns of the DataSet
pd.options.display.max_columns=None

#print(yt.columns)

# 1 - Display All Rows Except the Last 5 rows Using Head Method
#print(yt.head())

# 2 - Display All Rows Except the First 5 Rows Using Tail Method
#print(yt.tail())

# 3 - Find Shape of Our Dataset (Number of Rows And Number of Columns)
#print(yt.shape)

# 4 - Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
#print(yt.info())

# 5 - Get Overall Statistics About The Dataframe
#print(yt.describe())

# 6 - Data Cleaning  (Replace '--'  to NaN)
yt=yt.replace('--',np.nan,regex=True)

# 7 - Check Null Values In The Dataset
#nans=yt.isnull().sum().sum()
#print(nans)

# Percentage of mising values
#total_values=(yt.count().sum())+(yt.isnull().sum().sum())
#print(total_values)
#print(nans/total_values*100)
#sns.heatmap(yt.isnull())
#plt.show()

yt.dropna(inplace=True)
#sns.heatmap(yt.isnull())
#plt.show()
#print(yt.shape)

# 8 - Data Cleaning [ Rank Column ]
#print(yt.dtypes)
yt['Rank']=yt['Rank'].str[:-2]
yt['Rank']=yt['Rank'].str.replace(',','').astype('int')
#print(yt['Rank'].dtype)

# 9 - Data Cleaning [ Video Uploads & Subscribers ]
#print(yt.dtypes)
yt['Video Uploads']=yt['Video Uploads'].astype('int')
yt['Subscribers']=yt['Subscribers'].astype('int')
#print(yt.dtypes)

# 10 - Data Cleaning [ Grade Column ]
#print(yt.Grade.unique())
yt.Grade = yt.Grade.map({'A++ ':5,'A+ ':4,'A ':3,'A- ':2,'B+ ':1})
#print(yt.dtypes)

# 11 - Find Average Views For Each Channel
yt['Avg_views'] = yt['Video views']/yt['Video Uploads']
#print(yt.head())

# 12 - Find Out Top Five Channels With Maximum Number of Video Uploads
#print(yt.nlargest(5,['Video Uploads']))
# or
#print(yt.sort_values(by='Video Uploads',ascending=False).head())

# 13 - Find Correlation Matrix
#print(yt.corr())

# 14 - Which Grade Has A Maximum Number of Video Uploads?
#sns.barplot(x='Grade',y='Video Uploads',data=yt)
#plt.show()

# 15 - Which Grade Has The Highest Average Views?
#sns.barplot(x='Grade',y='Avg_views',data=yt)
#plt.show()

# 16 - Which Grade Has The Highest Number of Subscribers?
#sns.barplot(x='Grade',y='Subscribers',data=yt)
#plt.show()

# 17 - Which Grade Has The Highest Video Views?
#print(yt.groupby('Grade')['Video views'].mean().sort_values(ascending=False))
#sns.barplot(x='Grade',y='Video views',data=yt)
#plt.show()

# 18 - Order the number os times each grade appears in the dataset
#print(yt['Grade'].value_counts().sort_values(ascending=False))
