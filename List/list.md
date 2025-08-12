```
['ravi', 'tina', 'aman']
>>> list[0]
'ravi'
>>> list.remove("tina")
>>> list
['ravi', 'aman']
>>> list[0]="ravindra"
>>> list
['ravindra', 'aman']
>>> list2=["anya"]
>>> list+list2
['ravindra', 'aman', 'anya']
>>> ["Aman"]*3
['Aman', 'Aman', 'Aman']
>>> students = ["Ravi", "Anya", "Tina", "Aman", "Neha"]
>>> students[-2:]
['Aman', 'Neha']
>>> students[::2]
['Ravi', 'Tina', 'Neha']
>>> students[:]
['Ravi', 'Anya', 'Tina', 'Aman', 'Neha']
>>> students.insert(0,"ram")
>>> students
['ram', 'Ravi', 'Anya', 'Tina', 'Aman', 'Neha']     
>>> list=[["ravi","pdf"],["tina","doc"]]
>>> backup=list
>>> list[0][1]="zip"
>>> list
[['ravi', 'zip'], ['tina', 'doc']]
>>> backup
[['ravi', 'zip'], ['tina', 'doc']]
>>> backup=list[:]
>>> list[1][1]="zip"
>>> backup
[['ravi', 'zip'], ['tina', 'zip']]
>>> list=["fax","tina"]
>>> backup=list[:]
>>> backup.append("neha")
>>> list
['fax', 'tina']
>>> backup
['fax', 'tina', 'neha']
>>> list=["ravi","tina"]
>>> list=["ravi","tina","ram"]
>>> backup
['fax', 'tina', 'neha']
>>> list=["ravi","tina"]
>>> list=["ravi","tina","ram"]
>>> backup=list[2:1]
>>> backup
[]
>>> grp1=[["ravi"],["tina"]]
[]
>>> grp1=[["ravi"],["tina"]]
>>> grp2=grp1[:]
>>> grp2=grp1[:]
>>> grp1[0].append("riya")
>>> grp2[0]
>>> grp1[0].append("riya")
>>> grp2[0]
['ravi', 'riya']
['ravi', 'riya']
>>> grp2
>>> grp2
[['ravi', 'riya'], ['tina']]      
>>> grp1.append("ritu")
>>> grp1
[['ravi', 'riya'], ['tina'], 'ritu']
>>> grp2
[['ravi', 'riya'], ['tina']]
>>> meals=["paneer","raita","rasgulla"]
>>> veg=["paneer","raita","roti"]
>>> res=filter(lambda x:x not in veg ,meals)
     
>>> del list
>>> print(len(list(res)))
1
>>> item=['a','b','c']
>>> res=list(map(lambda x: x+'1',item))
>>> print(''.join(res))
a1b1c1
>>> price=[100,200]
>>> update_price=list(map(lambda p: p*1.18,price))
>>> price[1]=300
>>> print(update_price)
[118.0, 236.0]
```
```
>>> list=["ravi","ram","raj"]
>>> list.append("radha")
>>> list
['ravi', 'ram', 'raj', 'radha']
>>> list.pop()
'radha'
>>> list
['ravi', 'ram', 'raj']
>>> list.remove("ravi")
>>> list
['ram', 'raj']
>>> list2=list
>>> list2[0]="radha"
>>> list2
['radha', 'raj']
>>> list 
['radha', 'raj']
>>> list2=list.copy()
>>> list2[0]="ravi"
>>> list
['radha', 'raj']
>>> list2
['ravi', 'raj']
```

```
>>> number=[x**2 for x in range(10)]
>>> number
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
