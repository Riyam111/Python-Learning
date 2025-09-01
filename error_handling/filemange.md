### first method to open file 
```
if your file is notfound then given code create one txt file named test
file=open('test.txt','w')
try:
file.write('chai aur code')
finally:
file.close()
```

### second method is 
```
with open ('test.txt','w') as file:
file.write('chai aur python')
```