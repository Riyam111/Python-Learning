import pandas as pd
data={
    "name":['Ram','shaym','ghanshaym'],
    "age":[10,20,30],
    "city":['noida','delhi','patna']  
}
df=pd.DataFrame(data)
print(df)
print('after performing insert method')
# inserting new column and list of values on a specific location
df.insert(0,"id",[11,12,13])
print(df)
# assigning new value to specific column
df.loc[1,"age"]=40
print(df)
# adding a column in last and adding some property in that
df["bonus"]=df["age"]*0.1
print(df)

# delete a column
df.drop(columns=["bonus"],inplace=True)
print(df)