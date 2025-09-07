# 1.Create a NumPy array of numbers from 1 to 20.
import numpy as np
arr1=np.arange(1,21,1)
print(arr1)
print(arr1.shape)
print(arr1.size)

# 2.Create a 2D array (3x4) filled with numbers from 10 to 21.
arr_2d=np.arange(10,22,1).reshape(3,4)
print(arr_2d)
print("total sum: ",np.sum(arr_2d))
print("row wise sum: ",np.sum(arr_2d,axis=1))
print("col wise sum: ",np.sum(arr_2d,axis=0))



# Create a 3x3 identity matrix
arr_3d=np.eye(3)
print("identity matrix: ",arr_3d)






