#it help in estimatiing the missing value like you have 10,20,40 50 then
#it will predict missing value which is 30
import pandas as pd
data={
    "name":['radha','Krishna','ram','raju','raj',None],
    "age":[20,None,50,60,70,None]

}
df=pd.DataFrame(data)
print('before interpolation')
print(df)
#linear interpolation
#df['age']=df['age'].interpolate(method="linear")
#print('after interpolation')
#print(df)

# What limit_direction does

#forward → fills NaN by looking ahead (uses earlier values to fill later gaps).

#backward → fills NaN by looking backward (uses later values to fill earlier gaps).

#both → allows interpolation in both directions.

#⚡ Important: limit_direction only matters if the missing values are at the edges (start or end) of your data.
print('after interpolation')
df['age']=df['age'].interpolate(method='linear',limit_direction='backward')
print(df)
