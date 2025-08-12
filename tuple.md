### here we will see how tuple work 
| Feature         | **List**                                                     | **Tuple**                                                                                      |
| --------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| **Mutability**  | ✅ Mutable — you can change elements, append, remove, etc.    | ❌ Immutable — once created, elements cannot be changed, added, or removed.                     |
| **Syntax**      | Square brackets: `my_list = [1, 2, 3]`                       | Parentheses: `my_tuple = (1, 2, 3)`                                                            |
| **Performance** | Slower — due to mutability and extra methods.                | Faster — immutability allows internal optimizations.                                           |
| **Methods**     | Many (e.g., `.append()`, `.remove()`, `.pop()`, `.extend()`) | Few (e.g., `.count()`, `.index()`)                                                             |
| **Use case**    | When you need a collection that can change.                  | When you need a fixed collection (e.g., coordinates, database records) or as a dictionary key. |
| **Hashable**    | ❌ Not hashable (can’t be used as a dictionary key)           | ✅ Hashable if all elements are immutable.                                                      |

```
>>> wordlist=('hii','hello','how')
>>> wordlist
('hii', 'hello', 'how')
>>> newword=('what','why')
>>> newword
('what', 'why')
>>> mergeword=newword+wordlist
>>> mergeword
('what', 'why', 'hii', 'hello', 'how')
>>> mergeword=wordlist+newword
>>> mergeword
('hii', 'hello', 'how', 'what', 'why')
>>> mergeword[0]
'hii'
>>> (a,b,c,d,e)=mergeword
>>> a
'hii'
>>> b
'hello'
>>> c
'how'
>>> e
'why'
>>> mergeword.count('hello')
1
>>> b
'hello'
>>> c
'how'
>>> e
'why'
>>> mergeword.count('hello')
1
'how'
>>> e
'why'
>>> mergeword.count('hello')
1
'why'
>>> mergeword.count('hello')
1
1
>>> mergeword.remove('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'remove'
>>> mergeword.append('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>>
```
