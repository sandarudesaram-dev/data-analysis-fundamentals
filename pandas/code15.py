# Different selection techniques using pandas

import pandas as pd

df = pd.read_csv("data.csv")

# SELECTION BY COLUMN: SELECTING A SINGLE COLUMN
print(df["Name"])		# truncated output

print()

print(df["Weight"])

print()

print(df["Height"])

print()

print(df["Name"].to_string())	# full output