import  pandas as pd 
import numpy as np
"""
a =pd.Series([12,14,15,16,90])
print(a)

a= a.apply(lambda x :x *2)
print(a)

users = pd.Series(["user1","user2","user3","user4","user5"])
print(users)

users = users.apply(lambda x :x.upper())
print(users)
"""

# dataframe :

"""
df = pd.DataFrame(
    {
        "name" : ["John","Mary","Tom","Bill","Steve"],
        "age" : [20,23,25,28,27],
        "city" : ["New York","London","Paris","Istanbul","Tokyo"],
    }
)
print(df)"""
"""
df1 = pd.DataFrame([[1,2],[3,4]],columns=["data1","data2"])
print(df1)

df2 =pd.DataFrame(np.array([[1,2],[3,4]]),columns=["data1","data2"])
print(df2)
"""

# head ,tail , sample, describe  :

data = {
        "name" : ["John","Mary","tom","Bill","Steve","priyanshi","shalin","vijay","ankit","shivani"],
        "age" : [20,23,25,28,27,21,22,23,24,25],
        "city" : ["New York","London","Paris","Istanbul","Tokyo","Delhi","Mumbai","Bangalore","Hyderabad","Chennai"],
    }

df = pd.DataFrame(data)
# print(df)
# print(df.head(3))  # by default  first  5 row  print 
# print(df.tail()) # by default  last  5 row  print
# print(df.sample())
# print(df.describe())
# print(df.info())
print(df.shape)
print(df.size)
print(df.columns)
print(df.index)
print(df.dtypes)