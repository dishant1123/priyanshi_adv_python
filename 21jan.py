import  numpy as  np 
import random 
"""
1 d array  -vector
2 d array  -matrix
3 d array  -tensor
"""

# 1 d array  : 

"""
a=np.array([1,2,3,4,5,6,7,8,9,10])
print("a : \n",a)
print("a.shape : \n",a.shape)
print("a.ndim : \n",a.ndim)
"""
# 2 d array  : 

"""a= np.array([[1,2,3],[4,5,6],[7,8,9]])
print("a : \n",a)
print("a.shape : \n",a.shape)
print("a.ndim : \n",a.ndim)
"""
# 3 d array  :
"""
a=np.array([[[1,2,3,56],[4,5,6,90]],[[7,8,9,34],[10,11,12,67]]])
print("a : \n",a)
print("a.shape : \n",a.shape)
print("a.ndim : \n",a.ndim)
"""

# vector  : 

a= np.random.randint(low=1,high=16,size=16).reshape(4,4)
print("a : \n",a)

def fun1(x):
    if x %2==0:
        x+=3 
    else :
        x+=4 
    return x 
    
verctorized = np.vectorize(fun1)
print(verctorized(a))

import math 

print("after  using  vectorize  log10 : \n")
vectorlog = np.vectorize(math.log10)
print(vectorlog(a))
