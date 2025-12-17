# Filtering

# Refers to the process of selecting elements from an array that match a given condition.

import numpy as np

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
	         [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]

print(teenagers)	# Output: [17 16 15] - This is boolean indexing
# Boolean indexing flattens our array

print()

adults = ages[(ages >= 18) & (ages < 65)]
# & is used instead of and beacuse NumPy uses C style arrays
# | is used instead of or beacuse NumPy uses C style arrays
print(adults)

print()

seniors = ages[ages >= 65]
print(seniors)

print()

evens = ages[ages % 2 == 0]
print(evens)

print()

odds = ages[ages % 2 != 0]
print(odds)