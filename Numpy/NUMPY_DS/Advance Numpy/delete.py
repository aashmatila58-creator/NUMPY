""" 
np.delete(array, index, axis = None)
flattern array
"""
# import numpy as np

# arr = np.array([10,20,30,40,50,60])
# print(arr)
# new_arr= np.delete(arr,3)
# print(new_arr)



# DELETE_2D ARRAY
import numpy as np

arr_2d = np.array([[1,2,3,4], [5,6,7,8]])

new_arr_2d = np.delete(arr_2d, 0, axis = 1)
print(new_arr_2d)

