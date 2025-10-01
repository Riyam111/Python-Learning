# customer data 
import pandas as pd
customer=pd.DataFrame({
    'customerId':[1,2,3],
    'name':['ram','shaym','gyan']
})

order=pd.DataFrame({
    'customerId':[1,2,4],
    'amount':[100,200,300]
})

df_merged=pd.merge(customer,order,on="customerId",how="right")
print("right join")
print(df_merged)
