import pandas as pd
data={
    "name":['Ram','shaym','ghanshaym'],
    "age":[10,20,30],
    "city":['noida','delhi','patna']  
}
df=pd.DataFrame(data)
print(df)
print(f'shape:{df.shape}')
print(f'Column Names: {df.columns}')
