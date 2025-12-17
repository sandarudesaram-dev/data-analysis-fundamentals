# Data cleaning = the process of fixing/removing:
#		  incomplete, incorrect, or irrelevant data.
#		  ~75% of work done with Pandas is data cleaning

import pandas as pd

df = pd.read_csv("data.csv")

print(df)

print()

# 1. Drop irrelevant columns
df = df.drop(columns=["Legendary", "No"])
print(df)

print()

df = pd.read_csv("data.csv")

# 2. Handle missing data	# dropna = Drop Not Available

df = pd.read_csv("data.csv")
df = df.dropna(subset = ["Type2"])
print(df.to_string())

print()

df = pd.read_csv("data.csv")
df = df.fillna({"Type2": "None"})
print(df.to_string())

print()

# 3. Fix inconsistent values

df = pd.read_csv("data.csv")
df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE", "Water": "WATER"})
print(df.to_string())

print()

# 4. Standadize text

df = pd.read_csv("data.csv")
df["Name"] = df["Name"].str.lower()
print(df.to_string())

print()

# 5. Fix data types

df = pd.read_csv("data.csv")
df["Legendary"] = df["Legendary"].astype(bool)
print(df.to_string())

print()

# 6. Remove duplicate values

df = pd.read_csv("data_dup.csv")
print(df)

print()

df = df.drop_duplicates()
print(df)