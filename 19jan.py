import  numpy as  np 
# load txt  :


"""data = np.loadtxt("1.txt")
print("student  data  : \n",data)
""" 
# specific row and col  : 

"""col =np.loadtxt("1.txt",usecols=(0,1),dtype=int)
print(col)
"""
# skid header row : 

"""skip =np.loadtxt("1.txt",skiprows=1)  
print(skip)
"""
# change in data type  : 

"""data =np.loadtxt("1.txt",dtype=str)
print(data)
"""
#unpack columns : 

"""roll,sub1,sub2,sub3 =np.loadtxt("1.txt",unpack=True)
print("\nrollno : \n",roll)
print("\nsub1 : \n",sub1)
"""
# note  : loadtxt fails if missing values exist. 

# genfromtxt : 

data =np.genfromtxt("2.txt",delimiter=",",names=True,encoding="utf-8",filling_values=0,dtype=None,usecols=(0,1))
print(data)

# print(data["salary"])
