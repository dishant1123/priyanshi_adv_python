# pip install  pandas  
"""
pandas : 
1. use for data cleaning  
2. use for data analysis
3. use for data manupulation 
4. csv file  read and write 
5. also using for  SQL similar  function like  filter , groupby , join ,merge ,sort
"""
# seris  : 

import  pandas as pd 

"""
s=pd.Series([1,2,3,4,5,6,7,8,9,10])
print(s)

s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s1)

s2=pd.Series({"maths":90,"science":99,"english":78,"hindi":60},dtype=int)
print(s2)
"""

# head , tail ,sample , shape ,size, ndim, dtype, values ,index ,info : 

"""
s2=pd.Series({"maths":90,"science":99,"english":78,"hindi":60,"physics":99,"chemistry":90,"biology":80,"computer science":95})

print(s2)
print(s2.head())  #  head  :  first  5  rows
print(s2.head(3))
print(s2.tail())
print(s2.tail(3))

print(s2.sample(5))  # random sample  
print(s2.shape)
print(s2.size)
print(s2.ndim)
print(s2.dtype)
print(s2.values)
print(s2.index)
print(s2.info())
"""

# loc , iloc : 
s=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])

"""
print(s)
print(s['a'])
print(s[0])

print(s.loc['a'])
print(s.iloc[4])

print("at",s.at['c'])
print("at",s.at['e'])

print("iat",s.iat[3])
print("iat",s.iat[4])

# label based : 
print(s[['a','c']])
print(s['a' : 'c'])

# boolean based :
print(s[s>=30])
"""

# airthematic : 

"""users =pd.Series([21,22,23,24,25],index=["priyanshi","shalin","vijay","ankit","shivani"])

# print(users.sample())
# print(users+1)
# print(users-1)
# print(users*2)
# print(users/2)

match1 =pd.Series([100,200,300,400,500],index=['a','b','c','d','e'])
match2=pd.Series([100,200,300,400,500],index=['x','b','c','d','e'])

print("original match1 : \n",match1)
print("original match2 : \n",match2)

# print("addition : \n",match1+match2)

result = match1.add(match2,fill_value=100)
print("addition : \n",result)

"""

# statistics :

"""
s=pd.Series([1,2,3,4,5,6,7,8,9,10])

print(s)
print(s.sum())
print(s.mean())
print(s.std())
print(s.min())
print(s.max())
print(s.median())
print(s.var())
print(s.std())
"""

# missing values :

"""s=pd.Series([10,20,30,0,None,50,None])  # np.nan  ==> none 
print(s)

print(s.isnull())
print(s.isnull().sum())
print(s.notnull())
print(s.notnull().sum())

s= s.fillna(0)
print(s)
print(s.isnull().sum())

s=s.dropna()
print(s)

"""

# sort :

s=pd.Series([10,20,11,22,0,30,45,50],index=["z","b","c","a","d","e","f","g"])

# print(s)
# print(s.sort_values())
# print(s.sort_values(ascending=True))
# print(s.sort_values(ascending=False))

print(s.sort_index())
print(s.sort_index(ascending=True))
print(s.sort_index(ascending=False))
