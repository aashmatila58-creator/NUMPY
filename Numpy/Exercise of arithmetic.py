import numpy as np
#  Exercise
# radii = np.array([1, 2, 3])
# print(np.pi * radii ** 2) #A = pi*r^2


# Element-wise arithmetic
# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])

# print(array1 + array2)


# Comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])

scores[scores < 75] = 0
print(scores)


