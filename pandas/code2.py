import pandas as pd

# Series = A Pandas 1-Dimensional labeled array that cab hold any data type. Think of it like a single column in a spreadsheet (1-Dimensional)

data = [100, 102, 104]

series = pd.Series(data)	# 'S' is uppercase as its a constructor

print(series)

print()

data = [100.1, 102.2, 104.3]

series = pd.Series(data)

print(series)

print()

data = ["A", "B", "C"]

series = pd.Series(data)

print(series)

print()

data = [True, False, True]

series = pd.Series(data)

print(series)