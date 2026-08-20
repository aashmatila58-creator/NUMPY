# CREATINF numpy array operations properties
# Shape.py 

# import numpy as np 
# arr_2d = np.array([[1,2,3],
#                     [4,5,6]])

# print(arr_2d.shape)


# Size.py
# import numpy as np 
# arr = np.array([[12,20,13], [45,30,67]])

# print(arr.size)




# ndim.py -> n means number & dim means dimension
# import numpy as np 
# arr_1d = np.array([1,2,3])
# arr_2d = np.array([[1,2,3,], [4,5,6]])
# arr_3d = np.array([[[1,2], [3,4], [5,6],[7,8]]])

# print(arr_1d.ndim)
# print(arr_2d.ndim)
# print(arr_3d.ndim)



# DATA types of array elements->dtype
# import numpy as np

# arr = np.array([12,13,14,15,16])
# print(arr.dtype)




# Converting from one data type to another 
import numpy as np
arr = np.array([11,12,13,14,15,16,17])
float_arr = arr.astype(float)

print(float_arr)
print(float_arr.dtype)