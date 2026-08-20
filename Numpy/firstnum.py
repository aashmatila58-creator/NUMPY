import numpy as np 

# print(np.__version__)
# my_list = [1,2,3,4,5]
# my_list = my_list*3
# print(my_list)
# array = np.array([1,2,3,4,5,6])
# array = array * 2
# print(array)
# print(type(array))

# Multidimensional array
array = np.array([['A','B', 'C'],
                  ['D','E','F'],
                  ['G','H','I']])
print(array.shape)
# print(array[0,0]) #multidimensional index 
word = array[0,0] + array[2,1]
print(word)