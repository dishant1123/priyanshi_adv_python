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

df = pd.read_csv("Movieratingdata1.csv")
print(df)