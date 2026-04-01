"""
group by  : 
"""

import pandas as pd

df= pd.DataFrame({
    "employess" :["priyanshi","kaki","deep","henil","mihir"],
    "id" :[9,6,8,12,13],
    "department" :["blockchain","developer","blockchain","developer","blockchain"],
    "salary" :[50000,40000,30000,20000,10000],
    "city" :['ahm','surat','baroda','surat','ahm']
})

print(df)

# task :1 department  wise salary  :

"""
department_wise_salary = df.groupby("department")['salary'].sum()
print(department_wise_salary)
"""
# task :2 multiple aggregation  :

"""department_wise_agg = df.groupby("department")['salary'].agg(['sum','mean','min','max'])
print(department_wise_agg)
"""

# task :3  group by with multiple column : department , city 

"""department_city_wise_salary = df.groupby(['department','city'])['salary'].sum()
print(department_city_wise_salary)
"""

# task :4 diff max - min salary  : 
"""result =df.groupby('department')['salary'].apply(lambda x : x.max()-x.min())
print(result)
"""
# task :5 group + filter : 

result =df.groupby('department').filter(lambda x :x['salary'].sum() >= 70000)
print(result)
