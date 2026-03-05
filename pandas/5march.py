import pandas as pd 

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

# print(df["country"])
# print(df["country"].unique())
# print(df["country"].nunique())  # number of unique values
print(df["country"].value_counts())
