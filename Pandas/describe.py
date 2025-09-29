import pandas as pd
data={
    "name":['Ram','shaym','ghanshaym'],
    "age":[10,20,30],
    "city":['noida','delhi','patna']  
}
df=pd.DataFrame(data)
print(df)
print('data describe')
print(df.describe())
