# Broadcasting

'''
Broadcasting allows NumPy to perform operations on arrays with different shapes by virtually expanding dimensions, so they match the larger array's shape.

The dimensions have the same size
OR
One of the dimensions has a size of 1
'''

import numpy as np

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)	# Output: (1, 4)
print(array2.shape)	# Output: (4, 1)

# Dimensions are read from right to left

print(array1 * array2)

print()

array1 = np.array([[1, 2, 3, 4],
		   [5, 6, 7, 8],
		   [9, 10, 11, 12],
		   [13, 14, 15, 16]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)	# Output: (4, 4)
print(array2.shape)	# Output: (4, 1)

print(array1 * array2)