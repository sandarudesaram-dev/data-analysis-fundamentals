import pandas as pd

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)

print(series)

print()

print(series.loc["Day 3"])
print(series.loc["Day 2"])
print(series.loc["Day 1"])

print()

series.loc["Day 3"] += 500

print(series.loc["Day 3"])

print()

print(series)