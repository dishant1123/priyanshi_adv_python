import numpy as np 

"""
broadcasting: it is  ability to perfrom operations on array of diiferent shapes without manually copying the data.  

numpy automatically stretches the smaller array  to match the larger one. 
"""

"""a1=np.arange(10,50,10)  # start  stop  step 
print(a1)
"""
# print(np.tile(a1,3)) # repeats the array 3 times

"""a2=np.tile(a1,(3,1))  # col  wise  
print(a2)
"""
"""a2=np.tile(a1,(3,1)).T  # row wise 
print(a2)

b=np.array([1,2,3])
b2=np.tile(b,(4,1)) .T
print(b2)

print(a2+b2)   # shape mismatch
"""
"""b1=np.array([[1,2,3]]).T
print("b1 : \n",b1)
print(a1+b1)

"""

# 1d and 2d array  for  boardcasting : 

"""a=np.array([[3,5]]).T
print("a : \n",a) 

b=np.array([1,2,3,4])
print("b : \n",b)

print(a+b)
"""
# will  following broadcasting work  : 

"""a=np.arange(8).reshape(2,4)
b=np.arange(16).reshape(4,4)
print("a: \n",a)
print("b: \n",b)
print(a+b)
# as demention  not match so broadcasting not possible. 
"""
# ex :2 

"""a=np.arange(1,10).reshape(3,3)
b=np.array([-1,0,1])

print("a: \n",a)
print("b: \n",b)
print(a+b)
# yes  broadcasting  is  possible
"""
# ex :3 
a=np.arange(1,10).reshape(3,3)
b=np.arange(3,10,3).reshape(3,1)

print("a: \n",a)
print("b: \n",b)
print(a+b)