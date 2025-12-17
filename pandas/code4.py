import pandas as pd

data = [100, 102, 104]

series = pd.Series(data, index=["a", "b", "c"])

print(series.loc["a"])
print(series.loc["c"])
print(series.loc["b"])

print()

print(series)

print()

series.loc["c"] = 200

print(series)

print()

print(series.iloc[0])
print(series.iloc[1])
print(series.iloc[2])