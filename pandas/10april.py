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

"""top_10_directors = df.groupby('director_name').size().nlargest(10)
print(top_10_directors)

plt.bar(top_10_directors.index, top_10_directors.values, color='red', align='center', width=0.5, edgecolor='black', linewidth=1, label='Top 10 Directors by Movies')
plt.xlabel('Director Name')
plt.ylabel('Number of Movies')
plt.title('Top 10 Directors by Movies')
plt.show()
"""
# top 10 movies by revenue : 

"""days=[1,2,3,4,5,6,7,8,9,10]  # days 
temparature=[35,37,38.90,29,31,30,27,26,25,24]

plt.plot(days,temparature,color = 'red',label = 'temperature',marker = 'o',linewidth = 2,markersize = 6,linestyle = '-',markeredgecolor = 'black')
plt.xlabel('Days')
plt.ylabel('Temparature')
plt.title('Temparature')
plt.show()
"""

marks = [100,99,78,89,50,88,67]
name =["dev","sudev","het","jay","ram","sita","priya"]

plt.bar(name,marks,color="red",align="center",width=0.5,edgecolor="black",linewidth=1,label="marks")
plt.xlabel("name")
plt.ylabel("marks")
plt.title("marks of students")
plt.xticks(rotation=90,ha="right",fontsize=10)
plt.yticks(rotation=80,ha="right",fontsize=10)
plt.show()

