import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Opening a file using Absolute path
data = pd.read_csv(r'C:\Users\mar.urbano\Desktop\Desktop 2\Python\PortfolioProjects\IMDB Project\IMDB-Movie-Data.csv')

#Asking Pandas to display all columns of the DataSet
#pd.options.display.max_columns=None

#Displaying column names
#print(data.columns)

# 1 - Top 10 rows of DataSet
#print(data.head(10))

# 2 - Last 10 rows of DataSet
#print(data.tail(10))

#Checking data type
#print(type(data))

# 3 - Shape of our DataSet - Number of Rows and Columns based on the index of the tuple returned by .shape
#print('Number of rows: ',data.shape[0])
#print('Number of columns: ',data.shape[1])

# 4 - Getting general informations: number of rows, number of columns, columns' names, data type per column, number of non-null values per column, memory usage...
#print(data.info())

# 5 - Check missing values: The code below with .values.any() will return a boolean. True if our DataSet contains any missing values, False if it doesn't
#print('Any missing values?',data.isnull().values.any())

'''
Using two .sum() functions will count all missing values in our DataFrame.
If we used only one, it would return the names of the columns with a NaN count in each of them, like a group by
If we use only .isnull() we get our whole DataSet with booleans. True for NaNs.
'''
#print('Any missing values?',data.isnull().sum().sum())

#We can visualize missing data using sns.heatmap().
#Plots created using seaborn need to be displayed like ordinary matplotlib plots. This can be done using the plt.show()
#sns.heatmap(data.isnull())
#plt.show()

#Show percentage of missing values 
#perc_missing = data.isnull().sum().sum() / len(data) * 100
#print(perc_missing)

# 6 - Drop missing values: Since .dropna() by default creates a new DataFrame (or Series) with no NaNs, we have to create a new variable in order to print the results
#If we wanted to modify the current DataFrame, we'd have to modify the 'inplace' method to 'True': data.dropna(inplace=True)
#data_dropna = data.dropna()
#print(data_dropna.isnull().sum().sum())

# 7 - Check if there are any duplicated values
#dup_data = data.duplicated().any()
#print('Are there any duplicated values?',dup_data)

#Drop duplicates
#data=data.drop_duplicates()

# 8 - Summary statistics for numerical columns
#print(data.describe())

# 9 - Exibir apenas o título dos filmes com duração superior a 180 minutos
#print(data[data['Runtime (Minutes)']>180]['Title'])
#or
#print(data[data['Runtime (Minutes)']>180].Title)
#Também poderia botar a coluna 'Title' antes da condição de minutagem, tanto com colchetes ou com o ponto, que o resultado seria o mesmo

# 10 - Year that had the highest average voting
#data.groupby('Year')['Votes'].mean().sort_values(ascending=False)
#sns.barplot(x='Year',y='Votes',data=data)
#plt.title('Votes By Year')
#plt.show()

# 11 - Year that had the highest average Revenue
#data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)
#sns.barplot(x='Year',y='Revenue (Millions)',data=data)
#plt.title('Revenue By Year')
#plt.show()

# 12 - Average rating for each director
#print(data.groupby('Director')['Rating'].mean().sort_values(ascending=False))

# 13 - Top 10 lengthy movie titles and runtime
#top10_len = data.nlargest(10, 'Runtime (Minutes)')[['Title','Runtime (Minutes)']].set_index('Title')
#sns.barplot(x='Runtime (Minutes)',y=top10_len.index,data=top10_len)
#plt.show()

# 14 - Number of movies per year
#print(data.groupby('Year')['Title'].count().sort_values(ascending=False))
# or
#data['Year'].value_counts()
#sns.countplot(x='Year',data=data)
#plt.title('Number Of Movies Per Year')
#plt.show()

# 15 - Most popular movie title (highest revenue)
#print(data.groupby('Title')['Revenue (Millions)'].max().sort_values(ascending=False))
# or displaying only the one result that we want
#print(data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]['Title'])

# 16 - Top 10 Highest Rated Movie Titles, its Directors and Ratings
#top10_len = data.nlargest(10,'Rating')[['Title','Director','Rating']].set_index('Title')
#sns.barplot(x='Rating',y=top10_len.index,data=top10_len)
#plt.show()

# 17 - Top 10 Highest Revenue Movie Titles and its Revenues
#top_10 = data.nlargest(10,'Revenue (Millions)')[['Title','Revenue (Millions)']].set_index('Title')
#sns.barplot(x='Revenue (Millions)',y=top_10.index,data=top_10)
#plt.title('Top 10 Highest Revenue Movie Titles')
#plt.show()

# 18 - Average Rating of Movies Year Wise
#print(data.groupby('Year').Rating.mean().sort_values(ascending=False))

# 19 - Does Rating Affect The Revenue? 
#sns.scatterplot(x='Rating',y='Revenue (Millions)',data=data)
#plt.show()
#(Based on the scatter plot, the answer is Yes)

# 20 - Classify Movies Based on Ratings [Excellent, Good, and Average]
'''
def ratings (rating):
    if rating >= 7.5:
        return 'Excellent'
    elif rating >= 6:
        return 'Good'
    else:
        return 'Average'

data['rating_grade']=data['Rating'].apply(ratings)
print(data.head())
'''

# 21 - Count Number of Action Movies
#print(data['Genre'].dtype)    #It's an object datatype, therefore we'll use string methods
#print(len(data[data['Genre'].str.contains('action',case=False)]))

'''
# 22 - Find Unique Values From Genre - Some movies have more than one genre associated with them
list1 = []
for value in data['Genre']:
    list1.append(value.split(','))

#print(list1)

one_d = []
for item in list1:
    for item1 in item:
        one_d.append(item1)

#print(one_d)

uni_list = []
for item in one_d:
    if item not in uni_list:
        uni_list.append(item)

print(uni_list)

print(len(uni_list))
'''













