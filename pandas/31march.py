import pandas as pd

df= pd.DataFrame({
    "name" :["priyanshi","kaki","deep","henil","mihir"],
    "math" :[90,67,80,90,60],
    "science" :[85,90,70,80,56]
})

# print(df)
df['avg']=df.apply(lambda x :(x['math']+x['science'])/2,axis =1 )
# print(df)

def grade(a):
    if a>=80:
        return "Distinction"
    elif a>=60:
        return "First Class"
    else :
        return "Second Class"
    
df['grade'] =df["avg"].apply(grade)
print("original dataframe : \n",df)    

"""
        name  math  science   avg         grade
0  priyanshi    90       85  87.5   Distinction
1       kaki    67       90  78.5   First Class
2       deep    80       70  75.0   First Class
3      henil    90       80  85.0   Distinction
4      mihir    60       56  58.0  Second Class
"""

# print only specific columns : name avg grade 

"""
new_col = df.filter(items=['name','avg','grade'])
print("specific columns : \n",new_col)
"""

# print  only name startwith 'p':

new_col = df.filter(like='pr')
new_col = df.filter(regex='^s')

print("specific columns : \n",new_col)