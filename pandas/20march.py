import pandas as pd
import numpy as np

# drop , dropna , drop_duplicates : 

a= pd.DataFrame([[0,1,2,np.nan,5],[2,0,1,5,np.nan],[5,0,1,np.nan,5],[2,0,1,np.nan,np.nan]])

# print(a)
# a= a.drop(axis=1,columns=[2,3])
# a= a.drop(axis=0,index=[2,3])

# a=a.dropna()
# a=a.dropna(axis=1)
# a=a.dropna(axis=0)
# a=a.dropna(axis=1,inplace=True,how='all')  # if all values  are  nan  then drop that row or col
# a.dropna(axis=1,inplace=True,how='any')  # if all values  are  nan  then drop that row or col

# a=a.drop_duplicates()
# a.drop_duplicates(subset=[1],inplace=True)
# a.drop_duplicates(subset=[1,2],inplace=True)
# a.drop_duplicates(subset=[3,4],inplace=True)
# a.dropna(thresh =2,axis=1,inplace=True)
print(a)

