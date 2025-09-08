# insert in array
import numpy as np
arr1=np.array([1,2,3,4,5])
arr1=np.insert(arr1,2,9)
print(arr1)

# inserting in 2d array
arr_2d=np.array([[1,2],[3,4],[4,5]])
arr_2d=np.insert(arr_2d,1,[8,9],axis=0)
arr_2d2=np.insert(arr_2d,1,[8,9,10,11],axis=1)
print(arr_2d)
print(arr_2d2)

# append in array(add)
arr2=np.array([1,2,3,4,5])
arr2=np.append(arr2,[9])
print(arr2)

# join two array
"""
np.concatenate((array1,array2),axis=0)
axis 0>vertical stacking
axis 1>horizontal stacking
"""
arr3=np.concatenate((arr1,arr2))
print(arr3)

# delete value from array
arr4=np.delete(arr3,1)
print(arr4)

# delete row/column from 2d array
arr5=np.delete(arr_2d,0,axis=0)
print(arr5)

"""
merge two array horigentally or vertically
vstack() row wise
hstack() column wise
"""
num1=np.array([1,2,3])
num2=np.array([4,5,6])
print(np.vstack((num1,num2))) # vertically stack
print(np.hstack(((num1,num2)))) # horizontally


"""
np.split()
equal
np.hsplit()
np.vsplit()
"""
# spliting array into k parts
# In summary, np.vsplit splits arrays vertically (along the 0th axis, or rows), 
# while np.hsplit splits arrays horizontally (along the 1st axis, or columns).
num=np.array([10,20,30,40,50,60])
print(np.split(num,2))
num_2d=np.array([[1,2],[3,4]])
print(np.vsplit(num_2d,2))
print(np.hsplit(num_2d,2))


