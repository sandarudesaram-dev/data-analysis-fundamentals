import pandas as pd

data = [100, 102, 104, 200, 202]

series = pd.Series(data, index=["a", "b", "c", "d", "e"])

print(series)

print()

print(series[series >= 200])

print()

print(series[series < 200])