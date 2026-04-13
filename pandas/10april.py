import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv("pandas\movies.csv")
directors = pd.read_csv("pandas\directors.csv")

# print(movies)
# print(directors)

# task  :1 remove  first  col  in both data  movies and directors  :
# task  :2 join  ==> director_id join 


""" 
if (grade =='a') 
{
    bs =60000; 
    other =8000; 
    
    
}
else if()

"""

# top 10  movies by directors : 
movies = movies.drop(['Unnamed: 0'], axis=1)
directors = directors.drop(['Unnamed: 0'], axis=1)

df = movies.merge(directors, left_on='director_id', right_on='id',how='inner')
# print(df.head(10))

# top 10 director name by movies :

top_10_directors = df.groupby('director_name').size().nlargest(10)
print(top_10_directors)

plt.bar(top_10_directors.index, top_10_directors.values, color='red', align='center', width=0.5, edgecolor='black', linewidth=1, label='Top 10 Directors by Movies')
plt.xlabel('Director Name')
plt.ylabel('Number of Movies')
plt.title('Top 10 Directors by Movies')
plt.show()

# top 10 movies by revenue : 