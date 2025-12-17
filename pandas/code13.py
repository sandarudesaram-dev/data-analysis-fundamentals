# Importing CSV (Comma-separated values) files

import pandas as pd

df = pd.read_csv("data.csv")

print(df) # truncated output

print()

print(df.to_string()) # full output