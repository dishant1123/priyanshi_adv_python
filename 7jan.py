import numpy as np 

"""
a=np.random.randint(low=-1,high=10,size=(3,3))

print(a)
print(np.count_nonzero(a))
"""

# vstack and hstack :

"""
a=np.random.randint(low=-1,high=10,size=(3,3))
b=np.random.randint(low=-10,high=10,size=(3,3))
print(a)
print(np.vstack((a,b)))
print(np.hstack((a,b)))

print(np.repeat(a,3))
print(np.repeat(a,3,axis=0))
print(np.repeat(a,3,axis=1))
"""

# linear algebra :
"""
a=np.random.randint(low=1,high=10,size=(3,3))
b=np.random.randint(low=-10,high=10,size=(3,3))
print(a)

print(np.linalg.det(a))
print(np.linalg.matrix_rank(a))  # hw to check

print(np.identity(3))
"""

# statistical methods : 

a=np.random.randint(low=1,high=10,size=8).reshape(2,4)

print("original matrix : \n",a)
# print(np.mean(a))  # 
# print(np.median(a))  #
# print(np.std(a))
# print(np.var(a))

# print(np.min(a))
# print(np.min(a,axis=0))
# print(np.min(a,axis=1))

# print(np.argmin(a))
# print(np.argmin(a,axis=0))
# print(np.argmin(a,axis=1))

# print(np.max(a))
# print(np.max(a,axis=0))
# print(np.max(a,axis=1))

# print(np.argmax(a))
# print(np.argmax(a,axis=0))
# print(np.argmax(a,axis=1))

# print(np.sort(a))  # row  wise 
# print(np.sort(a,axis=0))
# print(np.sort(a,axis=1))

