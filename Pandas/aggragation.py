import pandas as pd
data={
    "name":['Ram','Sita','ghanshaym','radha','krishna'],
    "age":[10,20,30,10,20],
    "city":['noida','delhi','patna','barsana','gokul'] ,
    "salary":[7000,60000,74000,80000,40000] 
}
df=pd.DataFrame(data)
print(df)
# here we can use mean,sum,min,max all property
filtered=df.groupby('age')['salary'].mean()
print(filtered)