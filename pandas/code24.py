# Filtering = Keeping the rows that match a condition

import pandas as pd

df = pd.read_csv("data.csv")

ff = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
# Use "&" (C style operator) instaed of "and"

print(ff)

print()

FF = df[(df["Type1"] == "Normal") & (df["Type2"] == "Flying")]

print(FF)