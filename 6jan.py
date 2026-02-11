import numpy as np 
import random 
# end -start / step  
"""
a=np.linspace(0,10,20)  # 
print(a)
"""
"""b=np.random.randint(low=-10,high=10,size=(3,4))
print(b)
print(b.shape)
print(b.ndim)
print(b.itemsize)
print(b.nbytes)  # no of element  *size  of each element  
"""

# rules : 
"""
axis =0 ==> col wise 
axis =1 ==> row wise
"""
"""a=np.arange(1,10).reshape(3,3)
print(a)
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

print(a+10)
print(a-10)
print(a*10)
print(a/10)
print(a%10)
"""

# sum and  multiplication  : 
"""a=np.random.randint(low=-10,high=10,size=(4,3))
b=np.random.randint(low=-10,high=10,size=(3,4))
print("a matrix : \n",a)
print("b matrix : \n",b)

# print(a+b)  # element  wise  addition 
# print(a*b)  # element  wise  multiplication  not  matrix  multiplication

c= np.matmul(a,b)  # matrix multiplication
print("c matrix multiply : \n",c)
"""

# np.where() : 
"""
a=np.random.randint(low=-10,high=10,size=(3,3))
print(a)
print(np.where(a>0))
"""