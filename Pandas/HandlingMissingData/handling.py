import pandas as pd
data={
    "name":['Ram',None,'ghanshaym'],
    "age":[10,None,30],
    "city":['noida',None,'patna'] ,
    "salary":[7000,6000,74000] 
}
df=pd.DataFrame(data)
print(df)
# Drop rows with any NaN values:
#df.dropna(inplace=True)
#print(df)
# filling nan value to 0 by default
#df.fillna(0,inplace=True)
#print(df)
# filling a specific value in nan of col
mean_age = df['age'].mean()
df['age'] = df['age'].fillna(mean_age)
print(df)