import numpy as np

rng = np.random.default_rng()

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
fruit = rng.choice(fruits)
print(fruit)

fruits = rng.choice(fruits, size=3)
print(fruits)

fruits = rng.choice(fruits, size=(3, 3))
print(fruits)