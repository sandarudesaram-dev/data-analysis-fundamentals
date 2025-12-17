# Different selection techniques using pandas

import pandas as pd

df = pd.read_csv("data.csv")

# SELECTION BY COLUMN: SELECTING MULTIPLE COLUMNS

print(df[["Name", "Height", "Weight"]]) # truncated output

print()

print(df[["Weight", "Name"]])

print()

print(df[["Name", "Height", "Weight"]].to_string())	# full output