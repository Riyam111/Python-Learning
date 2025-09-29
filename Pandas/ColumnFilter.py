# selecting specific column
# filter rows
# combine multiple condition 
# square bracket
# boolean conditions
import pandas as pd
data={
    "name":['Ram','shaym','ghanshaym'],
    "age":[10,20,30],
    "city":['noida','delhi','patna']  
}
df=pd.DataFrame(data)
print(df)
# selecting single column
name=df["name"]
print('column no.1 named=> name')
print(name)
# selecting multiple column
subset=df[["name","age"]]
print('\n subset with name and salary')
print(subset)




