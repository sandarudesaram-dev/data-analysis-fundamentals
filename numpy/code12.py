# Comparison operators

import numpy as np

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100)
print(scores >= 60)
print(scores < 60)

print()

scores[scores < 60] = 0
print(scores)