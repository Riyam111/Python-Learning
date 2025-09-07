 # find number of row and number of column in 2d array
import numpy as np
array2=np.array([[1,2 ,3 ],[4,5,6]])
print(array2.shape)
# output=>(2,3)


# finding number of element in an array
arr1=np.array([[1 ,2,3],[2,4,4]])
print(arr1.size)
# output=>6


# finding array is 1d ,2d or 3d
arr_1d=np.array([1,2,3])
arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_3d=np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)
#output=>
# 1
# 2
# 3


#finding datatype 
arr_float=np.array([10,20.3,3.5])
print(arr_float.dtype)
#output=>float64


#convert one datatype to another datatype
arr_int=arr_float.astype(int)
print(arr_int)
print(arr_int.dtype)
#output =>[10 20  3]
# int64