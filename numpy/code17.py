# Filtering (Filtering preserving the original shape of the array)

# But where() is lot slower than using boolean indexing

import numpy as np

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
	         [39, 22, 15, 99, 18, 19, 20, 21]])

adults = np.where(ages >= 18, ages, 0)
# where(condition, array, fill value)

print(adults)