import numpy as np 

"""
board casting  : it is  ability to perfrom operations on array of diiferent shapes without manually copying the data.  

numpy automatically stretches the smaller array  to match the larger one. 
"""

a1=np.arange(10,50,10)  # start  stop  step 
print(a1)

# print(np.tile(a1,3)) # repeats the array 3 times

a2=np.tile(a1,(3,1))  # col  wise  
print(a2)

a2=np.tile(a1,(3,1)).T  # row wise 
print(a2)