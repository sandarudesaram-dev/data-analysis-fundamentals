# Random Numbers

import numpy as np

print(np.random.uniform())
# Output: A random floating point number between 0 and 1

print(np.random.uniform(low=-1, high=1))

print(np.random.uniform(low=-1, high=1, size=3))

print(np.random.uniform(low=-1, high=1, size=(3, 2)))

np.random.seed(seed=1)
print(np.random.uniform(low=-1, high=1, size=(3, 2)))