### Sort a list
```python
numbers = [4, 2, 9, 1]
numbers.sort()          # sorts in place
print(numbers)          # [1, 2, 4, 9]

sorted_numbers = sorted(numbers)  # returns new sorted list
print(sorted_numbers)             # [1, 2, 4, 9]
```

### Sort a dictionary by keys
```python
d = {'b': 2, 'a': 1, 'c': 3}
sorted_d = dict(sorted(d.items()))
print(sorted_d)  # {'a': 1, 'b': 2, 'c': 3}
```
### Sort a dictionary by values
```python
d = {'a': 3, 'b': 1, 'c': 2}
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)  # {'b': 1, 'c': 2, 'a': 3}
```
### 2️⃣ Mapping / map()

Apply a function to all elements in an iterable.
```python
numbers = ['1', '2', '3']
numbers_int = list(map(int, numbers))
print(numbers_int)  # [1, 2, 3]

# Example with lambda
squared = list(map(lambda x: x*x, numbers_int))
print(squared)     # [1, 4, 9]

3️⃣ List functions
Create / append
lst = []
lst.append(5)
lst.append(10)
print(lst)  # [5, 10]

List comprehension
lst = [x*x for x in range(5)]
print(lst)  # [0, 1, 4, 9, 16]

Split a string into list
s = "1 2 3"
lst = s.split()  # ['1', '2', '3']
lst = list(map(int, s.split()))  # [1, 2, 3]

4️⃣ Dictionary functions
d = {}

# Assign key-value
d['key'] = 10

# Access keys and values
keys = d.keys()
values = d.values()
items = d.items()  # list of (key, value) tuples

# Check if key exists
if 'key' in d:
    print(d['key'])
```
### ✅ Quick Notes

#### sorted() → returns a sorted copy
#### .sort() → sorts in place

#### map() + list() → convert input strings to numbers quickly
#### dict.items() → for sorting dictionaries or iterating over key-value pairs

#### append() / list comprehension → to build lists dynamically