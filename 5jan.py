import numpy as np 
# intrinsic method  : 
"""
arange   ==> start  , stop  , step 
ones ==> 1  ==>default    ==>float  
zeros  ==> 0  ==>default    ==>float
"""
"""
a=np.arange(1,10,2)
print(a)

b=np.arange(1,13).reshape(4,3)
print(b)

c=np.ones(12,dtype=int).reshape(3,4)
print(c)

d=np.zeros(12,dtype=int).reshape(3,4)
print(d)
"""

# task  :1 
"""
 1 1 1 1 1 
 1 0 0 0 1 
 1 0 9 0 1 
 1 0 0 0 1
 1 1 1 1 1
"""

"""e=np.full((3,4),44) 
print(e)

a=np.array([
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14],
    [15,16,17,18,19,20,21],
    [22,23,24,25,26,27,28]
])

b= np.full_like(a,10)
print(b)
"""
import random 

"""a =np.random.randint(low=-10,high =10,size=12).reshape(3,4)
a =np.random.randint(1,4,size=(2,2))  # high  excluded 
print(a)
"""

b=np.random.random(10).reshape(2,5)
print(b)
