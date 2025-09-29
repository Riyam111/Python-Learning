import pandas as pd
df=pd.read_json("output.json")
print('display the info of dataset')
print(df.info())
