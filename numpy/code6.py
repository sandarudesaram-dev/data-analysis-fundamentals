# Slicing

import numpy as np

array = np.array([[1, 2, 3, 4],
		  [5, 6, 7, 8],
		  [9, 10, 11, 12],
		  [13, 14, 15, 16]])

# array[start:end:step]

print(array[0])
print(array[2])
print(array[-1])
print(array[-3])

print()

print(array[0:3])
print(array[1:4])
print(array[1:])
print(array[0:])

print()

print(array[0:4:2])
print(array[::2])
print(array[::-1])
print(array[::-2])