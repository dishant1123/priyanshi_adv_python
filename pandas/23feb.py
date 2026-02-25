import  pandas as pd
import numpy as np

data ={
    "name":["John","Mary","Tom","Bill","Steve","priyanshi","shalin","vijay","ankit","shivani"],
    "age" :[20,23,25,28,27,21,22,23,24,25],
    "city" :["New York","London","Paris","Istanbul","Tokyo","Delhi","Mumbai","Bangalore","Hyderabad","Chennai"]
    
}
df=pd.DataFrame(data)
# print(df)

# print(df['age'])
# print(df[['name','age']])
# print(df.iloc[0])
# print(df.loc[2,"name"])
# print(df.iloc[2,2])
# print(df.iloc[1:3,1:3])

# df['age'] =df['age'] +1
# print(df)

# df['age'] =[21,22,23,24,25,26,27,28,29,30]
# print(df)

# drop  : 

"""df =df.drop("age",axis =1)
print(df)

df=df.drop(columns=["city"])
print(df)
"""
# df=df.rename(columns={"age":"student_age"})
# print(df)

"""df = pd.read_csv("Movieratingdata1.csv")
print(df)

print(df.head())
print(df.tail())
df = df[["GENRES","RATING"]]
print(df)

"""

df =pd.read_csv("Movieratingdata1.csv")

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

df.replace(["not available","not mension","not value"],np.nan,inplace=True)
# print(df)

# df.fillna(value =0,inplace=True)
# df.fillna({"MOVIE_ID":0},inplace=True)

# df["RATING"] =df["RATING"].astype(float)  # error ==> bcz of not available is string data type. 
# df["RATING"] = df["RATING"].fillna(df["RATING"].mean())

df.fillna(value =0,inplace=True)
# print(df)

df['PRODUCTION_YEAR'] = df['PRODUCTION_YEAR'].astype(int)
df["RATING"] =df["RATING"].astype(float)

# print(df['PRODUCTION_YEAR']>2015)

# data = df[df['PRODUCTION_YEAR']>2015]

# data = df[(df['PRODUCTION_YEAR']>2015) & (df['RATING']>4)]

data = df[df['GENRES'].str.contains("war",na=True)]
print(data)