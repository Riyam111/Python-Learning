# addition without using loop
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
res=arr1+arr2
print(res)

# multiplication without using loop
arr3=arr1*3
print(arr3)

"""
👉 Vectorization means replacing explicit Python loops with NumPy array operations (which are implemented in optimized C code).
This makes code much faster and shorter.
"""