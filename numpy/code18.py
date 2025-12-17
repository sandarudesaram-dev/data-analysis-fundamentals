# Random Numbers

import numpy as np

rng = np.random.default_rng()

print(rng.integers(1, 7))

print(rng.integers(low=1, high=101))
# Using keyword arguments is not necessary but it is more readable.

print(rng.integers(low=1, high=101, size=3))

print(rng.integers(low=1, high=101, size=(3, 2)))

print()

rng = np.random.default_rng(seed=1)
# seed is useful if you want to reproduce the same results

print(rng.integers(low=1, high=101, size=(3, 2)))

