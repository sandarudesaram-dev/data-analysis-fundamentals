# Different selection techniques using pandas

import pandas as pd

# SELECTION BY ROW/S

# INTEGER BASED INDEXING

df = pd.read_csv("data.csv", index_col="Name")

print(df.iloc[0:11])

print()

print(df.iloc[0:11:2])

print()

print(df.iloc[0:11:2, 0:3])   # Selecting indices of columns to be displayed

