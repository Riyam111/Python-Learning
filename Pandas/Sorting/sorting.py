import pandas as pd
data={
    "name":['Ram','Sita','ghanshaym'],
    "age":[10,20,30],
    "city":['noida','delhi','patna'] ,
    "salary":[7000,60000,74000] 
}
df=pd.DataFrame(data)
print(df)

# sort by value
# df.sort_values(by=['column name 1','column name 2'],ascending=[True/False for first column,True/False for second column],inplace=True)
print('data after sorting by age in desending order')
df.sort_values(by='age',ascending=False,inplace=True)
print(df)


