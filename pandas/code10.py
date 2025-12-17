import pandas as pd

data = {
	"Name": ["Spongebob", "Patrick", "Squidward"],
	"Age": [30, 35, 50]
	}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

print(df)

print()

print(df.loc["Employee 1"])
print(df.loc["Employee 2"])
print(df.loc["Employee 3"])

print()

print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])