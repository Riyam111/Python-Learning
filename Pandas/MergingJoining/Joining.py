import pandas as pd
customer1=pd.DataFrame({
    'customerId':[1,2,3],
    'name':['ram','shaym','gyan']
})

customer2=pd.DataFrame({
    'customerId':[4,5,6],
    'name':['raj','dev','adi']
})
df_concate=pd.concat([customer1,customer2],axis=0,ignore_index=True)
print(df_concate)