# you can easily calculate any thing without using for loop
import numpy as np
prices=np.array([100,200,300])
discount=10
final_prices=prices-(prices*discount/100)
print(final_prices)

# multyplying in whole array
arr=np.array([100,200,300])
res=arr*2
print(res)

#adding some value in 2d array
arr_2d=np.array([[1,2,3],[4,5,6]])
vector=np.array([10,20,30])
res=arr_2d+vector
ans=arr_2d[0]+vector
print(res)
print(ans)

"""
👉 Broadcasting means NumPy automatically stretches arrays of different shapes to make their shapes compatible during arithmetic operations.
It avoids explicit loops and lets you do operations between arrays of different sizes.

"""
