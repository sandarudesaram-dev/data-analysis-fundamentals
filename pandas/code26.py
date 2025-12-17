import pandas as pd

df = pd.read_csv("data.csv")

print(df)

print()

# Aggregate functions applied only to a single column

print(df["Height"].mean())

print()

print(df["Height"].sum())

print()

print(df["Height"].min())

print()

print(df["Height"].max())

print()

print(df["Height"].count())

