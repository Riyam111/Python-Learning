import pandas as pd
data={
    "name":['Ram','shaym','ghanshaym'],
    "age":[10,20,30],
    "city":['noida','delhi','patna']  
}
df=pd.DataFrame(data)
print(df)
#creating new csv file
df.to_csv("output.csv",index=False)
#creating new json file
df.to_json("output.json",index=False)
#creating new xlsx file
df.to_excel("output.xlsx",index=False)