### diff b/w repr,str,print
```python
s = 'hello\nworld'
print(str(s))   # Output: hello
                #         world

print(repr(s))  # Output: 'hello\nworld' ← This shows the escape sequence clearly  repr() is like a developer's X-ray goggles — it shows the full skeleton of the object, which is critical for debugging, testing, and understanding what's really happening behind the scenes.

print(s)  # output hello
          #        world
# in internal prinnt Calls str() internally to convert the object to a string (if available).Sends the result to the console.
```
### here are some example and properties of number system
```python
>>> import math
>>> math.floor(2.3)
2
>>> math.floor(3.9)
3
>>> math.trunc(3.9)
3
>>> math.trunc(2.5)
2
>>> math.trunc(-2.5)
-2
>>> math.floor(-2.5)
-3
>>> int('64',8) #octal value of 64
52
>>> import random
>>> random.random()
0.7683211112260019
>>> random.randint(1,10)
10
>>> random.randint(1,10)
7
>>> random.randint(1,10)
9
>>> random.randint(1,10)
4
>>> l1=['a','b','c','d']
>>> random.choice(l1)
'c'
>>> random.choice(l1)   
'a'
>>> random.choice(l1)
'c'
>>> random.shuffle(l1)
>>> print(l1)
['a', 'b', 'c', 'd']
>>> random.shuffle(l1)
>>> print(l1)
['d', 'c', 'b', 'a']
>>> 0.1+0.1+0.1
0.30000000000000004
>>> # this is known python error
>>> from decimal import Decimal
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')
Decimal('0.3')
>>> setone={1,2,3,4}
>>> setone | {1,3,6}
{1, 2, 3, 4, 6}
>>> setone
{1, 2, 3, 4}
>>> setone-{1,2,3,4}
set()
>>> type({})
<class 'dict'>
>>> True
True
>>> True +3
4
>>> True is 1
False
```
### how sliceing work here
```python
>>> chai='adarak chai'
>>> print(chai)
adarak chai
>>> slice_chai=chai[0:6]
>>> print(slice_chai)
adarak
>>> chai[-2]
'a'
>>> chai[-2:-1]
'a'
>>> num_list="0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[:6]
'012345'
>>> num_list[2:]
'23456789'
>>> num_list[0:8:3]
'036'
```
### here will see use of strip()
```
>>> chai="     hii kaise ho  "
>>> print(chai)
     hii kaise ho  
>>> print(chai.strip())
hii kaise ho
>>> 
```
### use of replace
```
>>> chai="lemon tea"
>>> print(chai.replace("tea","coffee"))
lemon coffee
>>> chai
'lemon tea'
>>> 
```
### use of split
```
>>> flavour="lemon, ginger, masala, mint"
>>> print(flavour.split())
['lemon,', 'ginger,', 'masala,', 'mint']
>>> print(flavour.split(", "))
['lemon', 'ginger', 'masala', 'mint']
>>>
names = input().strip().split(",")
it will take input as riya,raju,adi
then remove extra space
then make a list ["riya","raju"]
```
### use of find , count, format
```
>>> chai="masala chai"
>>> print(chai.find("chai"))
7
>>> chai="chai chai chai chai"
>>> print(chai.count("chai"))
4
>>> chai_type="ginger"
>>> quantity=2
>>> order="i ordered {} cup of {} tea"
>>> order
'i ordered {} cup of {} tea'
>>> print(order.format(quantity,chai_type))      
i ordered 2 cup of ginger tea
>>>
```
### convert list to string
```
>>> chai_variety=["lemon","masal","ginger"]
>>> chai_variety
['lemon', 'masal', 'ginger']
>>> print(" ".join(chai_variety))
lemon masal ginger
>>> print(",".join(chai_variety))
lemon,masal,ginger
>>>
>>> print(len(chai_variety))
3
```

```
>>> chai="he said \"i killed somone\""
>>> chai
'he said "i killed somone"'
>>>
```
### print raw data
```
>>> chai="c:\user\pwd"
  File "<stdin>", line 1
    chai="c:\user\pwd"
         ^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>> chai="c:\\user\\pwd"
>>> chai
'c:\\user\\pwd'
>>> print(chai)
c:\user\pwd
>>> chai=r"c:\user\pwd"
>>> chai
'c:\\user\\pwd'
>>> print(chai)
c:\user\pwd
>>>
```
### boolean
```
>>> chai="masala chai"
>>> print("masala" in chai)
True
>>>
```

### how zip ( ) work
```
names = ["sachin", "ramesh", "kalam"]
dates = [100, 50, 100]

zipped = zip(names, dates)
print(list(zipped))
output is =>>[("sachin", 100), ("ramesh", 50), ("kalam", 100)]
```

### how to store number correspond to values vector
```
names = ["sachin", "ramesh", "kalam"]
dates = [100, 50, 100]
birthday_map = {}

for name, date in zip(names, dates):
    birthday_map.setdefault(date, []).append(name)

print(birthday_map)
output=>{100: ["sachin", "kalam"], 50: ["ramesh"]}
```







