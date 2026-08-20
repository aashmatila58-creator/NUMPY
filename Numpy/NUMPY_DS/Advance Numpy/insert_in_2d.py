# import numpy as np

# arr_2d = np.array([[1,2,],[3,4]])
# print(arr_2d)

# new_arr_2d = np.insert(arr_2d, 1, [5,6], axis=0)
# print(new_arr_2d)




# APPEND

# import numpy as np

# arr = np.array([12,13,14,15,16])
# new_arr = np.append(arr, [16,17,18,19,20])

# print(new_arr)




# CONCATE

"""
np.concatenate((array1, array2), axis = 0)

axis 0 > vertical stacking
axis 1 > horizontal stacking
"""

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

new_arr = np.concatenate((arr1, arr2))
print(new_arr)

