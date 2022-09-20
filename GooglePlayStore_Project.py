import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Opening a file using Absolute path
playstore = pd.read_csv(r'C:\Users\mar.urbano\Desktop\Desktop 2\Python\PortfolioProjects\Google Play Store Apps\googleplaystore.csv')

# Asking Pandas to display all columns of the DataSet
pd.options.display.max_columns=None

# 1. Display Top 5 Rows of The Dataset
playstore.head()

# 2. Check the Last 3 Rows of The Dataset
playstore.tail(3)

# 3. Find Shape of Our Dataset (Number of Rows & Number of Columns)
playstore.shape

# 4. Get Information About Our Dataset
playstore.info()

# Count null values per column
playstore.isnull().sum()

# 5. Get Overall Statistics About The Dataframe
playstore.describe(include='all')

# 6. Total Number of Apps That Contain The Word 'Astrology' In Its Title
len(playstore[playstore.App.str.contains('Astrology',case=False)])

# 7. Find Average App Rating
playstore['Rating'].mean()

# 8.  Find Total Number of Unique Category
playstore['Category'].nunique()

# 9. Which Category Getting The Highest Average Rating?
playstore.groupby('Category')['Rating'].mean().sort_values(ascending=False)

# 10. Find Total Number of App having 5 Star Rating
len(playstore[playstore.Rating==5.0])

# 11. Find Average Value of Reviews

# Check the error message that said we couldn't convert 'object' neither to 'float' or 'int' ('3.0M')
playstore[playstore['Reviews']=='3.0M']['Reviews']

# Solving the above problem

playstore['Reviews'] = playstore['Reviews'].replace('3.0M',3.0)
playstore['Reviews'] = playstore['Reviews'].astype('float')

playstore['Reviews'].dtype

playstore.Reviews.mean()

# 12. Find Total Number of Free and Paid Apps
playstore.groupby('Type')['Type'].count()

# 13.  Which App Has Maximum Reviews?
playstore[playstore['Reviews'].max()==playstore['Reviews']]['App']

# 14. Display Top 5 Apps Having Highest Reviews
playstore.nlargest(5,'Reviews')[['App','Reviews']]

# 15. Find Average Rating of Free and Paid Apps
playstore.groupby('Type')['Rating'].mean()

# 16. Display Top 5 Apps Having Maximum Installs
playstore['Installs'] = playstore['Installs'].str.replace(',','')
playstore['Installs'] = playstore['Installs'].str.replace('+','')

playstore[playstore['Installs']=='Free']

playstore['Installs'] = playstore['Installs'].replace('Free',0)
playstore['Installs'] = playstore['Installs'].astype('int')

playstore.Installs.dtype

playstore.nlargest(5,'Installs')[['App','Installs']]

