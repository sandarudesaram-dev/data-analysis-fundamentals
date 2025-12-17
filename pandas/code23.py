# Filtering = Keeping the rows that match a condition

import pandas as pd

df = pd.read_csv("data.csv")

water_pokemon = df[df["Type1"] == "Water"]

dual_water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
# Use "|" (C style operator) instead of "or"

print(water_pokemon)

print()

print(dual_water_pokemon)