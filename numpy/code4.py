import numpy as np

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
		  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
		  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

print(array[0][0][0]) # Chain indexing

print(array[0, 0, 0]) # Multidimensional indexing (faster)
