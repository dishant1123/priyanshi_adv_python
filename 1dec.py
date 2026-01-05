# numpy : 
"""
use : 

1. matrix easliy 
2. analysis 
3. array manupulating 
"""

"""l1=[1,2,3,4,5,6]
print(l1)

l2=[[1,2],[3,4]]
print(l2)

for i in  l2 :
    print(i)
"""
"""
[
 [1,2],
 [3,4]   
]
"""

#pip install numpy :

import numpy as np 

"""
a=np.array([1,2,3,4,56])
print(a)
b=np.array([1,2,3,4,56,"priyanshi"])
print(b)  # by default it is string

c=np.array([1,2,3,4,5,78.90],dtype=int)
print(c)
d=np.array([1,2,3,4,5,78.95],dtype=float)
print(d)
"""

# 2d array : 

"""a=np.array([[1,2],[3,4],[4,5]])
print(a)
print(a.ndim)# number  of  dimension

b=np.array([[[1,2],[3,4],[4,5]]])
print(b)
print(b.ndim)

c=np.array((1,2,3,4,5,6,"om"))
print(c)
print(c.dtype)
print(c.ndim)
"""

# slicing  : 

"""a=np.array([12,13,16,89,45,23,78,90,355,789])
print(a)
print(a.dtype)
print(a[2])
print(a[2 :8])
print(a[ :8])
print(a[-1])
print(a[-5 :-1])
print(a[-1 :-5 :-1])
print(a[ : :2])
print(a[ : :-2])
print(a[ : :-1])
"""
# 2d array slicing  : 

"""
a=np.array([
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14],
    [15,16,17,18,19,20,21],
    [22,23,24,25,26,27,28]
])

print(a)
print(a[0])
print(a[0,4])
print(a[1:3,2:4])
print(a[2, : : 2])
print(a[2:4 ,: : 2])
"""
# array manipulating :
a=np.array([
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14],
    [15,16,17,18,19,20,21],
    [22,23,24,25,26,27,28]
])
# a[2:7] =900
# a[2:7]=[101,102,103,104,105,106,107]
# a[1:3,1:6]=50
# print(a)

# task  :1 
"""
[[8,9],
[15,16]]

task :2 
[2,10,18,26]

task :3 
[[6,7],
[20,21],
[27,28]]
"""

print(a[[0,1,2,3],[1,2,3,4]])





