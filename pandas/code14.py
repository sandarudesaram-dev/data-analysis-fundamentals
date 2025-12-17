# Importing JSON (JavaScript Object Notation) files

import pandas as pd

df = pd.read_json("data.json")

print(df)	# truncated output

print()

print(df.to_string()) # full output
