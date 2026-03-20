import pandas as pd

df = pd.read_csv('pandas\mckinsey.csv')
# print(df)

# implicit index vs explicit index :
"""
implicit index : always start with  0.  : iloc 
explicit index : start with any number. (we define as we want)  : loc
"""

# print(df.loc[0])
# print(df.iloc[0])

# print(df.iloc[1:5,1:4])
# print(df.loc[1:5,'year':'continent'])

# print(df.iloc[[1,3,5,7,9],[0,2,3,4]])
# print(df.iloc[-1])  # last row  print 
# print(df.loc[-1])  # error 

# print(df.loc[1:10:2])
# print(df.iloc[1:10:2])

# print  year ==2002  : 
# print(df.loc[df['year']==2002])

# multiple  condition and  print  row  : 

"""
task :1 year ==2001 and continent ==india , year country ,life_exp gdp_cap
"""
"""
result =df.loc[(df['year']==1997)  | (df['country']=='India') ,['year','country','life_exp','gdp_cap']]
print(result)
"""
# task :2  display life_exp >35 and country name   

