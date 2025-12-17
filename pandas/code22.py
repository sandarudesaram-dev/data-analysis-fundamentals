# Filtering = Keeping the rows that match a condition

import pandas as pd

df = pd.read_csv("data.csv")

tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] > 100]

legendary_pokemon = df[df["Legendary"] == 1]		# Method 1
Legendary_pokemon = df[df["Legendary"] == True]		# Method 2

print(tall_pokemon)

print()

print(heavy_pokemon)

print()

print(legendary_pokemon)

print()

print(Legendary_pokemon)

print()

print(df)
