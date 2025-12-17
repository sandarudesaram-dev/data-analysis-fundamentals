# Aggregate functions = summarize data and typically return a single value

import numpy as np

array = np.array([[1, 2, 3, 4, 5],
		  [6, 7, 8, 9, 10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))	# Standard deviation
print(np.var(array))	# Variance (Square of std)
print(np.max(array))
print(np.min(array))
print(np.argmin(array))	# Position of min value
print(np.argmax(array))	# Position of max value

print()

print(np.sum(array, axis=0)) 
# axis=0 means function is applied to all columns.

print(np.sum(array, axis=1)) 
# axis=1 means function is applied to all rows.