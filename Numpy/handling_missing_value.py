import numpy as np
arr=np.array([1,2,np.nan,4,np.nan])
print(np.isnan(arr))
#output=>[False False  True False  True]
# we can not equate np.nan==np.nan

#np.nan_to_num(array,nan=value),default=0
new_array=np.nan_to_num(arr,nan=10)
print(new_array)
#output=>[ 1.  2. 10.  4. 10.]

# infinite
num1=np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(num1))

#replace infinte
cleaned_arr=np.nan_to_num(num1,posinf=1000,neginf=-1000)
print(cleaned_arr)

