import numpy as np

# flatten , ravel :  use  to  convert 2d array or 3d array  to  1d array . 

# flatten  : 

"""
a= np.array([[1,2,3],[4,5,6],[7,8,9]])
print("original matrix : \n",a)
print(a.ndim)
a1 =a.flatten()
a1[1] =99
print("convert matrix in to 1d array : \n",a1)
print("after  changes : \n",a)
"""
# ravel : 

"""
a= np.array([[1,2,3],[4,5,6],[7,8,9]])
print("original matrix : \n",a)
print(a.ndim)

a1=a.ravel()  #  [1 2 3 4 5 6 7 8 9]
a1[4] =89
print("convert matrix in to 1d array : \n",a1)
print("original matrix : \n",a)
"""