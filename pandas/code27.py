# Aggregate functions

# Using groupby() functions

import pandas as pd

df = pd.read_csv("data.csv")

group = df.groupby("Type1")

print(group)

print()

print(group["Height"].mean())

print()

print(group["Height"].sum())

print()

print(group["Height"].min())

print()

print(group["Height"].max())

print()

print(group["Height"].count())