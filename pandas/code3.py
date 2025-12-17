import pandas as pd

data = [100, 102, 104]

series = pd.Series(data, index=["a", "b", "c"])
# index can be a list/ tuple/ dictionary/ numpy array/ series
# set is not used as a index becuase it does not preserve the order

print(series)

print()

data = [100, 102, 104]

series = pd.Series(data, index=["apartment #1", "apartment #2", "apartment #3"])

print(series)