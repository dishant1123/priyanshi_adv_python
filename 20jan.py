import  numpy  as  np
# np.where :  ==> condition  

"""
a=np.array([-3,4,5,6,7,8,9,10,0,-90])

result= np.where(a>=5)  # index of elements
result = np.where(a>0,"pos","neg")
result = np.where(a>0,1,-1)
result = np.where(a%2==0,1,-1)

print(result)
"""
# more  about numpy  : 
"""
1d array  -vector 
2d array  -matrix
3d array  -tensor
"""

# matrix multiplication : 

"""
a :   b :
1 2   5 6
3 4   7 8

(1*5  + 2*7 ) 19  (1*6 +2*8)  22
      
"""

a=np.array([[1,2],[3,4]]) 
b=np.array([[5,6],[7,8]])
print("a : \n",a)
print("b : \n",b)

result =np.matmul(a,b)
print("result : \n",result)

