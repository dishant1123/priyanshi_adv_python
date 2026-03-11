import pandas as pd 
import numpy as np

df =pd.read_csv("pandas\mckinsey.csv")
"""
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.columns)
print(df.dtypes)
print(df.shape)
print(df.isnull().sum())
print(df.size)
"""

# specific row and column : 

"""print(df['country'])
print(df[['country','year']])
"""

# drop , add : 

"""df =df.drop("country",axis =1)
df.drop(['country','year'],axis =1,inplace=True)

df["next_survery_year"] = df["year"] +3
print(df.head())
"""

# unique , nunique ,value_counts :

"""print(df["country"])
print(df["country"].unique())
print(df["country"].nunique())  # number of unique values
print(df["country"].value_counts())
"""

# new index : 
# df['new_index']=np.arange(3,1707)
# print(df.head())
# print(df.tail())
# print(df.index)
# print(df.index.values)

df.index =np.arange(5,1709)
print(df)

# implicit index vs explicit index :
"""
implicit index : always start with  0.
explicit index : start with any number. (we define as we want)
"""
