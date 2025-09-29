#use of head(),tail()
# we use head for printing row from starting
# and we use tail for printing row from last
# by default we take 5 row
import pandas as pd
df=pd.read_json("output.json")
print('display 2 row from start')
print(df.head(2))
print('display 2 row from last')
print(df.tail(2))