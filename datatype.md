# Object Types / Data Types

- Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

- Set : set('abc'), {'a', 'b', 'c'}

- File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

- Boolean : True, False
- None : None
- Funtions, modules, classes

- Advance: Decorators, Generators, Iterators, MetaProgramming

# 🧠 In Python:
- Variables don't have types. Objects do.
- This means:
- A variable is just a name (or reference) that points to an object in memory.
- The object has the actual data type, not the variable.
- ✅ Example:
- x = 5          # 'x' refers to an integer object
- print(type(x))  
- x = "hello"     # now 'x' refers to a string object
- print(type(x))  

## 🔁 Example: How List References Work

```python
>>> a = [1, 2, 3]
>>> b = a
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]

>>> a = [1, 2, 3]
>>> a[0] = 32
>>> a
[32, 2, 3]
>>> b
[1, 2, 3]

>>> b[0] = 34
>>> b
[34, 2, 3]

>>> a = [1, 2, 3]
>>> b = a
>>> b[0] = 33
>>> b
[33, 2, 3]
>>> a
[33, 2, 3]

>>> b = a[:]  # makes a shallow copy
>>> b[0] = 3
>>> b
[3, 2, 3]
>>> a
[33, 2, 3]

### 💡 Notes:
- `b = a` → Both `a` and `b` refer to the same list in memory.
- Changing `a` or `b` affects the same object.
- `b = a[:]` → Creates a **shallow copy**, so changes to `b` no longer affect `a`.