```
>>> keyvalue={'chai':'biscuit','roti':'sabzi','dal':'chawal'}
>>> keyvalue
{'chai': 'biscuit', 'roti': 'sabzi', 'dal': 'chawal'}
>>> keyvalue['chai']
'biscuit'
>>> keyvalue['chai']='bread'
>>> keyvalue
{'chai': 'bread', 'roti': 'sabzi', 'dal': 'chawal'}

>>> for key in keyvalue:
...  print(key,keyvalue[key])
...
chai bread
roti sabzi
dal chawal
>>> for key in keyvalue:
...   print(key,keyvalue[key].split(",")) 
... 
chai ['bread']
roti ['sabzi']
dal ['chawal']
>>> for key in keyvalue:
...  print(key,keyvalue[key],sep=",")    
...
chai,bread
roti,sabzi
dal,chawal
>>>
```


```
>>> chai
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'chai' is not defined
>>> chai={'ravi':'hii','ritu':'hello','pihu':'how'}
>>> chai
{'ravi': 'hii', 'ritu': 'hello', 'pihu': 'how'}
>>> del chai[ritu]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ritu' is not defined
>>> del chai['ritu']
>>> chai
{'ravi': 'hii', 'pihu': 'how'}
>>> chai['ritu']='how'
>>> chai
{'ravi': 'hii', 'pihu': 'how', 'ritu': 'how'}
>>> chai.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pop expected at least 1 argument, got 0
>>> chai.pop('ritu')
'how'
>>> chai
{'ravi': 'hii', 'pihu': 'how'}
>>>
```
```
>>> keyval=['hello','hii','how']
>>> keyval
['hello', 'hii', 'how']
>>> dafaultval='what'
>>> newkeyval=dict.fromkeys(keyval,dafaultval)
>>> newkeyval
{'hello': 'what', 'hii': 'what', 'how': 'what'}
>>> 
```