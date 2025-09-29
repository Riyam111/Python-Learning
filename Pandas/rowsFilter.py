import pandas as pd
data={
    "name":['Ram','shaym','ghanshaym'],
    "age":[10,20,30],
    "city":['noida','delhi','patna'] ,
    "salary":[7000,60000,74000] 
}
df=pd.DataFrame(data)
old_age=df[df['age']>10]
print('old age greater than 10')
print(old_age)

filterd=df[(df['age']==10)& (df['name']=='Ram')]
print(filterd)

high_salary=df[(df['salary']>7000)& (df['age']>20)]
print(high_salary)

