# Different selection techniques using pandas

import pandas as pd

# SELECTION BY ROW/S

# SETTING ONE COLUMN TO SERVE AS AN INDEX

df = pd.read_csv("data.csv", index_col="Name")

print(df)

print()

print(df.loc["Pikachu"])

print()

print(df.loc["Charizard"])

print()

# DISPLAYING A ROW WITH SELECTED COLUMNS

print(df.loc["Charizard", ["Height", "Weight"]])

