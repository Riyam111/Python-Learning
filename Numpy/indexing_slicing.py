"""
to access index
array[index] #1d array
array[row,column] #2d
"""
# accessing valu at specific index
import numpy as np
arr=np.array([10,20,30,40])
print(arr[0])
print(arr[-1])

# slicing
print(arr[1:3]) #index 1 to 2
print(arr[:3]) #index 0 to 2
print(arr[::2]) # every second element
print(arr[::-1]) #reverse array

# fancy indexing
print(arr[[0,1,3]])

# filtering 
print(arr[arr>25]) #output=> [30 40]

# reshaping(it does not create copy it create view)
print(arr.reshape(2,2)) 
#output=>>
# [[10 20]
# [30 40]]

"""
both do same work but 
.ravel() -> create views
.flatten() ->create copy
"""
# converting multidimensional array to 1d array
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())



