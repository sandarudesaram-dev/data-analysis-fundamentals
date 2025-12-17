# Different selection techniques using pandas

import pandas as pd

# SELECTION BY ROW/S

# SELECTING A RANGE OF ROWS

df = pd.read_csv("data.csv", index_col="Name")

print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])