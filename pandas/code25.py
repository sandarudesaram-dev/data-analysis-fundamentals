# Aggregate functions = Reduces a set of values into a single summary value
#			Used to summarize and analyze data
#			Often used with groupby() function

import pandas as pd

df = pd.read_csv("data.csv")

print(df)

print()

# Aggregate functions applied to the whole dataframe

print(df.mean(numeric_only=True))

print()

print(df.sum(numeric_only=True))

print()

print(df.min(numeric_only=True))

print()

print(df.max(numeric_only=True))

print()

print(df.count())	# Counts the number of values within each column