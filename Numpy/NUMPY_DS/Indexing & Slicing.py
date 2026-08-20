# Indexing & slicing 
# Fancy indexing, sorten masking


# Access.py
# syntax -> array[index] means 1d array , array[row, column] means 2d array
# import numpy as np

# arr = np.array([12,20,30,40,50,60])

# print(arr[0])  #first element
# print(arr[2])  
# print(arr[-1])  # last element




"""
slicing 
syntax -> array[start:stop:step]

arr[start:end] , start to end - 1

negative step, -1 reverse

"""

# import numpy as np

# arr = np.array([12,13,14,15,16,17,18])
# print(arr[1:5])    #index 1 to 5
# print(arr[:3])     #index 0 to 3
# print(arr[::2])    #every second element
# print(arr[::-1])





# FANCY indexing means selecting multiple elements at once
# import numpy as np

# arr = np.array([12,13,14,15,16,17,18,19])

# print(arr[[0, 2 , 4]])





# Filtering data / Boolean masking
import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90])

print(arr[arr > 35])

