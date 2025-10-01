import pandas as pd
data={
    "name":['Ram',None,'ghanshaym'],
    "age":[10,None,30],
    "city":['noida','delhi','patna'] ,
    "salary":[7000,60000,74000] 
}
df=pd.DataFrame(data)
print(df)
# this will return number of missing value in a column

print(df.isnull().sum())

