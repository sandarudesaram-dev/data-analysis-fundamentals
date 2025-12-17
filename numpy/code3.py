import numpy as np

array = np.array('A')
print(array.ndim)
print(array.shape)

print()

array = np.array(['A', 'B', 'C'])
print(array.ndim)
print(array.shape)

print()

array = np.array([['A', 'B', 'C'],
		  ['D', 'E', 'F'],
		  ['G', 'H', 'I']])
print(array.ndim)
print(array.shape)

print()

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
		  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
		  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
print(array.ndim)
print(array.shape)

print()

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
		  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']]])
print(array.ndim)
print(array.shape)